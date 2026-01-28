from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/", methods=["GET", "OPTIONS"])
def health():
    return "ok\n", 200

@app.route("/egress")
def egress():
    wan_ip = request.headers.get("X-PfSense-WAN-IP")
    if not wan_ip:
        abort(500, "WAN IP not provided by pfSense")
    return wan_ip + "\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)