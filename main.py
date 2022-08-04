from PIL import Image
import os
from os import listdir
from os.path import splitext
from tqdm import tqdm

target_directory = 'path'
target = '.png'

for file in tqdm(listdir(target_directory)):
    filename, extension = splitext(file)
    try:
        if extension not in ['.png', '.gif', '.mp4', '.webm',  target]:
            im = Image.open(target_directory + "/" + filename + extension)
            im.save(target_directory + "/" + filename + target)
            os.remove(target_directory + "/" + filename + extension)
    except OSError:
        print('Could not convert %s' % file)
