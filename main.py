from distutils.command.clean import clean
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    print(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    print(clean_name)

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')