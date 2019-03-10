#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

class Predict:

    WIDTH = 150
    HEIGHT = 150
    MODEL = './model/model.h5'
    WEIGHTS = './model/weights.h5'

    @classmethod
    def predict(self, file):

      self.cnn = tf.keras.models.load_model(Predict.MODEL)
      self.cnn.load_weights(Predict.WEIGHTS)

      tmp = load_img(file, target_size = (Predict.WIDTH, Predict.HEIGHT))
      tmp = img_to_array(tmp)
      tmp = np.expand_dims(tmp, axis = 0)

      array = self.cnn.predict(tmp)
      result = array[0]
      answer = np.argmax(result)

      return answer




