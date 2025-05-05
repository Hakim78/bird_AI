<template>
    <div class="bird-card" v-if="data">
      <div class="card-header">
        <div class="header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 3l4 4-8 12L0 11 4 7l4.5 1L12 2l2.5 5L18 3z"></path>
          </svg>
        </div>
        <h2>Fiche d'espèce</h2>
        <div class="header-actions">
          <button class="action-button" @click="toggleFavorite" :class="{ 'active': isFavorite }" title="Ajouter aux favoris">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"></path>
            </svg>
          </button>
        </div>
      </div>
      
      <div class="card-content">
        <div class="image-gallery">
          <div class="main-image-container" @click="toggleZoom">
            <img :src="data.image" alt="Image de l'oiseau" class="main-image" :class="{ 'zoomed': isZoomed }" />
            <div class="image-overlay">
              <svg v-if="!isZoomed" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                <line x1="11" y1="8" x2="11" y2="14"></line>
                <line x1="8" y1="11" x2="14" y2="11"></line>
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                <line x1="8" y1="11" x2="14" y2="11"></line>
              </svg>
            </div>
          </div>
        </div>
        
        <div class="species-info">
          <div class="species-name">
            <h3>{{ data.common_name || data.latin_name }}</h3>
            <p class="latin-name"><em>{{ data.latin_name }}</em></p>
          </div>
          
          <div class="info-cards">
            <div class="info-card">
              <div class="info-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                  <line x1="2" y1="12" x2="22" y2="12"></line>
                </svg>
              </div>
              <div class="info-content">
                <h4>Habitat</h4>
                <p>{{ data.zone || 'Information non disponible' }}</p>
              </div>
            </div>
            
            <div class="info-card">
              <div class="info-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
                  <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
                </svg>
              </div>
              <div class="info-content">
                <h4>Vocalisations</h4>
                <p>Chant mélodieux et varié, souvent entendu à l'aube et au crépuscule.</p>
              </div>
            </div>
          </div>
          
          <div class="description-box">
            <h4>Description</h4>
            <p>{{ data.info || 'Aucune information disponible pour cette espèce.' }}</p>
          </div>
          
          <div class="audio-player">
            <h4>Exemples sonores</h4>
            <div class="audio-container">
              <audio controls :src="data.sound" class="sound-player"></audio>
              <div class="audio-controls">
                <button class="control-button download-button" @click="downloadSound" title="Télécharger le son">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="card-footer">
        <button class="footer-button" @click="showMoreInfo">
          En savoir plus
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "BirdCard",
    props: {
      data: Object
    },
    data() {
      return {
        isZoomed: false,
        isFavorite: false
      };
    },
    methods: {
      toggleZoom() {
        this.isZoomed = !this.isZoomed;
      },
      toggleFavorite() {
        this.isFavorite = !this.isFavorite;
        
        // Ici, on pourrait implémenter la sauvegarde des favoris
        if (this.isFavorite) {
          this.saveFavorite();
        } else {
          this.removeFavorite();
        }
      },
      saveFavorite() {
        // Implémenter la sauvegarde du favori
        // localStorage ou appel API
        console.log('Oiseau ajouté aux favoris:', this.data.latin_name);
      },
      removeFavorite() {
        // Implémenter la suppression du favori
        console.log('Oiseau retiré des favoris:', this.data.latin_name);
      },
      downloadSound() {
        // Créer un lien de téléchargement pour le son
        if (this.data.sound) {
          const link = document.createElement('a');
          link.href = this.data.sound;
          link.download = `${this.data.latin_name || 'bird'}_sound.mp3`;
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        }
      },
      showMoreInfo() {
        // Rediriger vers une page avec plus d'informations ou ouvrir une modal
        window.open(`https://www.oiseaux.net/search?bird=${encodeURIComponent(this.data.latin_name)}`, '_blank');
      }
    },
    mounted() {
      // Vérifier si cet oiseau est déjà en favori
      const favorites = JSON.parse(localStorage.getItem('birdFavorites') || '[]');
      this.isFavorite = favorites.some(fav => fav.latin_name === this.data.latin_name);
    }
  };
  </script>
  
  <style scoped>
  .bird-card {
    background-color: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeIn 0.5s ease;
    margin-bottom: 1.5rem;
    position: relative;
  }
  
  .bird-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  
  .card-header {
    background: linear-gradient(90deg, #7fa98f, #5a8b76);
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
  
  .card-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    flex: 1;
  }
  
  .header-actions {
    display: flex;
    gap: 0.5rem;
  }
  
  .action-button {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .action-button:hover {
    background: rgba(255, 255, 255, 0.4);
  }
  
  .action-button svg {
    width: 16px;
    height: 16px;
    stroke: white;
    fill: none;
    transition: all 0.2s ease;
  }
  
  .action-button.active svg {
    fill: white;
  }
  
  .card-content {
    padding: 0;
  }
  
  .image-gallery {
    position: relative;
    height: 250px;
    overflow: hidden;
  }
  
  .main-image-container {
    width: 100%;
    height: 100%;
    position: relative;
    cursor: zoom-in;
    overflow: hidden;
  }
  
  .main-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  
  .main-image.zoomed {
    transform: scale(1.5);
    cursor: zoom-out;
  }
  
  .image-overlay {
    position: absolute;
    bottom: 10px;
    right: 10px;
    width: 40px;
    height: 40px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0.7;
    transition: opacity 0.2s ease;
    z-index: 2;
  }
  
  .image-overlay:hover {
    opacity: 1;
  }
  
  .image-overlay svg {
    width: 24px;
    height: 24px;
    stroke: #7fa98f;
  }
  
  .species-info {
    padding: 1.5rem;
  }
  
  .species-name {
    margin-bottom: 1.25rem;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 1rem;
  }
  
  .species-name h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 0 0.25rem;
    color: #2c3e50;
  }
  
  .latin-name {
    font-size: 1rem;
    color: #5f6368;
    margin: 0;
  }
  
  .info-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1.25rem;
  }
  
  .info-card {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 1rem;
    display: flex;
    transition: all 0.3s ease;
  }
  
  .info-card:hover {
    background-color: #f1f9f4;
    transform: translateY(-2px);
  }
  
  .info-icon {
    width: 36px;
    height: 36px;
    min-width: 36px;
    margin-right: 0.75rem;
    background-color: rgba(127, 169, 143, 0.15);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .info-icon svg {
    width: 20px;
    height: 20px;
    stroke: #7fa98f;
  }
  
  .info-content h4 {
    margin: 0 0 0.5rem;
    font-size: 0.9rem;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .info-content p {
    margin: 0;
    font-size: 0.8rem;
    color: #5f6368;
    line-height: 1.4;
  }
  
  .description-box {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 1.25rem;
    margin-bottom: 1.25rem;
    transition: all 0.3s ease;
  }
  
  .description-box:hover {
    background-color: #f1f9f4;
  }
  
  .description-box h4 {
    margin: 0 0 0.75rem;
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .description-box p {
    margin: 0;
    font-size: 0.9rem;
    color: #5f6368;
    line-height: 1.6;
  }
  
  .audio-player {
    margin-top: 1.25rem;
  }
  
  .audio-player h4 {
    margin: 0 0 0.75rem;
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
  }
  
  .audio-container {
    display: flex;
    align-items: center;
    gap: 1rem;
    position: relative;
  }
  
  .sound-player {
    flex: 1;
    border-radius: 30px;
    height: 40px;
  }
  
  .sound-player::-webkit-media-controls-panel {
    background-color: #f8f9fa;
  }
  
  .sound-player::-webkit-media-controls-play-button {
    background-color: #7fa98f;
    border-radius: 50%;
  }
  
  .audio-controls {
    display: flex;
    gap: 0.5rem;
  }
  
  .control-button {
    background-color: #f8f9fa;
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .control-button:hover {
    background-color: #7fa98f;
  }
  
  .control-button:hover svg {
    stroke: white;
  }
  
  .control-button svg {
    width: 16px;
    height: 16px;
    stroke: #7fa98f;
  }
  
  .card-footer {
    background-color: #f8f9fa;
    padding: 1rem;
    display: flex;
    justify-content: flex-end;
    border-top: 1px solid #f0f0f0;
  }
  
  .footer-button {
    background: none;
    border: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #7fa98f;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 0.5rem 1rem;
    border-radius: 20px;
  }
  
  .footer-button:hover {
    background-color: rgba(127, 169, 143, 0.1);
  }
  
  .footer-button svg {
    width: 16px;
    height: 16px;
    stroke: currentColor;
    transition: transform 0.2s ease;
  }
  
  .footer-button:hover svg {
    transform: translateX(4px);
  }
  
  /* Animations */
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
  
  /* Responsive */
  @media (max-width: 768px) {
    .info-cards {
      grid-template-columns: 1fr;
    }
    
    .audio-container {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .audio-controls {
      margin-top: 0.5rem;
    }
  }
  
  @media (max-width: 576px) {
    .species-name h3 {
      font-size: 1.25rem;
    }
    
    .latin-name {
      font-size: 0.9rem;
    }
    
    .image-gallery {
      height: 200px;
    }
    
    .description-box, 
    .info-card {
      padding: 1rem;
    }
  }
  
  /* Animation pour l'effet de pulsation du coeur lorsqu'on clique sur le bouton de favori */
  @keyframes heartBeat {
    0% {
      transform: scale(1);
    }
    14% {
      transform: scale(1.3);
    }
    28% {
      transform: scale(1);
    }
    42% {
      transform: scale(1.3);
    }
    70% {
      transform: scale(1);
    }
  }
  
  .action-button.active {
    animation: heartBeat 1s;
  }
  
  /* Effet de transition en douceur pour l'image */
  .main-image-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to bottom,
      transparent 70%,
      rgba(0, 0, 0, 0.2) 100%
    );
    z-index: 1;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  .main-image-container:hover::before {
    opacity: 1;
  }
  
  /* Effet de carte qui semble se soulever lorsqu'on survole */
  .info-card, .description-box {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
  }
  
  .info-card:hover, .description-box:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  }
  
  /* Accessibilité : focus style */
  .action-button:focus,
  .control-button:focus,
  .footer-button:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(127, 169, 143, 0.5);
  }
  </style>