import os

def find_files(file_name, search_path="C:/"):
    found_file_paths = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file == file_name:
                found_file_paths.append(os.path.join(root, file))
    return found_file_paths


file_name_to_find = input("Enter the file name to find: ")
found_file_paths = find_files(file_name_to_find)

if found_file_paths:
    print("File(s) found:")
    for file_path in found_file_paths:
        file_path = file_path.replace("\\", "/")
        print(file_path)
else:
    print("No file(s) found.")

mapped_data = [
    (path.split(os.sep), len(path.split(os.sep))) for path in found_file_paths
]

longest_path = max(mapped_data, key=lambda x: x[1])

print("Longest path(s):", "/".join(longest_path[0]))