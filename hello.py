from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/json', methods=['POST'])
def index(): 
    try:
        text = request.json['Text']
        try:
            if text == 'Hello':
                return jsonify({"Text": "Hello From the other side"})
            else:
                return jsonify({"Error": "Wrong or missing data"})
        except NameError:
            return jsonify({"NameError": "Undefined Variable!!!"})       
    except KeyError:
        return jsonify({"KeyError": "Unknown Key!!!"})  

@app.route('/form', methods=['POST'])
def base():
    try:
        text = request.form['Text']
        try:    
            if text == 'Hello':
                msg = 'Hello from the other side'
            else:
                msg = 'Wrong or missing data'
        except NameError:
            msg = 'Undefined Variable!!!'        
        return render_template('form.html', text_msg=msg)
    except KeyError:
        msg = 'Unkown Key!!!'
        return render_template('form.html', text_msg=msg)            