from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Fashional Backend Çalışıyor!"

@app.route("/yukle", methods=["POST"])
def yukle():
    if "image" not in request.files:
        return jsonify({"hata": "Dosya bulunamadı"}), 400

    dosya = request.files["image"]
    if dosya.filename == "":
        return jsonify({"hata": "Dosya adı boş"}), 400

    filename = secure_filename(dosya.filename)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    dosya.save(save_path)

    return jsonify({"mesaj": "Dosya alındı", "dosya": filename})
    

app.run(host="0.0.0.0", port=10000)
