from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/mover_no', methods=['POST'])
def mover_no():
    x = random.randint(10, 300)
    y = random.randint(10, 300)
    return jsonify({"x": x, "y": y})

@app.route('/respuesta_si', methods=['POST'])
def respuesta_si():
    return jsonify({"mensaje": "Este detalle es para demostrarte lo mucho que te amo y que sepas lo especial que eres para mí. Cada día me enamoro más y más de ti. 💕"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
