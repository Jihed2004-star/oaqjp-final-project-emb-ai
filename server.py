from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import *

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    text=request.args.get("textToAnalyze")
    res=emotion_detector(text)
    if res["dominant_emotion"]==None:
        return "Invalid Text"
    f_res=(f"For the given statement, the system response is 'anger': {res['anger']}, 'disgust': {res.get('disgust')}, 'fear': {res.get('fear')}, 'joy': {res.get('joy')} and 'sadness':{res.get('sadness')}. The dominant emotion is joy.")
    return f_res

