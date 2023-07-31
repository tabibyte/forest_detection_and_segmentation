from PIL import Image
import os
import shutil

def find_color_in_image(image_path, color_to_find):
    image = Image.open(image_path)
    pixel_data = image.convert("RGB").load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel_color = pixel_data[x, y]
            if pixel_color == color_to_find:
                return True
            break

    return False

def move_images_by_color(search_folder, source_folder, destination_no_color, destination_with_color, color_to_find):
    if not os.path.exists(destination_no_color):
        os.makedirs(destination_no_color)
    if not os.path.exists(destination_with_color):
        os.makedirs(destination_with_color)

    for filename in os.listdir(search_folder):
        src_path = os.path.join(search_folder, filename)
        if not os.path.isfile(src_path):
            continue

        if find_color_in_image(src_path, color_to_find):
            dest_folder = destination_with_color
        else:
            dest_folder = destination_no_color

        dest_path = os.path.join(dest_folder, filename)

        if os.path.exists(os.path.join(source_folder, filename)):
            shutil.move(os.path.join(source_folder, filename), dest_path)
            print(f"Moved '{filename}' to '{dest_path}'")


source_folder = "dataset_output"
search_folder = "dataset_mask_output"
destination_no_color = "non_forest"
destination_with_color = "forest"
color_to_find = (255, 0, 42)

move_images_by_color(search_folder, source_folder, destination_no_color, destination_with_color, color_to_find)