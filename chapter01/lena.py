import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("../../../oreilly-japan/deep-learning-from-scratch/dataset/lena.png")
plt.imshow(img)

plt.show()
