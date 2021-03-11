import string
from collections import Counter
import requests
import os 
from PIL import Image
from IPython.display import IFrame
import pandas as pd
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize
from random import randint as rnd
from ibm_watson import LanguageTranslatorV3
import numpy as np



class Points(object):

    def __init__(self,x,y):

        self.x=x

        self.y=y

    
    def print_point(self):

        print('x=',self.x,' y=',self.y)


p2=Points(1,2)

p2.x=2

p2.print_point()





