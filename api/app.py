from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import os
import numpy as np
import json
from utils import audio_to_spectrogram_image

# Initialisation de l'app Flask
app = Flask(__name__)
CORS(app)

# Chemins vers les modèles et données
MODEL_PATH = os.path.join("..", "ia_model", "saved_model", "bird_classifier.h5")
CLASSES_PATH = os.path.join("..", "ia_model", "saved_model", "classes.txt")
BIRD_DATA_PATH = os.path.join("bird_data.json")  # Chemin relatif ou absolu selon où tu l'as mis

# Chargement du modèle
model = load_model(MODEL_PATH)

# Chargement des noms de classes
with open(CLASSES_PATH, "r") as f:
    class_names = [line.strip() for line in f]

# Chargement des données oiseaux avec fallback
with open(BIRD_DATA_PATH, "r", encoding="utf-8") as f:
    bird_info = json.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier audio reçu."}), 400

    file = request.files["file"]
    audio_path = "temp.ogg"
    file.save(audio_path)

    try:
        print(f"Fichier reçu : {audio_path}")
        image = audio_to_spectrogram_image(audio_path)
        print(f"[INFO] Spectrogramme généré avec shape: {image.shape}")

        predictions = model.predict(image)[0]
        predicted_index = np.argmax(predictions)
        predicted_label = class_names[predicted_index]
        confidence = float(predictions[predicted_index])

        # Top 3
        top_indices = predictions.argsort()[-3:][::-1]
        top_3_preds = [
            {"label": class_names[i], "confidence": float(predictions[i])}
            for i in top_indices
        ]

        # Fallback si données inconnues
        bird_data = bird_info.get(predicted_label, bird_info.get("fallback", {}))

        return jsonify({
            "prediction": predicted_label,
            "confidence": round(confidence, 3),
            "top_predictions": top_3_preds,
            "bird_info": bird_data,
            "spectrogram_url": None  # add path after 
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    app.run(debug=True)
