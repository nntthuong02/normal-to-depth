import pandas as pd
import numpy as np

from glob import glob

import cv2
import matplotlib.pylab as plt

scholar_file = glob('image/scholar.png')

img_mpl = plt.imread(scholar_file)