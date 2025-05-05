<template>
    <div class="analysis-explanation" v-if="label">
      <div class="analysis-header">
        <div class="header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
          </svg>
        </div>
        <h2>Analyse Acoustique</h2>
      </div>
      
      <div class="analysis-content">
        <div class="result-summary">
          <div class="summary-animation">
            <div class="sound-wave">
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
          
          <div class="summary-text">
            <p class="summary-intro">Notre IA a analysé le son et identifié :</p>
            <h3 class="bird-species">{{ label }}</h3>
            <div class="confidence-badge" :class="getConfidenceClass(confidence)">
              <span class="confidence-value">{{ (confidence * 100).toFixed(1) }}%</span>
              <span class="confidence-label">{{ getConfidenceLabel(confidence) }}</span>
            </div>
          </div>
        </div>
        
        <div class="analysis-details">
          <div class="detail-card">
            <div class="detail-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
              </svg>
            </div>
            <div class="detail-content">
              <h4>Caractéristiques sonores</h4>
              <p>Cette prédiction est basée sur les motifs sonores spécifiques à l'espèce, notamment la fréquence, le rythme et les motifs mélodiques.</p>
            </div>
          </div>
          
          <div class="detail-suggestions">
            <h4>Suggestions</h4>
            <ul>
              <li v-if="confidence < 0.5">Essayez d'enregistrer le chant avec moins de bruit de fond</li>
              <li v-if="confidence < 0.7">Un enregistrement plus long pourrait améliorer la précision</li>
              <li>Comparez avec les enregistrements de référence pour confirmation</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AnalysisExplanation",
    props: {
      label: String,
      confidence: Number
    },
    methods: {
      getConfidenceClass(confidence) {
        const percent = confidence * 100;
        if (percent >= 80) return 'high-confidence';
        if (percent >= 60) return 'medium-confidence';
        if (percent >= 40) return 'low-confidence';
        return 'very-low-confidence';
      },
      getConfidenceLabel(confidence) {
        const percent = confidence * 100;
        if (percent >= 80) return 'Fiable';
        if (percent >= 60) return 'Probable';
        if (percent >= 40) return 'Incertain';
        return 'Douteux';
      }
    }
  };
  </script>
  
  <style scoped>
  .analysis-explanation {
    background-color: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 1.5rem;
    animation: fadeIn 0.5s ease-out;
  }
  
  .analysis-explanation:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  
  .analysis-header {
    background: linear-gradient(90deg, #7fa98f, #5a8b76);
    color: white;
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
  }
  
  .header-icon {
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
  }
  
  .header-icon svg {
    width: 100%;
    height: 100%;
    stroke: white;
  }
  
  .analysis-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
  }
  
  .analysis-content {
    padding: 1.5rem;
  }
  
  .result-summary {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #f0f0f0;
  }
  
  .summary-animation {
    width: 80px;
    height: 80px;
    margin-right: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(127, 169, 143, 0.1);
    border-radius: 50%;
    position: relative;
  }
  
  .sound-wave {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 40px;
  }
  
  .sound-wave span {
    display: block;
    width: 3px;
    height: 15px;
    margin: 0 1px;
    background-color: #7fa98f;
    border-radius: 3px;
    animation: soundWave 1.2s infinite ease-in-out;
  }
  
  .sound-wave span:nth-child(1) {
    animation-delay: 0s;
    height: 8px;
  }
  
  .sound-wave span:nth-child(2) {
    animation-delay: 0.2s;
    height: 15px;
  }
  
  .sound-wave span:nth-child(3) {
    animation-delay: 0.4s;
    height: 22px;
  }
  
  .sound-wave span:nth-child(4) {
    animation-delay: 0.6s;
    height: 30px;
  }
  
  .sound-wave span:nth-child(5) {
    animation-delay: 0.4s;
    height: 22px;
  }
  
  .sound-wave span:nth-child(6) {
    animation-delay: 0.2s;
    height: 15px;
  }
  
  .sound-wave span:nth-child(7) {
    animation-delay: 0s;
    height: 8px;
  }
  
  @keyframes soundWave {
    0%, 100% {
      transform: scaleY(1);
    }
    50% {
      transform: scaleY(1.5);
    }
  }
  
  .summary-text {
    flex: 1;
  }
  
  .summary-intro {
    margin: 0 0 0.5rem;
    color: #5f6368;
    font-size: 0.9rem;
  }
  
  .bird-species {
    margin: 0 0 0.75rem;
    font-size: 1.5rem;
    font-weight: 700;
    color: #2c3e50;
    transition: transform 0.3s ease;
  }
  
  .analysis-explanation:hover .bird-species {
    transform: translateX(3px);
  }
  
  .confidence-badge {
    display: inline-flex;
    align-items: center;
    padding: 0.4rem 0.75rem;
    border-radius: 30px;
    font-size: 0.85rem;
    font-weight: 500;
    gap: 0.5rem;
  }
  
  .confidence-value {
    font-weight: 700;
  }
  
  .high-confidence {
    background-color: rgba(127, 169, 143, 0.15);
    color: #2c7a51;
  }
  
  .medium-confidence {
    background-color: rgba(165, 205, 219, 0.15);
    color: #3f7a9c;
  }
  
  .low-confidence {
    background-color: rgba(217, 197, 160, 0.15);
    color: #a67a28;
  }
  
  .very-low-confidence {
    background-color: rgba(229, 115, 115, 0.15);
    color: #c93636;
  }
  
  .analysis-details {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  @media (min-width: 768px) {
    .analysis-details {
      grid-template-columns: 1fr 1fr;
    }
  }
  
  .detail-card {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    transition: all 0.3s ease;
  }
  
  .detail-card:hover {
    background-color: #f1f9f4;
    transform: translateY(-2px);
  }
  
  .detail-icon {
    width: 40px;
    height: 40px;
    min-width: 40px;
    margin-right: 1rem;
    background-color: rgba(127, 169, 143, 0.15);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .detail-icon svg {
    width: 24px;
    height: 24px;
    stroke: #7fa98f;
  }
  
  .detail-content h4,
  .detail-suggestions h4 {
    margin: 0 0 0.75rem;
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .detail-content p {
    margin: 0;
    font-size: 0.9rem;
    color: #5f6368;
    line-height: 1.5;
  }
  
  .detail-suggestions {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 1.25rem;
    transition: all 0.3s ease;
  }
  
  .detail-suggestions:hover {
    background-color: #f1f9f4;
    transform: translateY(-2px);
  }
  
  .detail-suggestions ul {
    margin: 0;
    padding-left: 1.25rem;
  }
  
  .detail-suggestions li {
    font-size: 0.9rem;
    color: #5f6368;
    margin-bottom: 0.5rem;
    line-height: 1.5;
  }
  
  .detail-suggestions li:last-child {
    margin-bottom: 0;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @media (max-width: 576px) {
    .result-summary {
      flex-direction: column;
      text-align: center;
    }
    
    .summary-animation {
      margin-right: 0;
      margin-bottom: 1rem;
    }
  }
  </style>