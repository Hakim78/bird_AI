<template>
  <div class="app-container">
    <Header />
    
    <!-- Section upload -->
    <div class="upload-section">
      <UploadZone @file-selected="handleAudioUpload" />
      <button 
        @click="submitAudio" 
        :disabled="!audioFile" 
        :class="['submit-button', { 'loading': isLoading }]"
      >
        {{ isLoading ? 'Analyse en cours...' : 'Analyser' }}
      </button>
    </div>
    
    <!-- Section résultats -->
    <div class="results-section" v-if="prediction || spectrogramUrl || topPredictions.length">
      <div class="results-grid">
        <!-- Première colonne -->
        <div class="left-column">
          <AnalysisExplanation 
            v-if="prediction" 
            :label="prediction" 
            :confidence="confidence" 
          />
          
          <Top3Predictions 
            v-if="topPredictions.length" 
            :predictions="topPredictions" 
          />
          
          <FallbackSuggestions 
            v-if="fallbackActive && !birdData" 
            :alternatives="fallbackOptions" 
          />
        </div>
        
        <!-- Deuxième colonne -->
        <div class="right-column">
          <SpectrogramView 
            v-if="spectrogramUrl" 
            :spectrogramUrl="spectrogramUrl" 
          />
          
          <BirdCard 
            v-if="birdData" 
            :data="birdData" 
          />
        </div>
      </div>
    </div>
    
    <!-- Section historique -->
    <div class="history-section">
      <PredictionHistory :history="predictionHistory" @select-prediction="loadHistoryItem" />
    </div>
    
    <!-- Section quiz -->
    <div class="quiz-section">
      <LearningQuiz />
    </div>
    
    <!-- Overlay de chargement -->
    <LoadingOverlay :visible="isLoading" message="Analyse du chant en cours..." />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import UploadZone from './components/UploadZone.vue'
import SpectrogramView from './components/SpectrogramView.vue'
import Top3Predictions from './components/Top3Predictions.vue'
import BirdCard from './components/BirdCard.vue'
import AnalysisExplanation from './components/AnalysisExplanation.vue'
import FallbackSuggestions from './components/FallbackSuggestions.vue'
import PredictionHistory from './components/PredictionHistory.vue'
import LearningQuiz from './components/LearningQuiz.vue'
import LoadingOverlay from './components/LoadingOverlay.vue'

export default {
  components: {
    Header,
    UploadZone,
    SpectrogramView,
    Top3Predictions,
    BirdCard,
    AnalysisExplanation,
    FallbackSuggestions,
    PredictionHistory,
    LearningQuiz,
    LoadingOverlay
  },
  data() {
    return {
      audioFile: null,
      prediction: '',
      confidence: 0,
      spectrogramUrl: '',
      topPredictions: [],
      birdData: null,
      fallbackOptions: [],
      fallbackActive: false,
      predictionHistory: [],
      isLoading: false
    };
  },
  created() {
    const savedHistory = localStorage.getItem('predictionHistory');
    if (savedHistory) {
      try {
        this.predictionHistory = JSON.parse(savedHistory);
      } catch (error) {
        console.error("Erreur de parsing de l'historique:", error);
        this.predictionHistory = [];
      }
    }
  },
  methods: {
    handleAudioUpload(file) {
      this.audioFile = file;
    },
    
    async submitAudio() {
      if (!this.audioFile || this.isLoading) return;
      
      this.isLoading = true;
      
      const formData = new FormData();
      formData.append("file", this.audioFile);

      try {
        const res = await fetch("http://localhost:5000/predict", {
          method: "POST",
          body: formData
        });

        if (!res.ok) {
          throw new Error(`Erreur serveur: ${res.status}`);
        }

        const data = await res.json();

        this.prediction = data.prediction;
        this.confidence = data.confidence;
        this.topPredictions = data.top3 || [];
        this.spectrogramUrl = data.spectrogram_url;
        this.birdData = data.bird_info || null;
        this.fallbackOptions = data.fallback || [];
        this.fallbackActive = !data.bird_info;

        const newItem = {
          prediction: data.prediction,
          confidence: data.confidence,
          timestamp: Date.now()
        };

        this.predictionHistory.unshift(newItem);
        this.predictionHistory = this.predictionHistory.slice(0, 5);

        localStorage.setItem('predictionHistory', JSON.stringify(this.predictionHistory));
      } catch (error) {
        console.error("Erreur lors de l'analyse:", error);
        alert(`Erreur: ${error.message || "Problème de connexion au serveur"}`);
      } finally {
        this.isLoading = false;
      }
    },
    
    loadHistoryItem(item) {
      // Pour charger un élément de l'historique
      this.prediction = item.prediction;
      this.confidence = item.confidence;
      
      // Si vous avez besoin de recharger les détails de l'oiseau
      // this.fetchBirdDetails(item.prediction);
    }
  }
};
</script>

<style>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  background: linear-gradient(135deg, #e1f1f7, #e8f4ed);
  min-height: 100vh;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.upload-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: center;
}

.results-section {
  margin-top: 1rem;
}

.results-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.left-column, .right-column {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.history-section, .quiz-section {
  margin-top: 1rem;
}

/* Pour le bouton submit */
.submit-button {
  min-width: 200px;
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.submit-button.loading {
  background-color: #a5cddb;
  cursor: not-allowed;
  position: relative;
  overflow: hidden;
}

.submit-button.loading::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 200%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  animation: loading-shine 1.5s infinite;
}

@keyframes loading-shine {
  to {
    left: 100%;
  }
}

/* Responsive design */
@media (max-width: 768px) {
  .results-grid {
    grid-template-columns: 1fr;
  }
  
  .app-container {
    padding: 1rem;
  }
}
</style>