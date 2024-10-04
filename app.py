from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert/temperature', methods=['GET'])
def convert_temperature():
    value = float(request.args.get('value'))
    from_unit = request.args.get('from')
    to_unit = request.args.get('to')

    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        result = (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        result = (value - 32) * 5/9
    else:
        return jsonify({'error': 'Conversão não suportada'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
