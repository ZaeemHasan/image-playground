import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ folder exists. If not create it!
is_image_folder = os.path.isdir(image_folder)
is_output_folder = os.path.isdir(output_folder)

if is_image_folder == False:
    raise OSError('Pokedex folder does not exists')

if is_output_folder == False:
    os.mkdir(output_folder)

# loop through Pokedex and convert images to PNG
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        # convert images to png and save it to the new folder
        img.save(f'{output_folder}{clean_name}.png', 'png')
        print(f'{filename} converted to {clean_name}.png')
        # print(clean_name)
    else:
        continue

