import os
import csv

# Chemin absolu vers ton dossier bird_audio
BASE_DIR = "C:/Users/willi/Documents/Ecole_ipssi_MIA4/avril_mai_2025/tp_groupe/bird_audio"
OUTPUT_CSV = "generate/new_metadata.csv"  # Le CSV sera généré dans le dossier generate

# Champs du CSV
columns = [
    "primary_label",
    "filename",
    "type",
    "rating",
    "duration",
    "samplerate"
]

data = []

for label in os.listdir(BASE_DIR):
    label_path = os.path.join(BASE_DIR, label)
    if os.path.isdir(label_path):
        for file in os.listdir(label_path):
            if file.endswith(".ogg"):
                data.append({
                    "primary_label": label,
                    "filename": f"{label}/{file}",
                    "type": "song",
                    "rating": 5.0,
                    "duration": 5,          # Valeur fictive à adapter si besoin
                    "samplerate": 32000     # D’après tes métadonnées
                })

# Création du fichier CSV
with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)

print(f"✅ CSV généré avec succès à : {OUTPUT_CSV}")
