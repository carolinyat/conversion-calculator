from flask import Flask, request, jsonify, render_template
import requests

app = Flask(_name_)

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

@app.route('/convert/currency', methods=['GET'])
def convert_currency():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')

    api_key = '0915a477d0bfd9be374e5a8d' 
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({'error': 'Erro ao acessar a API de câmbio'}), 400

    data = response.json()

    # Verifica se a moeda de destino existe na resposta
    conversion_rate = data['rates'].get(to_currency)

    if conversion_rate is None:
        return jsonify({'error': 'Moeda de destino não suportada'}), 400

    converted_amount = amount * conversion_rate

    return jsonify({'result': converted_amount})

if _name_ == '_main_':
    app.run(debug=True)