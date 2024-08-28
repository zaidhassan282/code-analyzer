import re #Importing ReGex module
from flask import Flask, jsonify, render_template, redirect, request
from tokenization.WordTokenizer import WordTokernizer

app = Flask(__name__)
@app.route('/')
def handleHome():
    return render_template('index.html')

@app.route('/tokenset', methods = ["GET","POST"])
def handleTokenSet():
    if request.method == "POST":
        try:
            tokenSet = WordTokernizer(request.json)
        except:
            return jsonify([['ERROR','Internal Server Error','500']])
        else:    
            return jsonify(tokenSet)

if __name__=="__main__":
    app.run(debug=True)

