import os
import re

# ROOT/src
os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

folders = [f for f in os.listdir('.') if os.path.isdir(f)]

abbr_map = {
    '': 'NORMAL',
}

pattern = re.compile(r'(?P<prefix>[a-z]?)(?P<order>\d+)-(?P<name>[\w-]+)\.md')
title_pattern = re.compile(r'^title: (?P<title>.+)$', re.M)
subject_pattern = re.compile(r'《(?P<subject>.+)》课堂笔记')

def __open(*args, **kwargs):
    """
    Opens a file with specified arguments, ensuring newline characters are normalized to '\n' and encoding is set to 'utf-8'.

    Parameters:
    *args: Variable length argument list to be passed to the built-in open function.
    **kwargs: Arbitrary keyword arguments to be passed to the built-in open function.

    Returns:
    file object: A file object as returned by the built-in open function.
    """
    return open(*args, newline='\n', encoding='utf-8', **kwargs)

def getTitle(file):
    """
    Extracts the title from the front matter of a given file.

    Args:
        file (str): The path to the file from which to extract the title.

    Returns:
        str: The extracted title if found, otherwise None.

    Raises:
        IOError: If the file cannot be opened or read.
        IndexError: If the front matter section is not properly formatted.
    """
    with __open(file, 'r') as f:
        front_matter = f.read().split('---\n')[1]
        title_match = title_pattern.search(front_matter)
        if title_match:
            return title_match.group('title')

def getIndex(subject):
    """
    Generates an index of markdown notes in a given subject directory.

    Args:
        subject (str): The path to the subject directory containing markdown notes.

    Returns:
        dict: A dictionary where keys are categories (e.g., 'NORMAL') and values are lists of tuples.
              Each tuple contains the order, title, and name of a note, sorted by order.
    """
    notes = [f for f in os.listdir(subject) if os.path.isfile(os.path.join(subject, f)) and f.endswith('.md') and f != 'index.md']
    index = {
        'NORMAL': [],
    }
    for note in notes:
        match = pattern.match(note)
        if match:
            prefix, order, name = match.groups()
            title = getTitle(os.path.join(subject, note))
            index[abbr_map[prefix]].append((order, title, name))
    for key in index:
        index[key].sort(key=lambda x: int(x[0]))
    return index

def findIndex(subject, name):
    """
    Finds the start and end indices of a specific index section in a markdown file.

    Args:
        subject (str): The directory path where the markdown file is located.
        name (str): The name of the index section to find.

    Returns:
        tuple: A tuple containing the start and end indices of the index section.
               If the section is not found, returns (None, None).
    """
    with __open(os.path.join(subject, 'index.md'), 'r') as f:
        content = f.read()
    index_start_pattern = re.compile(f'^<!-- \\{{\\{{\\{{ INDEX {name} START -->$', re.M)
    index_end_pattern = re.compile(f'^<!-- \\}}\\}}\\}} INDEX {name} END -->$', re.M)
    start_search = index_start_pattern.search(content)
    end_search = index_end_pattern.search(content)
    if not (start_search and end_search):
        return (None, None)
    start, end = start_search.end(), end_search.start()
    return (start, end)

def createIndex(subject, name='NORMAL', content=''):
    """
    Appends an index section to an 'index.md' file within the specified subject directory.

    Args:
        subject (str): The directory path where the 'index.md' file is located.
        name (str, optional): The name of the index section. Defaults to 'NORMAL'.
        content (str, optional): The content to be included within the index section. Defaults to an empty string.

    Returns:
        None
    """
    name = name or 'NORMAL'
    index_content = f'\n\n<!-- {{{{{{ INDEX {name} START -->{content}<!-- }}}}}} INDEX {name} END -->'
    with __open(os.path.join(subject, 'index.md'), 'a') as f:
        f.write(index_content)

def updateIndex(subject):
    """
    Updates the index file for a given subject by reading the current index,
    modifying it with new entries, and writing the updated content back to the file.

    Args:
        subject (str): The path to the subject directory containing the index file.

    The function performs the following steps:
    1. Retrieves the current index for the subject using the getIndex function.
    2. Reads the content of the 'index.md' file in the subject directory.
    3. Iterates through the index items and constructs the new index content.
    4. Finds the position of the current index in the file content.
    5. If the index is found, it replaces the old index with the new one.
    6. If the index is not found, it creates a new index entry.
    7. Writes the updated content back to the 'index.md' file.
    """
    index = getIndex(subject)
    with __open(os.path.join(subject, 'index.md'), 'r') as f:
        content = f.read()
    for name, index in index.items():
        index_content = '\n' + '\n'.join(f'{int(order)}. [{title}]({order}-{name})' for order, title, name in index) + '\n'
        start, end = findIndex(subject, name)
        if start and end:
            content = content[:start] + index_content + content[end:]
        else:
            createIndex(subject, name, index_content)
            continue
        with __open(os.path.join(subject, 'index.md'), 'w') as f:
            f.write(content)

def getSubjectName(subject):
    """
    Extracts the subject name from the 'index.md' file located in the given subject directory.

    Args:
        subject (str): The path to the subject directory.

    Returns:
        str: The extracted subject name.

    Raises:
        AttributeError: If the subject name pattern is not found in the title.
        FileNotFoundError: If the 'index.md' file does not exist in the subject directory.
    """
    raw_title = getTitle(os.path.join(subject, 'index.md'))
    return subject_pattern.search(raw_title).group('subject')

def updateRootIndex():
    """
    Updates the root index file (index.md) with a sorted list of folders and their corresponding subject names.

    The function performs the following steps:
    1. Collects folder names and their corresponding subject names into a list.
    2. Sorts the list by folder names.
    3. Generates the index content in markdown format.
    4. Reads the current content of the index.md file.
    5. Finds the start and end positions of the existing index content.
    6. If the existing index content is found, it replaces it with the new index content.
    7. If the existing index content is not found, it creates a new index section.
    8. Writes the updated content back to the index.md file.

    Note:
    - The function assumes the existence of helper functions: getSubjectName, findIndex, and createIndex.
    - The function uses a custom file opening function __open.

    Raises:
    - Any exceptions raised by the helper functions or file operations are not handled within this function.
    """
    index = []
    for folder in folders:
        index.append((folder, getSubjectName(folder)))
    index.sort(key=lambda x: x[0])
    index_content = '\n' + '\n'.join(f'- [{title}]({name})' for name, title in index) + '\n'
    with __open('index.md', 'r') as f:
        content = f.read()
    start, end = findIndex('.', 'NORMAL')
    if start and end:
        content = content[:start] + index_content + content[end:]
    else:
        createIndex('.', 'NORMAL', index_content)
        return
    with __open('index.md', 'w') as f:
        f.write(content)

def main():
    """
    Main function to update indexes for folders and the root.

    This function iterates through a list of folders, updating the index for each one
    by calling the `updateIndex` function. After processing all folders, it updates
    the root index by calling the `updateRootIndex` function.

    Note:
        The `folders` variable and the `updateIndex` and `updateRootIndex` functions
        are assumed to be defined elsewhere in the code.
    """
    for folder in folders:
        updateIndex(folder)
    updateRootIndex()

if __name__ == '__main__':
    main()

