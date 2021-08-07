import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
from keras.datasets import mnist
import keras.utils
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D





dataset = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/dataset_labbelled"
emozioni_corrisponenti = ["neutrale", "rabbia", "disprezzo", "disgusto", "paura", "felicità", "tristezza", "sorpresa"]
emo_val = [0, 1, 2, 3, 4, 5, 6, 7]

for emozioni in emozioni_corrisponenti:
    path = os.path.join(dataset, emozioni)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        #print(img_array)

training_data = []

def create_training_data():
    for emozioni in emozioni_corrisponenti:
        path = os.path.join(dataset, emozioni)
        emo = emozioni_corrisponenti.index(emozioni)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                training_data.append([img_array, emo])
            except Exception as e:
                pass

create_training_data()

dataTrain = np.array(training_data)

#print("flattern", dataTrain[0].flatten())

#print("spero funzioni", dataTrain[0].shape)

tot_train_examples = 335
width=640
height=490
channels = 1
f_size1 = 32 #numero filtri primo strato del modello
f_size2= 16  #numero filtri secondo strato del modello

train_emo = tf.keras.utils.to_categorical(emo_val)
#print(train_emo[0])

model = Sequential()
model.add(Conv2D(f_size1, kernel_size=3, activation='relu', input_shape=(width,height,channels)))
model.add(Dropout(0.3))

model.add(Conv2D(f_size2, kernel_size=3, activation='relu'))
model.add(Dropout(0.3))

model.add(Flatten())

model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(dataTrain, train_emo, epochs=10, batch_size=1024, shuffle=True)











































#print(len(training_data))
# random.shuffle(training_data)
#
# for sample in training_data[:10]:
#     pass
#     #print(sample[1])
#
# X = []
# y = []
#
# for feature, label in training_data:
#     X.append(feature)
#     y.append(label)
#
#
# pickle_out = open("X.pickle", "wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()
#
# pickle_out = open("y.pickle", "wb")
# pickle.dump(y, pickle_out)
# pickle_out.close()
#
# X = pickle.load(open("x.pickle", "rb"))
# y = pickle.load(open("y.pickle", "rb"))
#
#
# model = Sequential()
#
# model.add(Conv2D(64, (3,3)))
# model.add(Activation("relu"))
# model.add(MaxPooling2D(pool_size=(2,2)))
#
# model.add(Flatten())
# model.add(Dense(64))
#
# model.add(Dense(1))
# model.add(Activation("sigmoid"))

# model.compile(loss="binary_crossentropy",
#               optimizer="adam",
#               metrics=["accuracy"])
#
# model.fit(X, y, batch_size=32, validation_split=0.1)



#dataset = tf.keras.preprocessing.image_dataset_from_directory("/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/dataset_labbelled", labels='inferred')
#print(dataset)

# (x_train, y_train), (x_test, y_test) = dataset.load_data()
# print("funzia")
# print((x_train, y_train), (x_test, y_test))

