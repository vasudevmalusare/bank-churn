from flask import Flask, render_template, url_for, redirect, request
import utils


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<pred>')
def result(pred):
    return render_template('result.html', score = pred)


@app.route('/submit',methods = ['POST','GET'])
def submit():
    data = request.form
    if request.method == 'POST':
        print('Testing Result API',data)

        x1 = float(data['RowNumber'])
        x2 = float(data['CreditScore'])
        x3 = float(data['Geography'])
        x4 = float(data['Gender'])
        x5 = float(data['Age'])
        x6 = float(data['Tenure'])
        x7 = float(data['Balance'])
        x8 = float(data['NumOfProducts'])
        x9 = float(data['HasCrCard'])
        x10 = float(data['IsActiveMember'])
        x11 = float(data['EstimatedSalary'])

        res = utils.prediction(x1,x2,x3, x4, x5, x6, x7, x8, x9, x10, x11)

        entry = ""

        if res == 1:
            entry = 'Employee is leaving'
        else:
            
            entry = 'Employee is Not leaving'

        return redirect(url_for('result',pred = entry))
    
    else:
        return "Model Failed"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)