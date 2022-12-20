import os
from PIL import Image

sourcePath = '../cleanTeeth/clean/'      # bmp images path
savePath = '../cleanTeeth/raw_jpg/'    # jpg images path

for filename in os.listdir(sourcePath):
  if not filename.startswith('.'):
    oldImagePath = os.path.join(sourcePath, filename)
    img = Image.open(oldImagePath)
    newFilenName = filename.replace('.bmp', '.jpg')
    # print(newFilenName)
    img.save(savePath + newFilenName, 'JPEG')




