import os

# Root directory of the project
os.chdir((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def remove_zone_identifier_files(sourceDir):
    """
    Removes all files with the ":Zone.Identifier" suffix in the specified directory and its subdirectories.

    Args:
        sourceDir (str): The path to the directory where the search for ":Zone.Identifier" files will begin.

    Returns:
        None

    Raises:
        OSError: If an error occurs while attempting to delete a file, an error message will be printed.
    """
    for root, dirs, files in os.walk(sourceDir):
        for file in files:
            if file.endswith(":Zone.Identifier"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"已删除 {file_path}")
                except OSError as e:
                    print(f"删除 {file_path} 失败: {e}")

if __name__ == "__main__":
    source_dir = "src"
    remove_zone_identifier_files(source_dir)