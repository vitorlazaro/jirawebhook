from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def jira_webhook():
    data = request.get_json()
    print("Recebendo dados:")
    print(data) 
    with open("C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\webhook\\response.json", "w") as file_json:
        file_json.write(json.dumps(data, indent=4))
    return 'Dados recebidos'

if __name__ == '__main__':
    app.run(port=5000)