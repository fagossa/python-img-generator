import numpy as np
from numpy.random import randint, choice
import os
import string
from PIL import Image, ImageFont, ImageDraw

TF = ImageFont.truetype('consola.ttf', 18)

def MakeImg(t, f, fn, s = (100, 100), o = (0, 0)):
    '''
    Generate an image of text
    t:      The text to display in the image
    f:      The font to use
    fn:     The file name
    s:      The image size
    o:      The offest of the text in the image
    '''
    img = Image.new('RGB', s, "black")
    draw = ImageDraw.Draw(img)
    draw.text(o, t, (255, 255, 255), font = f)
    img.save(fn)

def GetFontSize(S):
    img = Image.new('RGB', (1, 1), "black")
    draw = ImageDraw.Draw(img)
    return draw.textsize(S, font = TF)

def GenMultiLine(posible_chars, ML, MINC, MAXC, NIMG, output_folder):
    CS = posible_chars
    MS = GetFontSize('\n'.join(ML * ['0' * MAXC]))
    Y = []
    for i in range(NIMG):
        # Random phrase
        Si = ' '.join(''.join(choice(CS, randint(MINC, MAXC))) for _ in range(randint(1, ML + 1)))
        (w, h) = MS
        # file name
        FNi = str(i) + '.png'
        img_path = os.path.join(output_folder, FNi)
        MakeImg(Si, TF, img_path, (w, 32), (5, 8))
        Y.append((FNi, Si.replace('\n', '@')))
    return Y

def write_report_file_from(content):
    with open("report.csv", 'w') as file_handler:
        for img_file, content in content:
            file_handler.write("{0} {1}\n".format(img_file, content.replace(" ", "|")))

if __name__ == "__main__":
    posible_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                     'y', 'z']
    generated_content = GenMultiLine(
        posible_chars = posible_chars,
        ML   = 5, # min word length
        MINC = 5,
        MAXC = 30, #max phrase length
        NIMG = 50, # number of images
        output_folder = 'Img')
    write_report_file_from(generated_content)
