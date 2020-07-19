import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train,y_train), (x_test,y_test)=mnist.load_data()

#normalize our data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Flatten())
#model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
#model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
#model.add(tf.keras.layers.Dense(10,activation='softmax'))

#model.compile(optimizer ='adam',loss ='sparse_categorical_crossentropy',metrics = ['accuracy'])

#model.fit(x_train, y_train, epochs=3)

#val_loss, val_acc = model.evaluate(x_test, y_test)
#print(val_loss, val_acc)

#model.save('epic_num_reader.model')

new_model = tf.keras.models.load_model('epic_num_reader.model')

predictions = new_model.predict(np.array(x_test))

print(np.argmax(predictions[14]))

plt.imshow(x_test[14])
plt.show(block=True)