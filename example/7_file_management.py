"""
Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png 
where n is the number of png files in that folder. Do the same for other file formats
"""

import os
import random
import uuid
from PIL import Image

print("This program will rename all png files in the current directory to 1.png, 2.png, ..., n.png")

# Get current directory
current_dir = os.getcwd()  
images_folder = os.path.join(current_dir, "clutter")
os.makedirs(images_folder, exist_ok=True)

# Save a new image

# for _ in range(5):  # generate 5 images
#     # Random size between 100x100 and 800x800
#     width = random.randint(100, 800)
#     height = random.randint(100, 800)
    
#     # Random color (R, G, B)
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
#     # Create image
#     img = Image.new("RGB", (width, height), color=color)
    
#     # Random unique filename
#     filename = f"{uuid.uuid4().hex}.png"
    
#     # Save image
#     img.save(os.path.join(images_folder, filename))
#     print(f"Saved {filename} with size {width}x{height} and color {color}")

all_images = os.listdir(images_folder)
for index, filename in enumerate(all_images, start=1):
  ext = os.path.splitext(filename)[1]
  new_name = f"image-{index}{ext}"
  old_path = os.path.join(images_folder,filename)
  new_path = os.path.join(images_folder,new_name)
  os.rename(old_path,new_path)
  print(f"Renamed {filename} → {new_name}")

  