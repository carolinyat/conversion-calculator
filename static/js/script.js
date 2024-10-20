// script.js
async function convert() {
    const value = document.getElementById('value').value;
    const from = document.getElementById('from').value;
    const to = document.getElementById('to').value;

    const response = await fetch(`/convert/temperature?from=${from}&to=${to}&value=${value}`);
    const data = await response.json();
    
    if (response.ok) {
        document.getElementById('result').innerText = `Resultado: ${data.result}`;
    } else {
        document.getElementById('result').innerText = `Erro: ${data.error}`;
    }
}

async function convertCurrency() {
    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    const response = await fetch(`/convert/currency?from=${fromCurrency}&to=${toCurrency}&amount=${amount}`);
    const data = await response.json();
    
    if (response.ok) {
        document.getElementById('currencyResult').innerText = `Resultado: ${data.result}`;
    } else {
        document.getElementById('currencyResult').innerText = `Erro: ${data.error}`;
    }
}