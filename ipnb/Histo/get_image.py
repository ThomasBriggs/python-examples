from matplotlib import image
from matplotlib import pyplot
import numpy as np
import pandas as pd

image = image.imread("256a8179_iss042e283178.jpg")
pyplot.imshow(image)
pyplot.show()

print(image.shape)