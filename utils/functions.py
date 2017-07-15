from IPython.display import Image
from pprint import pprint as pp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

%matplotlib inline
matplotlib.style.use('ggplot')

slidedir = "slides/slides-dir"

# Display slide
def ds(number):
    display(Image('{}/slide{:03d}.jpg'.format(slidedir, number)))  

# Image to Base64
import base64
import cStringIO
from PIL import Image as PImage

def load_img(path):
    return PImage.open(path)

def img_to_thumbnail(img):
    img.thumbnail((512,512))

def imgfile_to_base64(path):
    image = load_img(path)
    return img_to_base64(image)

def img_to_base64(image):
    buffer = cStringIO.StringIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue())

def img_from_base64(b64string):
    image_string = cStringIO.StringIO(base64.b64decode(b64string))
    return PImage.open(image_string)

from PIL import ImageFont
from PIL import ImageDraw
import math

font = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 150)
fontEmoji = ImageFont.truetype("fonts/OpenSansEmoji.ttf", 150)

def sayEmoji(string):
    return say_(string, fontEmoji)

def say(string):
    return say_(string, font)

def say_(string, font):
    if len(string) == 0:
        return False
    
    scale = 1.5
    fontsize = font.getsize(string) #The size of the image
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
