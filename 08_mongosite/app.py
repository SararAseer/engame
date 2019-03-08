# Team MONGOnificient: Michelle Tang & Jabir Chowdhury & Sarar Aseer
# Softdev pd6
# K#08: Ay Mon, Go Git It From Yer Flask
# 2019-03-07

import os

from flask import Flask, request, render_template, session, redirect

from util import nobelprize

app = Flask(__name__)
app.secret_key = os.urandom(32)
##loads home template
@app.route('/')
def __init__():
    return  render_template('index.html')

##Uses ip from initial form to rebuilt db there
@app.route('/process' , methods = ["POST"])
def __process__():
    ip = request.form.get("ip")
    nobelprize.rebuild(ip)
    return  render_template('query.html' , data = [])

##Takes query
@app.route('/query' , methods = ["POST"])
def __query__():
    query = request.form.get('topic')
    type = request.form.get("type")
    if type == "year":
        lst = nobelprize.find_year(query)##Finds a year, using premade search method
    elif type == "category":
        lst = nobelprize.find_category(query)##Finds a category, using premade search method
    else:
        lst = nobelprize.find_topic(query)
    return render_template('query.html', data = lst)##topic a year, using premade search method

##renerds new template after getting data

if __name__ == "__main__":
    app.debug = True
    app.run()
