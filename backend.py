import numpy as np
import tensorflow as tf


CLASS_NAME = ['Potato___healthy', 'Tomato___healthy', 'Corn___Common_rust',
              'Apple___Apple_scab', 'Soybean___healthy',
              'Tomato___Tomato_mosaic_virus', 'Tomato___Septoria_leaf_spot',
              'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Late_blight',
              'Grape___healthy', 'Cherry___Powdery_mildew', 'Apple___healthy',
              'Pepper,_bell___Bacterial_spot', 'Potato___Late_blight',
              'Corn___Northern_Leaf_Blight', 'Corn___healthy',
              'Orange___Haunglongbing_(Citrus_greening)', 'Apple___Black_rot',
              'Tomato___Target_Spot', 'Potato___Early_blight', 'Squash___Powdery_mildew',
              'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Raspberry___healthy',
              'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Peach___healthy',
              'Tomato___Early_blight', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
              'Strawberry___healthy', 'Blueberry___healthy', 'Peach___Bacterial_spot',
              'Pepper,_bell___healthy', 'Grape___Black_rot', 'Cherry___healthy',
              'Tomato___Bacterial_spot', 'Background_without_leaves', 'Strawberry___Leaf_scorch',
              'Grape___Esca_(Black_Measles)', 'Tomato___Leaf_Mold', 'Apple___Cedar_apple_rust']


class Backend:
    def __init__(self):
        self._image_shape = (224, 224)
        self._model_path = './model_effb0'
        self._model = None

        self._load_model()

    def _load_model(self):
        self._model = tf.keras.models.load_model(self._model_path)

    def predict_image(self, path):
        img = self._prepare_image(path)
        prob = self._model.predict(np.asarray([img]))[0]
        c_idx = np.argmax(prob)
        prob_f = round(prob[c_idx] * 100, 2)
        return f"Image category: {CLASS_NAME[c_idx]} | Probability: {prob_f}%"

    def _prepare_image(self, path):
        img = tf.io.read_file(path)
        img = tf.io.decode_image(img, channels=3)
        img = tf.image.resize(img, size=[self._image_shape[0], self._image_shape[1]])
        img = img/225.
        return img
