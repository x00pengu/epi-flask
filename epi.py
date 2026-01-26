from flask import Flask, jsonify
import netifaces
import requests

app = Flask(__name__)

def get_wan_ip():
    try:
        wan_interface = 'ens33'  # Change this to match your pfSense WAN interface
        addrs = netifaces.ifaddresses(wan_interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except Exception as e:
        return f"Error detecting WAN IP: {str(e)}"

def get_va_ip():
    try:
        # Use requests library to make HTTP request
        response = requests.get('https://wtfismyip.com/json', timeout=5)
        return response.json()['YourFuckingIPAddress']
    except Exception as e:
        return f"Error detecting VA IP: {str(e)}"

@app.route('/all')
def debug():
    # Show both for comparison
    return jsonify({
        "egress_ip": get_wan_ip(),
        "va_public_ip": get_va_ip()
    })

@app.route('/vaip')
def get_public_ip():
    # Return what external services see
    public_ip = get_va_ip()
    return jsonify({"va_public_ip": public_ip})

@app.route('/egress')
def get_ip():
    # Dynamically get the current WAN IP
    egress_ip = get_wan_ip()
    return jsonify({"egress_ip": egress_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
