import os

def remove_part_from_filename(folder_path, part_to_remove):
    for filename in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path, filename)

        if os.path.isfile(old_file_path):
            new_filename = filename.replace(part_to_remove, '')
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file if the new name is different from the old one
            if new_filename != filename:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'.")

folder_path = 'dataset_mask_output'
part_to_remove = 'tile_'

remove_part_from_filename(folder_path, part_to_remove)