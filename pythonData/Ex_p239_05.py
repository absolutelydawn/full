#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

glt.rcParams['font.family'] = ['NanumBarunGothic']

filename = 'ex802.py
myframe = pd.read_csv(filename, index_col=type, encoding='utf-8')
myframe.plot(title='지역별 차종 공통점', kind='line', )