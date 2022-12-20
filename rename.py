# This program rename files to the format of 5 digits ID and move them to the
# specified directory.

# Please change file paths to yours and make sure that the ID is the latest one.


import os


# CHANGE THESE 3 BEFORE RUN
# Starting ID (change this to the latest one)
id = 999  
# Images to be renamed path (change this to yours)
path = 'YOURDIR'   
# Path to folder for renamed files
path_for_renamed_files = 'YOURDIR'  
  

# If the renamed images folder does not exist, create one.
chk_folder = os.path.isdir(path_for_renamed_files)
if not chk_folder:
  os.makedirs(path_for_renamed_files) 

for filename in os.listdir(path):     
  if not filename.startswith('.'):
    oldPath = os.path.join(path, filename)    # Image path
    if os.path.isfile(oldPath):
      newName = "{:05d}".format(id) + '.bmp'  # form new ID
      # Path to file with new name
      newPath = os.path.join(path_for_renamed_files, newName)   
      os.rename(oldPath, newPath)  
      id += 1

print('New lastest ID is', id)




