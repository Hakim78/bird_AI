<template>
    <div class="confidence-container" v-if="confidence !== null">
      <div class="confidence-header">
        <div class="confidence-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
          </svg>
        </div>
        <h3>Confiance du modèle</h3>
      </div>
      
      <div class="confidence-content">
        <div class="gauge-container">
          <!-- Jauge circulaire -->
          <div class="gauge">
            <svg class="gauge-svg" viewBox="0 0 120 120">
              <circle class="gauge-background" cx="60" cy="60" r="54" />
              <circle 
                class="gauge-progress" 
                cx="60" 
                cy="60" 
                r="54" 
                :stroke="getBarColor(confidence)"
                :stroke-dasharray="`${confidence * 3.38}, 1000`"
              />
              <text x="60" y="60" class="gauge-text" text-anchor="middle" alignment-baseline="middle">
                {{ confidence.toFixed(0) }}%
              </text>
            </svg>
          </div>
          
          <!-- Niveau de confiance textuel -->
          <div class="level-indicator" :class="getConfidenceClass(confidence)">
            <div class="level-icon">
              <span v-if="confidence >= 90">✅</span>
              <span v-else-if="confidence >= 70">🧐</span>
              <span v-else-if="confidence >= 50">⚠️</span>
              <span v-else>❌</span>
            </div>
            <div class="level-text">{{ getConfidenceLevel(confidence) }}</div>
          </div>
        </div>
        
        <!-- Barre de progression -->
        <div class="progress-section">
          <div class="progress-label">
            <span>Incertain</span>
            <span>Certain</span>
          </div>
          
          <div class="bar-background">
            <div 
              class="bar-fill" 
              :style="{ width: confidence + '%', backgroundColor: getBarColor(confidence) }"
            ></div>
            
            <!-- Marqueurs de seuil -->
            <div class="threshold-marker" style="left: 50%"></div>
            <div class="threshold-marker" style="left: 70%"></div>
            <div class="threshold-marker" style="left: 90%"></div>
          </div>
          
          <p class="confidence-message">{{ getConfidenceMessage(confidence) }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      confidence: {
        type: Number,
        required: true
      }
    },
    methods: {
      getBarColor(value) {
        if (value >= 80) return '#7fa98f'; // vert
        if (value >= 60) return '#a5cddb'; // bleu
        if (value >= 40) return '#d9c5a0'; // beige/jaune
        return '#e57373'; // rouge
      },
      getConfidenceClass(value) {
        if (value >= 80) return 'level-high';
        if (value >= 60) return 'level-medium';
        if (value >= 40) return 'level-low';
        return 'level-very-low';
      },
      getConfidenceLevel(value) {
        if (value >= 90) return 'Très fiable';
        if (value >= 70) return 'Probable';
        if (value >= 50) return 'Incertain';
        return 'Peu fiable';
      },
      getConfidenceMessage(value) {
        if (value >= 90) {
          return 'Identification très fiable avec une forte certitude';
        } else if (value >= 70) {
          return 'Identification probable, bonne confiance dans le résultat';
        } else if (value >= 50) {
          return 'À vérifier manuellement, identification incertaine';
        } else {
          return 'Faible confiance, essayez un autre enregistrement audio';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .confidence-container {
    background-color: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeIn 0.5s ease;
    margin-bottom: 1.5rem;
  }
  
  .confidence-container:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  
  .confidence-header {
    background: linear-gradient(90deg, #a5cddb, #8fb8c9);
    color: white;
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
  }
  
  .confidence-icon {
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
  }
  
  .confidence-icon svg {
    width: 100%;
    height: 100%;
    stroke: white;
  }
  
  .confidence-header h3 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
  }
  
  .confidence-content {
    padding: 1.5rem;
  }
  
  .gauge-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.5rem;
  }
  
  .gauge {
    width: 100px;
    height: 100px;
    position: relative;
  }
  
  .gauge-svg {
    width: 100%;
    height: 100%;
    transform: rotate(-90deg);
  }
  
  .gauge-background {
    fill: none;
    stroke: #f0f0f0;
    stroke-width: 10;
  }
  
  .gauge-progress {
    fill: none;
    stroke-width: 10;
    stroke-linecap: round;
    transition: stroke-dasharray 1s ease;
  }
  
  .gauge-text {
    font-size: 20px;
    font-weight: 700;
    fill: #3c4043;
    transform: rotate(90deg);
  }
  
  .level-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0.75rem 1.25rem;
    border-radius: 12px;
    min-width: 120px;
  }
  
  .level-high {
    background-color: rgba(127, 169, 143, 0.15);
    color: #7fa98f;
  }
  
  .level-medium {
    background-color: rgba(165, 205, 219, 0.15);
    color: #6ca1b4;
  }
  
  .level-low {
    background-color: rgba(217, 197, 160, 0.15);
    color: #b39b63;
  }
  
  .level-very-low {
    background-color: rgba(229, 115, 115, 0.15);
    color: #e57373;
  }
  
  .level-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .level-text {
    font-weight: 600;
    font-size: 1rem;
  }
  
  .progress-section {
    margin-top: 1rem;
  }
  
  .progress-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    color: #5f6368;
    margin-bottom: 0.5rem;
  }
  
  .bar-background {
    width: 100%;
    height: 8px;
    background-color: #f5f5f5;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 1rem;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    position: relative;
  }
  
  .bar-fill {
    height: 100%;
    width: 0;
    border-radius: 4px;
    animation: barFill 1.2s ease forwards;
  }
  
  .threshold-marker {
    position: absolute;
    top: 0;
    width: 2px;
    height: 8px;
    background-color: rgba(0, 0, 0, 0.1);
    z-index: 2;
  }
  
  .confidence-message {
    font-size: 0.9rem;
    color: #5f6368;
    margin: 0.5rem 0 0;
    line-height: 1.5;
    transition: transform 0.2s ease;
  }
  
  .confidence-container:hover .confidence-message {
    transform: translateX(3px);
  }
  
  @keyframes barFill {
    0% {
      width: 0;
    }
    100% {
      width: var(--confidence);
    }
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @media (max-width: 768px) {
    .gauge-container {
      flex-direction: column;
      gap: 1rem;
    }
    
    .level-indicator {
      width: 100%;
    }
  }
  </style>