from IPython.display import Image
from pprint import pprint as pp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

%matplotlib inline
matplotlib.style.use('ggplot')

slidedir = "slides/slides-dir"

# Display slides
def ds(number, nslides=1):
    for i in range(nslides):
        display(Image('{}/slide{:03d}.png'.format(slidedir, number+i)))  
    
# Image to Base64
import base64
import cStringIO
from PIL import Image as PImage

def load_img(path):
    return PImage.open(path)

def img_to_thumbnail(img):
    img.thumbnail((512,512),PImage.ANTIALIAS)

def imgfile_to_base64(path):
    image = load_img(path)
    return img_to_base64(image)

def img_to_base64(image):
    buffer = cStringIO.StringIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue())

def img_from_base64(b64string):
    image_string = cStringIO.StringIO(base64.b64decode(b64string))
    return PImage.open(image_string)

from PIL import ImageFont
from PIL import ImageDraw
import math

font = ImageFont.truetype("fonts/OpenSans-ExtraBold.ttf", 150)
#fontEmoji = ImageFont.truetype("fonts/OpenSansEmoji.ttf", 150)
font_small = ImageFont.truetype("fonts/OpenSans-ExtraBold.ttf", 50)


#def sayEmoji(string):
#    return say_(string, fontEmoji)

def say(string):
    return say_(string, font)

yodaimg = PImage.open('images/yoda.jpg')
scale=1.5

def yoda(string):
    fontsize = font_small.getsize(string)
    yodacp = yodaimg.copy()
    ys = yodacp.size
    imgsize = [int(fontsize[0]*scale), int(fontsize[0] * scale * ys[1] / ys[0])]
    yodacp = yodacp.resize(imgsize)
    draw = ImageDraw.Draw(yodacp)
    draw.text((int(fontsize[0] * (1 - scale/2)),
               int(yodacp.size[1] - fontsize[1]*scale)),
              string,
              (255,255,255,1), 
              font=font_small)
    return yodacp
    
def say_(string, font):
    if len(string) == 0:
        return False
    
    fontsize = font.getsize(string) #The size of the font
    imgsize = [int(fontsize[0] * scale), int(fontsize[1] * scale)]

    image = PImage.new('RGB', imgsize) #Create the image

    innerColor = [80, 80, 255] #Color at the center
    outerColor = [0, 0, 80] #Color at the corners

    for y in range(imgsize[1]):
        for x in range(imgsize[0]):

            #Find the distance to the center
            distanceToCenter = math.sqrt((x) ** 2 + (y ) ** 2)

            #Make it on a scale from 0 to 1
            distanceToCenter = float(distanceToCenter) / (1.4142 * imgsize[0])

            #Calculate r, g, and b values
            r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
            g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
            b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)


            #Place the pixel        
            image.putpixel((x, y), (int(r), int(g), int(b)))

    draw = ImageDraw.Draw(image)
    draw.text((int((imgsize[0] - fontsize[0]) / 2),int((imgsize[1] - fontsize[1]) / 2)), 
              string, (255,255,255,1), font=font)

    return image
