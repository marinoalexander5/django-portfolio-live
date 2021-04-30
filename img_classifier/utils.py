from keras.preprocessing.image import load_img, img_to_array
from keras.applications.mobilenet import preprocess_input, decode_predictions
from .apps import ImgClassifierConfig as ImgClassifier

from io import BytesIO
import requests
import urllib
from PIL import Image

def classify_image(image_url):
    # get image from url
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('RGB')
    image = img.resize((224, 224), Image.NEAREST)

    # load image
    # image = load_img(f, target_size=(224, 224))
    # convert to numpy array
    image = img_to_array(image)
    # reshape
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare image for model
    image = preprocess_input(image)
    # predict across all 1,000 classes
    predictions = ImgClassifier.model.predict(image)
    # convert probabilities to class labels
    label = decode_predictions(predictions)
    # retrieve highest probability class
    label = label[0][0]

    return (label[1], label[2]*100)