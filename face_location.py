from PIL import Image, ImageDraw
import numpy as np
from face_recognition import *
import os


def load_image_file(file, mode='RGB'):
 
    im = Image.open(file)
    if mode:
        im = im.convert(mode)
    return np.array(im)



def face_location(img_path):
    img = load_image_file(img_path)
    location = face_locations(img)
    return location
    
def show_prediction_labels_on_image(img_path):
    
    pil_image = Image.open(img_path).convert("RGB")
    predictions = face_location(img_path)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left) in predictions:
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
    pil_image.show()

show_prediction_labels_on_image(os.path.join('group2.jpg'))




