<template>
    <div class="bird-profile" v-if="bird">
      <h2>Fiche de l’Oiseau</h2>
  
      <img :src="bird.image" alt="Image oiseau" class="bird-image" />
  
      <div class="bird-info">
        <p><strong>Nom scientifique :</strong> {{ bird.latin_name }}</p>
        <p><strong>Zone géographique :</strong> {{ bird.zone }}</p>
        <p><strong>Description :</strong> {{ bird.info }}</p>
      </div>
  
      <div class="bird-sound">
        <h3>Exemple sonore :</h3>
        <audio controls :src="bird.sound"></audio>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      bird: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  