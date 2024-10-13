import os
import shutil


def copy_matching_files(search_folder, second_folder, destination_folder, num_files):
    # Get a list of all files in the search folder
    search_files = os.listdir(search_folder)
    second_files = os.listdir(second_folder)

    # Dictionary to store files from the search folder
    search_files_dict = {}
    second_files_dict = {}

    # Populate dictionaries with files
    for file_name in search_files:
        full_path = os.path.join(search_folder, file_name)
        if os.path.isfile(full_path):
            base_name = os.path.basename(file_name)
            if base_name not in search_files_dict:
                search_files_dict[base_name] = []
            search_files_dict[base_name].append(full_path)

    for file_name in second_files:
        full_path = os.path.join(second_folder, file_name)
        if os.path.isfile(full_path):
            base_name = os.path.basename(file_name)
            if base_name not in second_files_dict:
                second_files_dict[base_name] = []
            second_files_dict[base_name].append(full_path)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy matching files to the destination folders
    copied_count = 0
    for base_name in search_files_dict.keys():
        if base_name in second_files_dict and copied_count < num_files:
            for search_file_path in search_files_dict[base_name]:
                destination_search_path = os.path.join(destination_folder, 'search', os.path.basename(search_file_path))
                shutil.copy(search_file_path, destination_search_path)
                copied_count += 1

                if copied_count >= num_files:
                    break

            for second_file_path in second_files_dict[base_name]:
                destination_second_path = os.path.join(destination_folder, 'second', os.path.basename(second_file_path))
                shutil.copy(second_file_path, destination_second_path)

                if copied_count >= num_files:
                    break


search_folder = "data_classified/Trees"
second_folder = "dataset_mask_output"
destination_folder = "dataset_u-net"
num_files = 157

copy_matching_files(search_folder, second_folder, destination_folder, num_files)
