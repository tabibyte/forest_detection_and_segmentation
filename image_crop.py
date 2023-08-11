from PIL import Image

def crop_and_save_image(image_path, output_folder):
    try:
        img = Image.open(image_path)
        width, height = img.size

        num_cols = width // 64
        num_rows = height // 64

        for y in range(num_rows):
            for x in range(num_cols):
                left = x * 64
                upper = y * 64
                right = left + 64
                lower = upper + 64

                tile = img.crop((left, upper, right, lower))
                tile_number = y * num_cols + x
                save_path = f"{output_folder}/tile_{tile_number}.png"
                tile.save(save_path)

        print(f"{num_cols * num_rows} tiles cropped and saved successfully.")
    except Exception as e:
        print(f"Error: {e}")


input_image_path = "mask binary.png"
output_folder_path = "dataset_mask_output"
crop_and_save_image(input_image_path, output_folder_path)