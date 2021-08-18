import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

dataset = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/dataset_labbelled"
dataset_mascherine = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/dataset_mascherine_labbelled"

altezza = 28
larghezza = 28
batch_size = 2

model = keras.Sequential([layers.Input((28,28,1)), layers.Conv2D(16,3,padding="same"), layers.Conv2D(32,3,padding="same"), layers.MaxPooling2D(), layers.Flatten(), layers.Dense(10)])

trainData = tf.keras.preprocessing.image_dataset_from_directory(dataset, labels="inferred", label_mode="int", color_mode="grayscale", batch_size=batch_size, image_size=(altezza,larghezza), shuffle=True, seed=123, validation_split=0.1, subset="training")
#validationData = tf.keras.preprocessing.image_dataset_from_directory(dataset, labels="inferred", label_mode="int", color_mode="grayscale", batch_size=batch_size, image_size=(altezza,larghezza), shuffle=True, seed=123, validation_split=0.1, subset="validation")
testData = tf.keras.preprocessing.image_dataset_from_directory(dataset_mascherine, labels="inferred", label_mode="int", color_mode="grayscale", batch_size=batch_size, image_size=(altezza,larghezza), shuffle=True, seed=123, validation_split=0.99, subset="validation")

model.compile(optimizer=keras.optimizers.Adam(), loss=[keras.losses.SparseCategoricalCrossentropy(from_logits=True)], metrics=["accuracy"])
#history = model.fit(trainData, epochs=50, verbose=2)
history = model.fit(trainData, validation_data=testData, epochs=50,batch_size=1024,shuffle=True)
#print(history.history.keys())

def genera_grafico(history):
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.xlabel("epoche")
    plt.ylabel("accuratezza")
    plt.title("Grafico Accuratezza")
    plt.legend(["Train", "Test"], loc ="upper left")
    plt.show()

genera_grafico(history)

print()

image = tf.keras.preprocessing.image.load_img("/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/datasetConMascherine/001/S005_001_00000011.png", color_mode='grayscale', target_size=(altezza, larghezza), interpolation='nearest')
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.
predictions = np.argmax(model.predict(input_arr), axis=-1)
print(predictions)

