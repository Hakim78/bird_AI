<template>
    <transition name="fade">
      <div class="loading-wrapper" v-if="visible">
        <div class="loading-backdrop"></div>
        <div class="loading-container">
          <div class="spinner-container">
            <div class="spinner-outer">
              <div class="spinner-wave"></div>
              <div class="spinner-inner">
                <svg class="spinner-bird" viewBox="0 0 24 24">
                  <path d="M18 3l4 4-8 12L0 11 4 7l4.5 1L12 2l2.5 5L18 3z" />
                </svg>
              </div>
            </div>
          </div>
          
          <div class="loading-content">
            <h3>{{ message }}</h3>
            <div class="loading-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <p class="loading-tip">{{ randomTip }}</p>
          </div>
        </div>
      </div>
    </transition>
  </template>
  
  <script>
  export default {
    props: {
      visible: {
        type: Boolean,
        default: false
      },
      message: {
        type: String,
        default: "Identification en cours"
      }
    },
    data() {
      return {
        tips: [
          "Saviez-vous que le merle noir peut imiter d'autres oiseaux ?",
          "Les mésanges peuvent mémoriser jusqu'à 1000 cachettes de nourriture.",
          "Le pic-vert peut frapper un arbre jusqu'à 20 fois par seconde.",
          "Le rouge-gorge est territorialement agressif, même contre son reflet.",
          "Le cygne peut vivre plus de 20 ans en milieu naturel."
        ],
        currentTipIndex: 0,
        tipInterval: null
      };
    },
    computed: {
      randomTip() {
        return this.tips[this.currentTipIndex];
      }
    },
    watch: {
      visible(newVal) {
        if (newVal) {
          this.startTipRotation();
        } else {
          this.stopTipRotation();
        }
      }
    },
    methods: {
      startTipRotation() {
        // Choisir un conseil aléatoire pour commencer
        this.currentTipIndex = Math.floor(Math.random() * this.tips.length);
        
        // Changer le conseil toutes les 5 secondes
        this.tipInterval = setInterval(() => {
          this.currentTipIndex = (this.currentTipIndex + 1) % this.tips.length;
        }, 5000);
      },
      stopTipRotation() {
        clearInterval(this.tipInterval);
      }
    },
    beforeUnmount() {
      this.stopTipRotation();
    }
  };
  </script>
  
  <style scoped>
  .loading-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
  }
  
  .loading-backdrop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(8px);
    animation: fadeIn 0.5s ease forwards;
  }
  
  .loading-container {
    position: relative;
    width: 90%;
    max-width: 400px;
    background: linear-gradient(135deg, #ffffff, #f8f9fa);
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(50, 50, 93, 0.1), 
                0 5px 15px rgba(0, 0, 0, 0.07);
    padding: 2.5rem;
    text-align: center;
    animation: slideUpFade 0.5s ease forwards;
    overflow: hidden;
  }
  
  /* Effet de "glow" subtil autour du conteneur */
  .loading-container::before {
    content: '';
    position: absolute;
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    background: linear-gradient(45deg, 
      rgba(165, 205, 219, 0.2),
      rgba(127, 169, 143, 0.2),
      rgba(217, 197, 160, 0.2),
      rgba(165, 205, 219, 0.2)
    );
    border-radius: 25px;
    z-index: -1;
    animation: borderGlow 6s linear infinite;
  }
  
  /* Section du spinner */
  .spinner-container {
    position: relative;
    margin: 0 auto 1.5rem;
    width: 100px;
    height: 100px;
  }
  
  .spinner-outer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(45deg, #a5cddb, #7fa98f);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: pulse 2s ease-in-out infinite;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .spinner-wave {
    position: absolute;
    top: -5px;
    left: -5px;
    right: -5px;
    bottom: -5px;
    border-radius: 50%;
    border: 3px solid transparent;
    background: linear-gradient(45deg, #a5cddb, #7fa98f) border-box;
    -webkit-mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: destination-out;
    mask-composite: exclude;
    animation: ripple 2s linear infinite;
    opacity: 0.7;
  }
  
  .spinner-inner {
    width: 70%;
    height: 70%;
    background-color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .spinner-bird {
    width: 60%;
    height: 60%;
    fill: #7fa98f;
    animation: rotate 10s linear infinite, bounce 2s ease-in-out infinite;
  }
  
  /* Contenu du texte */
  .loading-content {
    position: relative;
  }
  
  .loading-content h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 1rem;
  }
  
  .loading-dots {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    margin-bottom: 1.5rem;
  }
  
  .loading-dots span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #7fa98f;
    animation: dots 1.5s ease infinite;
  }
  
  .loading-dots span:nth-child(2) {
    animation-delay: 0.2s;
  }
  
  .loading-dots span:nth-child(3) {
    animation-delay: 0.4s;
  }
  
  .loading-tip {
    font-size: 0.9rem;
    color: #6c757d;
    line-height: 1.5;
    margin: 0;
    min-height: 4em;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.3s ease;
    animation: fadeText 0.5s ease;
    position: relative;
    padding: 0 1rem;
  }
  
  .loading-tip::before {
    content: '💡';
    font-size: 1.2rem;
    position: absolute;
    left: -5px;
    opacity: 0.7;
  }
  
  /* Animations */
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  
  @keyframes slideUpFade {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes pulse {
    0% {
      transform: scale(0.95);
    }
    50% {
      transform: scale(1.05);
    }
    100% {
      transform: scale(0.95);
    }
  }
  
  @keyframes ripple {
    0% {
      transform: scale(0.9);
      opacity: 0.7;
    }
    50% {
      transform: scale(1.1);
      opacity: 0.3;
    }
    100% {
      transform: scale(0.9);
      opacity: 0.7;
    }
  }
  
  @keyframes rotate {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
  
  @keyframes bounce {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }
  
  @keyframes dots {
    0%, 100% {
      transform: scale(1);
      opacity: 1;
    }
    50% {
      transform: scale(1.5);
      opacity: 0.6;
    }
  }
  
  @keyframes borderGlow {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }
  
  @keyframes fadeText {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  /* Transition de visibilité */
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  
  /* Responsive */
  @media (max-width: 480px) {
    .loading-container {
      padding: 1.5rem;
      max-width: 320px;
    }
    
    .spinner-container {
      width: 80px;
      height: 80px;
      margin-bottom: 1rem;
    }
    
    .loading-content h3 {
      font-size: 1.1rem;
    }
    
    .loading-tip {
      font-size: 0.8rem;
    }
  }
  </style>