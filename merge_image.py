
import os
from PIL import Image


image = 'logo_transparent.png'
logo_m = Image.open(image, 'r')
background = 'background.png'
bg = Image.open(background, 'r')
text_img = Image.new('RGBA', (1080,720), "white")
text_img.paste(bg, (0,0))
text_img.paste(logo_m, (480,0),mask=logo_m)

text_img.save("result_1.png", format="png")