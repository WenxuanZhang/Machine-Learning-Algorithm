'''
Author: Wenxuan Zhang
Date: 05/10/2015
All rights reserved.

About: This file takes an resume in .docx as an input and generate
a bargraph that shows the frequency of each character in descending
order

Prerequisites:
In order to run this script successfully, you should have an plotly 
account and related API key and Username.

'''
from docx import Document
from operator import itemgetter
from collections import Counter
import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import numpy as np

#Open file and read data.
document = Document('Wenxuan Zhang Resume.docx')
#Filter out non alphabet and non digital character.
docText = '\n\n'.join([
    paragraph.text.encode('utf-8') for paragraph in document.paragraphs
])
text=''.join(e for e in docText if e.isalnum())
text=text.upper()
#count frequency
c = Counter(text)
data = sorted(c.items(),key=itemgetter(1),reverse=True)
character, frequency= map(list, zip(*data))

#barplot is a function thaty takes data x, y, and title of graph as inputs
#and generate an interactive plotly bar plot.
def barplot(x,y,title):
    data = Data([
        Bar(
            x=x,
            y=y,
            marker=Marker(
                color='rgb(253,174,107)'
            )
        )
    ])
    layout = Layout(
        title=title,
        font=Font(
            family='Raleway, sans-serif'
        ),
        showlegend=False,
        xaxis=XAxis(
            tickangle=-45
        ),
        yaxis=YAxis(
            zeroline=False,
            gridwidth=2
        ),
        bargap=0.05
    )
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename=title)

#final step, generate barplot   
barplot(character, frequency,'Character Frequency of Resume')