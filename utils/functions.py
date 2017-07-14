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
