import os

downloads = '/Users/elangreen/Downloads/'
list = os.listdir(downloads)
dst = '/Users/elangreen/Pictures/'

for filename in list:
  if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
    os.rename(downloads  + filename, dst + filename)

