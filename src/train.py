#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

class Train:

    TRAIN_DATA = './data/train'
    VALIDATION_DATA = './data/validation'

    EPOCHS = 5
    WIDTH = 150
    HEIGHT = 150
    BATCH_SIZE = 32
    STEPS = 500
    VALIDATION_STEPS = 300
    FILTERS_FIRST_CONV = 32
    FILTERS_SECOND_CONV = 64
    SIZE_FIRST_FILTER = (3, 3)
    SIZE_SECOND_FILTER = (2, 2)
    POOL_SIZE = (2, 2)
    CLASSES = 2
    LR = 0.0004
  
    @classmethod
    def preprocess_images(self):

        self.training_datagen = ImageDataGenerator(
            rescale = 1./255,
            shear_range = 0.2,
            zoom_range = 0.2,
            horizontal_flip = True)

        self.test_datagen = ImageDataGenerator(rescale = 1./255)

        self.training_generator = self.training_datagen.flow_from_directory(
            os.path.join(sys.path[0],Train.TRAIN_DATA),
            target_size = (Train.HEIGHT, Train.WIDTH),
            batch_size = Train.BATCH_SIZE,
            class_mode = 'categorical')

        self.validation_generator = self.test_datagen.flow_from_directory(
            os.path.join(sys.path[0],Train.VALIDATION_DATA),
            target_size = (Train.HEIGHT, Train.WIDTH),
            batch_size = Train.BATCH_SIZE,
            class_mode = 'categorical')
        
        return (self.training_generator, self.validation_generator)

    @classmethod
    def train_cnn(self):

        (self.training_generator, self.validation_generator) = Train.preprocess_images()

        K.clear_session()

        self.cnn = Sequential()
        self.cnn.add(Convolution2D(Train.FILTERS_FIRST_CONV, Train.SIZE_FIRST_FILTER, padding = "same", input_shape = (Train.HEIGHT, Train.WIDTH, 3), activation = 'relu'))
        self.cnn.add(MaxPooling2D(pool_size = Train.POOL_SIZE))

        self.cnn.add(Convolution2D(Train.FILTERS_SECOND_CONV, Train.SIZE_SECOND_FILTER, padding = "same"))
        self.cnn.add(MaxPooling2D(pool_size = Train.POOL_SIZE))

        self.cnn.add(Flatten())
        self.cnn.add(Dense(256, activation = 'relu'))
        self.cnn.add(Dropout(0.5))
        self.cnn.add(Dense(Train.CLASSES, activation = 'softmax'))

        self.cnn.compile(loss = 'categorical_crossentropy',
            optimizer = optimizers.Adam(lr = Train.LR),
            metrics = ['accuracy'])

        self.cnn.fit_generator(
            self.training_generator,
            steps_per_epoch = Train.STEPS,
            epochs = Train.EPOCHS,
            validation_data = self.validation_generator,
            validation_steps = Train.VALIDATION_STEPS)
        
        return self.cnn

    @classmethod
    def create_model(self):

        self.cnn = Train.train_cnn()        

        target_dir = './model/'
        
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        
        self.cnn.save('./model/model.h5')
        self.cnn.save_weights('./model/weights.h5')
