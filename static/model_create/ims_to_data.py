from keras.preprocessing.image import img_to_array
import cv2
import os
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from tqdm import tqdm

np_arrays = []
labels = []

for i in tqdm(range(0,10)):
    for filename in os.scandir(f'Text/Sample{i}'):

        if filename.is_file():
            img = cv2.imread(filename.path)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            img_shape = [28,28]

            gray = cv2.resize(gray, tuple(img_shape))

            img_numpy_array = img_to_array(gray)

            np_arrays.append(img_numpy_array)
            labels.append(i)


np_arrays, labels = shuffle(np.array(np_arrays), np.array(labels))

with open('text_x_data.npy', 'wb') as f:
    np.save(f, np_arrays)

with open('text_y_data.npy', 'wb') as f:
    np.save(f, labels)

# idx = 0
# print(labels[idx])
# plt.imshow(np_arrays[idx],cmap='gray')
# plt.show()

            

            