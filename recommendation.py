from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import urllib.request
import requests
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='user'
app.config['MYSQL_PASSWORD']='user2001'
app.config['MYSQL_DB']='project'
mysql=MySQL(app)
app.secret_key = "super"
@app.route('/')
def index():
return render_template('recommend.html')
@app.route('/submit',methods =['GET', 'POST'])
def submit():
if request.method == 'POST':
course = request.form['course']
level=request.form.get("level")
msg=" "
try:
data.head()
similarity.shape
except:
data = pd.read_csv('courses.csv')
# creating a count matrix
cv = CountVectorizer()
count_matrix = cv.fit_transform(data['subject'])
# creating a similarity score matrix
similarity = cosine_similarity(count_matrix)
#return count_matrix,similarity
#data, similarity = create_similarity()
if course not in data['course_title'].unique():
a='Sorry! The Course you requested is not in our database. Please check the spelling or try 
with some other Courses'
return render_template('recommend.html',msg=a)
else:
i = data.loc[data['course_title']==course].index[0]
#print(i)
lst = list(enumerate(similarity[i]))
lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
rate=[]
#lst = lst[1:11] # excluding first item since it is the requested movie itself
#print(lst)
l = []
k=[]
site=[]
diff=[]
for i in range(len(lst)):
a = lst[i][0]
#print(a)
if(len(l)<10):
l.append(data['course_title'][a])
f=data['course_rating'][a]
user=data['Users'][a]
lev=data['course_difficulty'][a]
if(f>4.8 and len(rate)<10 and user>500 and lev==level):
rate.append(data['course_title'][a])
k.append(data['course_rating'][a])
site.append(data['Site '][a])
diff.append(data['course_difficulty'][a])
return render_template('resrecomm.html',output=rate,o=site)
if __name__==__main__:
 app.run(debug=true)
