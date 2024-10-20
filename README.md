# **Conversion Calculator - Web App**

## **Descrição do Projeto**
A **Conversion Calculator** é uma aplicação web que permite converter valores entre diferentes unidades de medida, como temperatura, distância e moedas. Este projeto utiliza **Python** com o framework **Flask** para o backend, e oferece um API REST para conversões simples.

### **Funcionalidades:**
- Conversão de temperatura: Celsius para Fahrenheit e Fahrenheit para Celsius.
- (Futuro) Conversão de moedas em tempo real com integração de API de câmbio.

## **Instalação**

### **1. Pré-requisitos**
Certifique-se de que você tem o **Python** (versão 3.7 ou superior) instalado em sua máquina. Você pode verificar isso rodando:

```bash
python --version
```

### **2. Clonar o repositório**
Clone o repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/conversion-calculator.git
cd conversion-calculator
```

### **3. Criar e Ativar o Ambiente Virtual**
Crie um ambiente virtual para isolar as dependências do projeto:

- Windows:
```bash
python -m venv venv
.\venv\Scripts\Activate
```

- Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **4. Instalar as Dependências**
Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### **5. Executar o Projeto**
Agora você pode rodar o servidor Flask localmente:

```bash
python app.py
```
O servidor estará disponível em: http://127.0.0.1:5000/

## **Rodando Testes**
### **1. Instalar Pytest**
```bash
pip install pytest
```

### **2. Executar os Testes**
```bash
pytest
```
