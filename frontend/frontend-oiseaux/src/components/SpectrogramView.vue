<template>
    <div class="spectrogram-component" v-if="spectrogramUrl">
      <div class="spectrogram-card">
        <div class="spectrogram-header">
          <div class="header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
              <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
            </svg>
          </div>
          <h2>Spectrogramme Acoustique</h2>
          <div class="spectrogram-controls">
            <button class="control-button hint-button" @click="toggleHint">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" y1="17" x2="12.01" y2="17"></line>
              </svg>
            </button>
          </div>
        </div>
        
        <transition name="hint-fade">
          <div v-if="showHint" class="spectrogram-hint">
            <p>Un spectrogramme visualise les fréquences sonores dans le temps. Les zones plus claires indiquent des sons plus intenses à cette fréquence.</p>
          </div>
        </transition>
        
        <div class="spectrogram-content">
          <div class="image-container">
            <div class="image-frame">
              <img :src="spectrogramUrl" alt="Spectrogramme audio" class="spectrogram-image" :class="{ 'zoom-active': zoomActive }" @click="toggleZoom" />
              
              <!-- Marqueurs de fréquence -->
              <div class="frequency-markers">
                <span>Aigus</span>
                <span>Médiums</span>
                <span>Graves</span>
              </div>
              
              <!-- Échelle de temps -->
              <div class="time-markers">
                <span>0s</span>
                <span>Temps</span>
                <span>5s</span>
              </div>
              
              <!-- Marqueur de zone d'intérêt -->
              <div v-if="birdCallHighlight" class="highlight-zone" :style="birdCallHighlight"></div>
            </div>
          </div>
          
          <div class="spectrogram-info">
            <div class="info-row">
              <div class="info-item">
                <span class="info-label">Durée</span>
                <span class="info-value">5.2 secondes</span>
              </div>
              <div class="info-item">
                <span class="info-label">Fréquence dominante</span>
                <span class="info-value">3.8 kHz</span>
              </div>
            </div>
            
            <div class="pattern-tags">
              <span class="pattern-tag">
                <span class="tag-dot"></span>
                Sifflements
              </span>
              <span class="pattern-tag">
                <span class="tag-dot"></span>
                Trilles
              </span>
              <span v-if="hasPattern('Répétitions')" class="pattern-tag">
                <span class="tag-dot"></span>
                Répétitions
              </span>
            </div>
          </div>
        </div>
        
        <div class="spectrogram-footer">
          <p>Le spectrogramme est généré par analyse de fréquence FFT du son.</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      spectrogramUrl: {
        type: String,
        required: false
      },
      patterns: {
        type: Array,
        default: () => ['Sifflements', 'Trilles']
      },
      highlightArea: {
        type: Object,
        default: null
      }
    },
    data() {
      return {
        showHint: false,
        zoomActive: false,
        birdCallHighlight: { 
          top: '25%', 
          left: '30%', 
          width: '40%', 
          height: '30%' 
        }
      };
    },
    methods: {
      toggleHint() {
        this.showHint = !this.showHint;
      },
      toggleZoom() {
        this.zoomActive = !this.zoomActive;
      },
      hasPattern(pattern) {
        return this.patterns.includes(pattern);
      }
    }
  };
  </script>
  
  <style scoped>
  .spectrogram-component {
    margin-bottom: 2rem;
  }
  
  .spectrogram-card {
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05), 
                0 5px 10px rgba(0, 0, 0, 0.02);
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
  }
  
  .spectrogram-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08), 
                0 10px 20px rgba(0, 0, 0, 0.03);
  }
  
  .spectrogram-header {
    background: linear-gradient(90deg, #a5cddb, #8fb8c9);
    color: white;
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    position: relative;
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
  
  .spectrogram-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    flex: 1;
  }
  
  .spectrogram-controls {
    display: flex;
    gap: 0.5rem;
  }
  
  .control-button {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  
  .control-button:hover {
    background: rgba(255, 255, 255, 0.4);
  }
  
  .control-button svg {
    width: 18px;
    height: 18px;
    stroke: white;
  }
  
  .spectrogram-hint {
    background-color: #f1f9ff;
    padding: 1rem 1.5rem;
    border-bottom: 1px solid #e1f1f7;
  }
  
  .spectrogram-hint p {
    margin: 0;
    font-size: 0.9rem;
    color: #5f6368;
    line-height: 1.5;
  }
  
  .spectrogram-content {
    padding: 1.5rem;
  }
  
  .image-container {
    position: relative;
    margin-bottom: 1.5rem;
  }
  
  .image-frame {
    position: relative;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
    background-color: #f5f7fa;
  }
  
  .spectrogram-image {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.3s ease;
    cursor: zoom-in;
  }
  
  .spectrogram-image.zoom-active {
    transform: scale(1.5);
    cursor: zoom-out;
  }
  
  .frequency-markers {
    position: absolute;
    left: 10px;
    top: 0;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 10px 0;
    color: rgba(0, 0, 0, 0.4);
    font-size: 0.8rem;
    font-weight: 500;
    pointer-events: none;
  }
  
  .time-markers {
    position: absolute;
    bottom: 5px;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 10px;
    color: rgba(0, 0, 0, 0.4);
    font-size: 0.8rem;
    font-weight: 500;
    pointer-events: none;
  }
  
  .highlight-zone {
    position: absolute;
    border: 2px dashed rgba(127, 169, 143, 0.8);
    border-radius: 6px;
    pointer-events: none;
    animation: pulse-border 2s infinite;
  }
  
  .spectrogram-info {
    border-top: 1px solid #f0f0f0;
    padding-top: 1rem;
  }
  
  .info-row {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .info-item {
    display: flex;
    flex-direction: column;
  }
  
  .info-label {
    font-size: 0.8rem;
    color: #5f6368;
    margin-bottom: 0.25rem;
  }
  
  .info-value {
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .pattern-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
  }
  
  .pattern-tag {
    display: inline-flex;
    align-items: center;
    background-color: #f1f9ff;
    padding: 0.4rem 0.75rem;
    border-radius: 16px;
    font-size: 0.8rem;
    color: #5f6368;
  }
  
  .tag-dot {
    width: 8px;
    height: 8px;
    background-color: #a5cddb;
    border-radius: 50%;
    margin-right: 0.4rem;
  }
  
  .pattern-tag:nth-child(2) .tag-dot {
    background-color: #7fa98f;
  }
  
  .pattern-tag:nth-child(3) .tag-dot {
    background-color: #d9c5a0;
  }
  
  .spectrogram-footer {
    border-top: 1px solid #f0f0f0;
    padding: 1rem 1.5rem;
    color: #5f6368;
    font-size: 0.8rem;
    background-color: #f9fafb;
  }
  
  .spectrogram-footer p {
    margin: 0;
  }
  
  /* Animations */
  @keyframes pulse-border {
    0% {
      box-shadow: 0 0 0 0 rgba(127, 169, 143, 0.4);
    }
    70% {
      box-shadow: 0 0 0 10px rgba(127, 169, 143, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(127, 169, 143, 0);
    }
  }
  
  /* Transitions */
  .hint-fade-enter-active,
  .hint-fade-leave-active {
    transition: all 0.3s ease;
  }
  
  .hint-fade-enter-from,
  .hint-fade-leave-to {
    opacity: 0;
    transform: translateY(-10px);
  }
  
  /* Responsive */
  @media (max-width: 768px) {
    .info-row {
      flex-direction: column;
      gap: 0.75rem;
    }
    
    .frequency-markers,
    .time-markers {
      font-size: 0.7rem;
    }
  }
  </style>