from flask import Flask,render_template,redirect,request
import joblib
import warnings
import os
warnings.filterwarnings('ignore')

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        gender=request.form['gender']
        height=request.form['height']
        weight=request.form['weight']
        BP_High=request.form['bp_high']
        BP_Low=request.form['bp_low']
        Cholestrol=request.form['cholestrol']
        gluocose=request.form['gluocose']
        smoke=request.form['smoke']
        alcohol=request.form['alcohol']
        active=request.form['active']
        model=joblib.load(r".\cardio_heart_detection\cardioheart")
        prediction=model.predict([[gender,height,weight,BP_High,BP_Low,Cholestrol,gluocose,smoke,alcohol,active]])
        if prediction == 1 or prediction == '1' :
            return render_template('index2.html')
        else:
            return render_template('index3.html')
        
    return render_template('index.html')




if __name__=='__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    app.run(host='0.0.0.0',port=port)
