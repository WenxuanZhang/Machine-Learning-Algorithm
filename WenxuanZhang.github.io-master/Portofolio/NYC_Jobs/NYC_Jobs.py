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
import datetime
from chracter_frequency import barplot
import re
import inflect

#read in data
jobs=pd.read_csv('NYC_Jobs.csv',index_col=None)
# aggregate by Agency
Post_Agency=jobs.groupby('Agency')['# Of Positions'].apply(sum)
Post_Agency.sort(ascending=False)
Agency, Number =list(Post_Agency.index),list(Post_Agency)
#plot it
barplot(Agency, Number,'#of Position by Agency')

#Caculate the annual salary of those position provide hourly or daily wage
Daily=jobs['Salary Frequency']=='Daily'
jobs['Salary Range From'][Daily]= jobs['Salary Range From'][Daily]*251
jobs['Salary Range To'][Daily]= jobs['Salary Range To'][Daily]*251
Hourly=jobs['Salary Frequency']=='Hourly'
jobs['Salary Range From'][Hourly]= jobs['Salary Range From'][Hourly]*2008
jobs['Salary Range To'][Hourly]= jobs['Salary Range To'][Hourly]*2008

# Boxplot the salary lower bound by department
data =[]
for A in Agency:
    y=jobs['Salary Range From'][jobs['Agency']==A]
    trace=Box(y=y,name=A)
    data=data+[trace]

salary = Data(data)
layout = Layout(
        title='Salary Lower Bound by Department',
        font=Font(
            family='Raleway, sans-serif'
        ),
    showlegend=False
)
fig = Figure(data=salary, layout=layout)
plot_url = py.plot(fig, filename='Salary Lower Bound')

#Extract the jobs with the lowest salary.
Lowest = jobs.loc[jobs['Salary Range From']==min(jobs['Salary Range From'])]
Lowest.groupby('Agency')['# Of Positions'].apply(sum)
#Extract the jobs with the highest salary.
Highest = jobs.loc[jobs['Salary Range To']==max(jobs['Salary Range To'])]
Highest.groupby('Agency')['# Of Positions'].apply(sum)

# Boxplot the salary lower bound by department
data = []
for A in Agency:
    y=jobs['Salary Range To'][jobs['Agency']==A]
    trace=Box(y=y,name=A)
    data=data+[trace]

salary = Data(data)
layout = Layout(
    title='Salary Upper Bound by Department',
        font=Font(
            family='Raleway, sans-serif'
        ),
    showlegend=False
)
fig = Figure(data=salary, layout=layout)
plot_url = py.plot(fig, filename='Salary Uppper Bound')

#Generate a new field Lag, which is the days since it posted.
#bar plot it.
jobs=pd.read_csv('NYC_Jobs.csv',index_col=None)
jobs['Posting Date'] = [datetime.strptime( i,'%m/%d/%y %H:%M') for i in jobs['Posting Date']]
jobs['Lag'] = datetime.now()-jobs['Posting Date']
jobs['Lag'] = [int(round(i/np.timedelta64(1,'D')))for i in jobs['Lag']]
postdays = pd.value_counts(jobs['Lag'])
days,count=list(postdays.index),list(postdays)
barplot(days, count,'Number of Post days')

#Calculated mean of Lag of each department, barplot it.
jobs.groupby('Agency')['Lag'].apply(np.mean)
post_dept.sort(ascending=False)
Dept,days = list(post_dept.index),list(post_dept)
barplot(Dept,days,'Mean of Posted Days by Department')

#Average Salary
jobs['Salary']=(jobs['Salary Range From']+jobs['Salary Range To'])/2
p = inflect.engine()
word_to_number_mapping = {}
for i in range(1, 50):
    word_form = p.number_to_words(i)  
    word_to_number_mapping[word_form] = i

# Define a function that take minimum requirement as an input and return
# the year of experience required by this postion.
def experience(requirements):
    if type(requirements)!=float:
        text=''.join(e for e in requirements if e.isalnum() or e==' ')
        pattern = r'(\s{1}\w*\s{1})(?=years* of (\w*\s{1})*experience)'
        result = re.findall(pattern,text)
        number = [r[0].strip() for r in result]
        num=[]
        for i in range(len(number)):
            if number[i].isdigit():
                num.append(int(number[i]))
            if number[i] in word_to_number_mapping:
                num.append(word_to_number_mapping[number[i]])
        if len(num)>0:
            return max(num)
        else:
            return float('nan')
    else:
        return float('nan')
#Generate experience need for each job.
exp = []
for i in range(len(jobs['Minimum Qual Requirements'])):
    require = jobs['Minimum Qual Requirements'][i]
    exp = exp + [experience(require)]

#Deal with the encode issue.
jobs['Business Title'] = [unicode(j, errors='ignore').encode('utf-8') for j in jobs['Business Title']]

#Plot Exp vs Salary
trace1 = Scatter(
    x=jobs['exp'],
    y=jobs['Salary'],
    mode='markers',
    text=jobs['Business Title'],
    marker=Marker(
        color='rgb(253,174,107)',
        size=12,
        line=Line(
            color='white',
            width=0.5
        )
    )
)


data = Data([trace1])
layout = Layout(
    title='',
    xaxis=XAxis(
        title='Year of Experience',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Salary',
        showline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Experience vs Salary')



