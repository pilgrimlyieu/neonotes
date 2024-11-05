import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def remove_zone_identifier_files(sourceDir):
    """
    递归删除 source_dir 内部所有以 Zone.Identifier 结尾的文件。
    :param source_dir: 源目录
    """
    for root, dirs, files in os.walk(sourceDir):
        for file in files:
            if file.endswith("Zone.Identifier"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"已删除 {file_path}")
                except Exception as e:
                    print(f"删除 {file_path} 失败: {e}")

if __name__ == "__main__":
    source_dir = "../src"
    remove_zone_identifier_files(source_dir)