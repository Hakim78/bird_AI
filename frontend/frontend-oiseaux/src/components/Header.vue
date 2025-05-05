<template>
    <header class="app-header">
      <div class="logo-container">
        <img src="../assets/bird-logo.png" alt="Logo Prédiction d'Oiseau" class="logo-image" />
        <div class="logo-effect"></div>
      </div>
      
      <div class="header-content">
        <h1 class="site-title">Prédiction d'Oiseau</h1>
        <p class="site-tagline">Identifiez les oiseaux par leur chant</p>
      </div>
      
      <div class="header-decoration">
        <div class="flying-bird"></div>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: "Header"
  }
  </script>
  
  <style scoped>
  .app-header {
    display: flex;
    align-items: center;
    padding: 1.5rem 0;
    position: relative;
    margin-bottom: 2rem;
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.3));
    border-radius: 16px;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.03);
    overflow: hidden;
  }
  
  .logo-container {
    position: relative;
    width: 70px;
    height: 70px;
    margin: 0 1.5rem 0 2rem;
    flex-shrink: 0;
  }
  
  .logo-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
    z-index: 2;
    position: relative;
    filter: drop-shadow(0 2px 5px rgba(0, 0, 0, 0.2));
    transition: transform 0.3s ease;
  }
  
  .app-header:hover .logo-image {
    transform: scale(1.05) rotate(5deg);
  }
  
  .logo-effect {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 54px;
    height: 54px;
    background: rgba(127, 169, 143, 0.2);
    border-radius: 50%;
    z-index: 1;
    animation: pulse 3s infinite ease-in-out;
  }
  
  @keyframes pulse {
    0% {
      transform: translate(-50%, -50%) scale(1);
      opacity: 0.5;
    }
    50% {
      transform: translate(-50%, -50%) scale(1.3);
      opacity: 0.2;
    }
    100% {
      transform: translate(-50%, -50%) scale(1);
      opacity: 0.5;
    }
  }
  
  .header-content {
    flex: 1;
  }
  
  .site-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0;
    color: #2c3e50;
    background: linear-gradient(90deg, #5a8b76, #7fa98f);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.02em;
    position: relative;
  }
  
  .site-title::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 40px;
    height: 3px;
    border-radius: 3px;
    background: linear-gradient(90deg, #7fa98f, #a5cddb);
    transition: width 0.3s ease;
  }
  
  .app-header:hover .site-title::after {
    width: 80px;
  }
  
  .site-tagline {
    margin: 0.5rem 0 0;
    font-size: 1rem;
    color: #5f6368;
    opacity: 0.8;
  }
  
  .header-decoration {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 100px;
    overflow: hidden;
    pointer-events: none;
  }
  
  .flying-bird {
    position: absolute;
    top: 15px;
    right: 20px;
    width: 24px;
    height: 20px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%237fa98f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.5"><path d="M18 3l4 4-8 12L0 11 4 7l4.5 1L12 2l2.5 5L18 3z"/></svg>');
    background-repeat: no-repeat;
    background-size: contain;
    animation: flyAround 15s infinite ease-in-out;
    opacity: 0.3;
  }
  
  @keyframes flyAround {
    0% {
      transform: translate(0, 0) rotate(-10deg);
    }
    25% {
      transform: translate(-30px, 15px) rotate(5deg);
    }
    50% {
      transform: translate(-15px, 30px) rotate(-15deg);
    }
    75% {
      transform: translate(-40px, 10px) rotate(5deg);
    }
    100% {
      transform: translate(0, 0) rotate(-10deg);
    }
  }
  
  /* Media Queries */
  @media (max-width: 768px) {
    .app-header {
      padding: 1rem 0;
      margin-bottom: 1.5rem;
    }
    
    .logo-container {
      width: 60px;
      height: 60px;
      margin: 0 1rem 0 1.25rem;
    }
    
    .site-title {
      font-size: 1.5rem;
    }
    
    .site-tagline {
      font-size: 0.9rem;
    }
    
    .header-decoration {
      width: 60px;
    }
  }
  
  @media (max-width: 480px) {
    .app-header {
      padding: 0.75rem 0;
      margin-bottom: 1rem;
    }
    
    .logo-container {
      width: 50px;
      height: 50px;
      margin: 0 0.75rem 0 1rem;
    }
    
    .site-title {
      font-size: 1.2rem;
    }
    
    .site-tagline {
      font-size: 0.8rem;
    }
    
    .header-decoration {
      display: none;
    }
  }
  </style>