'''
Author: Wenxuan Zhang
Date: 05/10/2015
All rights reserved.

About: This file takes an resume in .docx as an input and generate
a bargraph that shows the frequency of each word in descending
order

Prerequisites:
In order to run this script successfully, you should have an plotly 
account and related API key and Username.

Besides, because this script import function from character_frequency.py,
make sure chracter_frequency.py are in your working library.
'''

from docx import Document
from operator import itemgetter
from collections import Counter
import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import numpy as np
from character_frequency import barplot

document = Document('Wenxuan Zhang Resume.docx')
docText = '\n\n'.join([
    paragraph.text.encode('utf-8') for paragraph in document.paragraphs
])
text=''.join(e for e in docText if e.isalnum() or e==' ')
text=text.lower()
text=text.split()
c = Counter(text)
data = sorted(c.items(),key=itemgetter(1),reverse=True)
word, frequency= map(list, zip(*data))

barplot(word, frequency,'Word Frequency of Resume')
