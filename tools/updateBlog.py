import os
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def is_different(src, dst):
    """
    检查源文件或文件夹和目标文件或文件夹是否不同。
    :param src: 源路径
    :param dst: 目标路径
    :return: 如果不同则返回 True，否则返回 False
    """
    if not os.path.exists(dst):
        return True
    if os.path.isdir(src):
        return False  # 如果是文件夹，暂时不比较
    return os.path.getmtime(src) != os.path.getmtime(dst) or os.path.getsize(src) != os.path.getsize(dst)

def copy_directory(sourceDir, targetDir, exclude=None, callback=None, verbose=False):
    """
    复制 sourceDir 下的所有文件夹到 targetDir，在有重复的时候进行覆盖。
    :param sourceDir: 源目录
    :param targetDir: 目标目录
    :param exclude: 排除列表，包含不需要复制的文件夹名称
    :param callback: 复制完成后执行的回调函数
    :param verbose: 是否显示成功的消息，正数表示显示
    """
    if exclude is None:
        exclude = []

    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    for item in os.listdir(sourceDir):
        s = os.path.join(sourceDir, item)
        d = os.path.join(targetDir, item)
        if item not in exclude:
            try:
                if os.path.isdir(s):
                    if not os.path.exists(d) or is_different(s, d):
                        if os.path.exists(d):
                            shutil.rmtree(d)
                        shutil.copytree(s, d)
                        if verbose:
                            print(f"文件夹 {s} 复制到 {d} 成功")
                else:
                    if is_different(s, d):
                        shutil.copy2(s, d)
                        if verbose:
                            print(f"文件 {s} 复制到 {d} 成功")
            except Exception as e:
                print(f"复制 {s} 到 {d} 失败: {e}")

    if callback:
        callback(verbose)

if __name__ == "__main__":
    sourceDir = "../src"
    targetDir = "/mnt/d/Blog/source/notes/"
    exclude = [
        "SUMMARY.md",
        "updateSummary.py",
    ]

    def update_index(verbose):
        update_index_script = os.path.join(targetDir, "_updateindex.py")
        if os.path.exists(update_index_script):
            os.system(f'python {update_index_script}')
        if verbose:
            print("索引更新完成")

    copy_directory(sourceDir, targetDir, exclude, update_index, verbose=True)