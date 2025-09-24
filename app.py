from flask import Flask, request, send_file, jsonify
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "QR Code service online! Use /qrcode?text=seu_texto"})

@app.route("/qrcode", methods=["GET"])
def generate_qrcode():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "Parâmetro 'text' é obrigatório"}), 400

    # Gerar QRCode
    img = qrcode.make(text)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")
