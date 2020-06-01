from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/conf", methods=["POST"])
def config():
    #menangkap ip mikrotik client
    data = request.get_json()
    ip_mik = data["ip_router"]
    # Cetak ip Mikrotik
    print (f"IP Address Mikrotik adalah : {ip_mik}")
    return jsonify(data)
    

if __name__ == "__main__":
    app.run (host='192.168.122.1', debug=True, port=5005)