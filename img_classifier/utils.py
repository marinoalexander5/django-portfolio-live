from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions
from .apps import ImgClassifierConfig as ImgClassifier

def classify_image(image_url):
    # load image
    image = load_img(image_url, target_size=(224, 224))
    # convert to numpy array
    image = img_to_array(image)
    # reshape
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare image for model
    image = preprocess_input(image)
    # predict across all 1,000 classes
    yhat = ImgClassifier.model.predict(image)
    # convert probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve highest probability class
    label = label[0][0]
    return label[1]