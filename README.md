                            BirdCall AI — Prédiction de chants d'oiseaux par l'IA

Une application Vue.js + Flask permettant de reconnaître des oiseaux à partir de leur chant, enrichie d’un spectrogramme, d’une fiche descriptive et de modules e-learning.

 Sommaire
🧠 Objectif du projet

⚙️ Stack technologique

🚀 Lancement rapide

📁 Structure du projet

🧪 Fonctionnalités clés

📌 Données utilisées

📈 Modèle IA

🎓 Modules éducatifs

🙋 Auteurs et contributions

🎯 Objectif du projet
BirdCall AI est un outil de prédiction sonore capable de reconnaître le chant d’un oiseau grâce à une intelligence artificielle basée sur un modèle CNN entraîné sur des spectrogrammes.
L'application vise également un objectif éducatif, en aidant les utilisateurs à apprendre à distinguer les chants d'oiseaux et à enrichir leur culture ornithologique.

⚙️ Stack technologique
🧠 Backend (IA + API)
Python 3.x

Flask

TensorFlow / Keras

Librosa / NumPy / Matplotlib

Flask-CORS

🎨 Frontend
Vue.js 3 (via Vite)

Vanilla CSS

LocalStorage

🚀 Lancement rapide
1. Clone du projet
git clone https://github.com/ton-utilisateur/birdcall-ai.git
cd birdcall-ai
2. 📦 Installation du backend (Flask)
cd api
pip install -r requirements.txt
Lancer le serveur :

bash
python app.py
3. 💻 Installation du frontend (Vue.js)
cd frontend/frontend-oiseaux
npm install
npm run dev
Le frontend sera disponible sur : http://localhost:5173

📁 Structure du projet
bash
├── api/
│   ├── app.py               # Serveur Flask
│   ├── utils.py             # Génération des spectrogrammes
│   ├── bird_data.json       # Infos enrichies sur les oiseaux
│   └── saved_model/         # Modèle entraîné
│
├── frontend/frontend-oiseaux/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── components/
│   │       ├── Header.vue
│   │       ├── UploadZone.vue
│   │       ├── SpectrogramView.vue
│   │       ├── Top3Predictions.vue
│   │       ├── BirdCard.vue
│   │       ├── AnalysisExplanation.vue
│   │       ├── FallbackSuggestions.vue
│   │       ├── PredictionHistory.vue
│   │       └── LearningQuiz.vue
│   └── style.css
🧪 Fonctionnalités clés
Fonction	Description
🔊 Upload de fichier audio	L’utilisateur dépose un .ogg contenant un chant d’oiseau.
🧠 Prédiction IA	Le backend prédit l’espèce à partir du spectrogramme généré.
📊 Top 3 espèces	Affichage des 3 espèces les plus probables avec leur score.
🌍 Fiche oiseau enrichie	Image, zone géographique, nom scientifique, audio d'exemple.
🖼️ Spectrogramme affiché	Généré en temps réel depuis l’audio.
🧩 Mode quiz (e-learning)	L’utilisateur doit deviner l’espèce à partir d’un son.
🧠 Explication IA (XAI)	En option : affichage de heatmaps ou explication de la prédiction.
🕘 Historique des analyses	Stocké en local, visualisable via la section Historique.
📉 Fallback intelligent	Suggestions générales si l’espèce est inconnue.

📌 Données utilisées
Données audio d’oiseaux (.ogg)

Fichiers .txt contenant les classes (classes.txt)

Spectrogrammes générés via librosa

📈 Modèle IA
Architecture : Convolutional Neural Network ( blocs Conv2D + MaxPooling)

Input : spectrogrammes 128x128

Output : prédiction multi-classe

Entraîné localement sur mon cpu

🎓 Modules éducatifs
Quiz interactif : l’utilisateur apprend à reconnaître les sons.

Explication de la prédiction IA (via messages simplifiés).

Fiches encyclopédiques enrichies.

Parcours utilisateur avec historique et score de progression.

📌 À faire (roadmap)
 ✅ Ajouter un bouton “Réécouter le son”

 ✅ Générer des certificats de niveau

 ✅ Permettre l’upload de plusieurs sons

 🔲 Ajouter un mode “comparaison de chants”

 🔲 Ajouter une interface mobile responsive


