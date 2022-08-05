from PIL import Image
import os
from os import listdir
from os.path import splitext
from tqdm import tqdm
import datetime

target_directory = 'path'
target = '.png'
date = str(datetime.datetime.now())
date = date.replace(":", "-")
with open('errors in ' + str(date) + '.txt', 'a') as f:
    f.write('errors:')
    f.write("\n")
    data = []
    for file in tqdm(listdir(target_directory)):
        filename, extension = splitext(file)
        try:
            if extension not in ['.png', '.gif', '.mp4', '.webm',  target]:
                im = Image.open(target_directory + "/" + filename + extension)
                im.save(target_directory + "/" + filename + target)
                os.remove(target_directory + "/" + filename + extension)
        except OSError:
            f.write(str('Could not convert %s' % file))
            f.write("\n")
