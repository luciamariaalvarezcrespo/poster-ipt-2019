#Poster IPT_ACM_2019
#Autoras: Icia Carro Barallobre && Lucia Alvarez Crespo

############ Librerias #######
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import tensorflow as tf


longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
cnn = tf.keras.models.load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  return answer




