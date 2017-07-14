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

font = ImageFont.truetype("MelmaCracked.ttf", 25)


def say(string):
    imgsize = (250, 250) #The size of the image

    image = PImage.new('RGB', imgsize) #Create the image

    innerColor = [80, 80, 255] #Color at the center
    outerColor = [0, 0, 80] #Color at the corners

    for y in range(imgsize[1]):
        for x in range(imgsize[0]):

            #Find the distance to the center
            distanceToCenter = math.sqrt((x - imgsize[0]/2) ** 2 + (y - imgsize[1]/2) ** 2)

            #Make it on a scale from 0 to 1
            distanceToCenter = float(distanceToCenter) / (math.sqrt(2) * imgsize[0]/2)

            #Calculate r, g, and b values
            r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
            g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
            b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)


            #Place the pixel        
            image.putpixel((x, y), (int(r), int(g), int(b)))

    img = PImage.new("RGBA", (500,400), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.text((0,0), "This is a test", (255,255,255,1), font=font)
    draw = ImageDraw.Draw(img)
    image.save('circlegradient.jpg')

