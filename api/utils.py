import librosa
import matplotlib
matplotlib.use('Agg')

import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from PIL import Image
import io

def audio_to_spectrogram_image(audio_path, img_size=(128, 128)):  # ✅ Taille 128x128
    y, sr = librosa.load(audio_path, sr=None)

    # Spectrogramme
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Sauvegarde image temporaire du spectrogramme
    fig = plt.figure(figsize=(1.28, 1.28), dpi=100)  # => 128px x 128px
    plt.axis('off')
    librosa.display.specshow(S_dB, sr=sr)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    buf.seek(0)

    image = Image.open(buf).convert('RGB')
    image = image.resize(img_size)  # ✅ Redimensionne à (128, 128)
    image_array = np.array(image) / 255.0  # Normalise
    return np.expand_dims(image_array, axis=0)  # ✅ shape (1, 128, 128, 3)

