import os
import shutil
import hashlib
import json

# Root directory of the project
os.chdir((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

RECURSION_DEPTH = 2
MD5_CACHE_FILE  = "cache/updateBlog_md5.json"
VERBOSE         = True

def load_md5_cache():
    """
    Load the MD5 cache from a file if it exists.

    This function checks if the MD5 cache file exists. If it does, it reads the
    file and loads the JSON content into a dictionary. If the file does not
    exist, it returns an empty dictionary.

    Returns:
        dict: A dictionary containing the MD5 cache data if the file exists,
              otherwise an empty dictionary.
    """
    if os.path.exists(MD5_CACHE_FILE):
        with open(MD5_CACHE_FILE, "r", encoding="utf8") as f:
            return json.load(f)
    return {}

def save_md5_cache(cache):
    """
    Save the given MD5 cache to a file.

    Args:
        cache (dict): A dictionary containing the MD5 cache to be saved.

    Raises:
        IOError: If there is an issue writing to the file.
    """
    with open(MD5_CACHE_FILE, "w", encoding="utf8") as f:
        json.dump(cache, f)
    if VERBOSE:
        print("MD5 缓存保存成功")

md5_cache = load_md5_cache()

def calculate_md5(file_path):
    """
    Calculate the MD5 hash of a file.

    Args:
        file_path (str): The path to the file for which the MD5 hash is to be calculated.

    Returns:
        str: The MD5 hash of the file as a hexadecimal string.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def is_different(src, dst):
    """
    Determines if the source file or directory is different from the destination file.

    Args:
        src (str): The path to the source file or directory.
        dst (str): The path to the destination file.

    Returns:
        bool: True if the source is a directory, the destination does not exist, or the 
              MD5 checksums of the source and destination files are different. False otherwise.
    """
    if os.path.isdir(src):
        return True
    else:
        if not os.path.exists(dst):
            return True
        src_md5 = calculate_md5(src)
        dst_md5 = md5_cache.get(dst, None)
        if dst_md5 is None:
            dst_md5 = calculate_md5(dst)
            md5_cache[dst] = dst_md5
        if src_md5 != dst_md5:
            md5_cache[dst] = src_md5
            return True
        return False

def copy_directory(src, dst, excl=None, depth=0):
    """
    Recursively copies a directory from the source to the destination, with options to exclude certain items and limit recursion depth.

    Args:
        src (str): The source directory path.
        dst (str): The destination directory path.
        excl (list, optional): A list of directory or file names to exclude from copying. Defaults to None.
        depth (int, optional): The current depth of recursion. Defaults to 0.

    Raises:
        OSError: If an OS error occurs during copying.
        shutil.Error: If a shutil error occurs during copying.

    Notes:
        - If the destination directory does not exist, it will be created.
        - If an item in the source directory is in the exclusion list, it will be skipped.
        - If the item is a directory and the recursion depth is less than the maximum allowed depth, the function will call itself recursively.
        - If the item is a directory and the recursion depth is equal to or greater than the maximum allowed depth, the destination directory will be removed and the source directory will be copied in its entirety.
        - If the item is a file, it will be copied directly.
        - If VERBOSE is set to True, the function will print messages indicating the success of each copy operation.
    """
    if excl is None:
        excl = []

    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if item in excl:
            continue
        try:
            if is_different(s, d):
                if os.path.isdir(s):
                    if depth < RECURSION_DEPTH:
                        copy_directory(s, d, None, depth+1)
                    else:
                        shutil.rmtree(d)
                        shutil.copytree(s, d)
                        if VERBOSE:
                            print(f"目录 {s} 复制到 {d} 成功")
                else:
                    shutil.copy(s, d)
                    if VERBOSE:
                        print(f"文件 {s} 复制到 {d} 成功")
        except (OSError, shutil.Error) as e:
            print(f"复制 {s} 到 {d} 失败: {e}")

if __name__ == "__main__":
    sourceDir = "src"
    targetDir = "/mnt/d/Blog/source/notes/"
    exclude = [
        "SUMMARY.md",
        "updateSummary.py",
    ]

    update_index_script = "tools/autoIndex.py"
    if os.path.exists(update_index_script):
        os.system(f'python {update_index_script}')
    if VERBOSE:
        print("索引更新完成")

    copy_directory(sourceDir, targetDir, exclude)
    save_md5_cache(md5_cache)