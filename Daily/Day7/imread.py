from skimage.io import imread
from skimage.filters import sobel
import matplotlib.pyplot as plt

buck = imread("buckaroo_crop.jpeg")
print(buck.shape)

plt.imshow(buck)
plt.show()
