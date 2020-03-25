from skimage import resize
import numpy as np

def preprocess(obs):
    return resize(img, (105, 80), mode='reflect').mean(2)[22:102,:]

