import nltk
import json
import pickle
import numpy as np
import random

ignore_words = ['?','!',',','.',"'s","'m"]

import tensorflow
from data_preprocessing import get_stem_words

model = tensorflow.keras.models.load_model('./chat_bot')