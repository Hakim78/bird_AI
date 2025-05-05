<template>
    <div v-if="prediction" class="result-box">
      <div class="result-header">
        <div class="header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
          </svg>
        </div>
        <h2>Prédiction</h2>
      </div>
      
      <div class="result-content">
        <div class="bird-name">
          <span class="bird-label">Espèce identifiée :</span>
          <span class="bird-value">{{ prediction }}</span>
        </div>
        
        <div class="confidence-container">
          <div class="confidence-label">
            <span>Niveau de confiance</span>
            <span class="confidence-value">{{ getConfidenceDisplay() }}</span>
          </div>
          
          <div class="bar-background">
            <div class="bar-fill" :style="{ width: confidence + '%', backgroundColor: getBarColor() }"></div>
          </div>
          
          <p class="confidence-text">{{ getConfidenceMessage() }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "PredictionResult",
    props: {
      prediction: String,
      confidence: Number
    },
    methods: {
      getConfidenceDisplay() {
        return this.confidence.toFixed(1) + '%';
      },
      getBarColor() {
        if (this.confidence >= 80) return '#7fa98f';
        if (this.confidence >= 60) return '#a5cddb';
        if (this.confidence >= 40) return '#d9c5a0';
        return '#e57373';
      },
      getConfidenceMessage() {
        if (this.confidence >= 90) {
          return '✅ Identification très fiable';
        } else if (this.confidence >= 70) {
          return '🧐 Identification probable';
        } else if (this.confidence >= 50) {
          return '⚠️ À vérifier manuellement';
        } else {
          return '❌ Faible confiance, refaire un enregistrement';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .result-box {
    background-color: white;
    border-radius: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    margin-bottom: 1.5rem;
    animation: slideInFade 0.6s ease-out;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .result-box:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  
  .result-header {
    background-color: #7fa98f;
    color: white;
    padding: 1rem;
    display: flex;
    align-items: center;
    position: relative;
  }
  
  .header-icon {
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
  }
  
  .result-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
  }
  
  .result-content {
    padding: 1.5rem;
  }
  
  .bird-name {
    margin-bottom: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.5rem;
  }
  
  .bird-label {
    font-size: 0.9rem;
    color: #5f6368;
  }
  
  .bird-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #3c4043;
    padding-left: 0.25rem;
    transition: transform 0.2s ease;
  }
  
  .result-box:hover .bird-value {
    transform: translateX(3px);
  }
  
  .confidence-container {
    margin-top: 1rem;
  }
  
  .confidence-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    color: #5f6368;
  }
  
  .confidence-value {
    font-weight: 600;
    color: #3c4043;
  }
  
  .bar-background {
    width: 100%;
    height: 8px;
    background-color: #f5f5f5;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 0.75rem;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  
  .bar-fill {
    height: 100%;
    width: 0%;
    border-radius: 4px;
    animation: barFill 1s ease forwards;
  }
  
  .confidence-text {
    font-size: 0.9rem;
    color: #5f6368;
    margin-top: 0.5rem;
    transition: transform 0.2s ease;
  }
  
  .result-box:hover .confidence-text {
    transform: translateX(3px);
  }
  
  @keyframes barFill {
    0% {
      width: 0%;
    }
    100% {
      width: var(--width);
    }
  }
  
  @keyframes slideInFade {
    0% {
      opacity: 0;
      transform: translateY(20px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
  </style>