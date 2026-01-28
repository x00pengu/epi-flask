from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "APP 1 Working!"

@app.route('/egress')
def get_client_ip():
    client_ip = request.remote_addr
    return client_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
