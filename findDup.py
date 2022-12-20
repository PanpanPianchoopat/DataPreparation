# This program compares between originally cleaned images and new images data.
# If a duplicate of any clean images is found, that duplication in new image
# folder will be deleted. 

# Change both image folder paths before running this program.

import os
from PIL import Image, ImageStat
import cv2

# Folder of images (CHANGE BOTH PATHS BEFORE RUN)
# Path to cleaned images
base_folder = os.path.join(os.getcwd(), 'YOURDIR') 
# Path to new image data
raw_folder = os.path.join(os.getcwd(), 'YOURDIR')

# All images file name
old_files = [_ for _ in os.listdir(base_folder) if _.endswith('bmp')]
new_files = [_ for _ in os.listdir(raw_folder) if _.endswith('bmp')]

# Count of each type
same = 0                          # No. of image pair that are duplicated
del_count = 0                     # No. of duplicated image deleted
new_file_count = len(new_files)   # No. of new image file

print('Find duplicate files in progress...')
print('This process can take some time...')

# Go through the the files
for original_file in old_files:
  # Find mean of original image
  original_img = Image.open(os.path.join(base_folder, original_file))
  pix_mean = ImageStat.Stat(original_img).mean

  # Go through the files again
  for file_chk in new_files:
    # Find mean of that file
    chk_img = Image.open(os.path.join(raw_folder, file_chk))
    pix_mean2 = ImageStat.Stat(chk_img).mean
    if pix_mean == pix_mean2:
      # If mean is the same compare image shape
      ori = cv2.imread(os.path.join(base_folder, original_file))
      dup = cv2.imread(os.path.join(raw_folder, file_chk))
      if ori.shape == dup.shape:
        # If shape is the same find difference in each pixel
        difference = cv2.subtract(ori, dup)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
          same += 1 
          # cv2.imshow("Original", ori)
          # cv2.imshow("Duplicate", dup)
          print(original_file, 'and', file_chk, 'are the same')
          # Delete duplicated image
          del_path = os.path.join(raw_folder, file_chk)
          if os.path.isfile(del_path):
            os.remove(del_path)
            print('\tRemoved', file_chk)
            new_files.remove(file_chk)
            del_count += 1

print('Summary:')
print('\tFound', same, 'duplicated files out of', new_file_count, 'images')
print('\tDelete', del_count, 'duplicated files')
