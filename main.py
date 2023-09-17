from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import date
import os
from matplotlib import font_manager

path = ''
file_list = os.listdir()

font = font_manager.FontProperties(family='Roboto Slab', weight='regular')
font_file = font_manager.findfont(font)

for file_name in file_list:
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        img = Image.open(path + file_name)
         
        I1 = ImageDraw.Draw(img)

        text_font = ImageFont.truetype(font_file, 24)

        I1.text((img.size[0]-146,
                 img.size[1]-48),
                date.today().strftime('%d/%m/%Y'),
                font=text_font,
                fill =(255, 210, 30),
                stroke_width=1,
                stroke_fill=(66, 64, 60))

        img.save(path + file_name)
