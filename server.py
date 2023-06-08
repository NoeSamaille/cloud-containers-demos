from flask import Flask
import requests
import os

app = Flask(__name__)

@app.get('/')
def hello():
    return 'Hello Flow'

@app.get('/quote')
def quote():
    category = 'computers'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': os.environ['API_KEY']})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
