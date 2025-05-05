<template>
    <div class="prediction-history" v-if="history.length">
      <div class="history-header">
        <div class="header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </div>
        <h2>Historique d'analyse</h2>
        <div class="history-actions">
          <button class="action-button" @click="clearHistory" title="Effacer l'historique">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
          </button>
        </div>
      </div>
      
      <div class="history-content">
        <transition-group name="list" tag="ul" class="history-list">
          <li v-for="(item, index) in history" 
              :key="index" 
              class="history-item"
              @click="$emit('select-prediction', item)">
            
            <div class="item-content">
              <div class="item-prediction">
                <div class="item-species" :class="getConfidenceClass(item.confidence)">
                  {{ item.prediction }}
                </div>
                <div class="item-confidence" :class="getConfidenceClass(item.confidence)">
                  {{ (item.confidence * 100).toFixed(1) }}%
                </div>
              </div>
              
              <div class="item-meta">
                <div class="item-timestamp">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  <span>{{ formatDate(item.timestamp) }}</span>
                </div>
                
                <button class="item-play" @click.stop="replayAnalysis(item)" title="Rejouer cette analyse">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                  </svg>
                </button>
              </div>
            </div>
          </li>
        </transition-group>
        
        <div v-if="history.length > 3" class="history-footer">
          <button class="show-more-button" @click="toggleShowAll">
            {{ showAll ? 'Voir moins' : 'Voir tout l\'historique' }}
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="{ 'rotate': showAll }">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      history: {
        type: Array,
        required: true
      }
    },
    emits: ['select-prediction', 'clear-history'],
    data() {
      return {
        showAll: false
      };
    },
    computed: {
      displayedHistory() {
        if (this.showAll || this.history.length <= 3) {
          return this.history;
        }
        return this.history.slice(0, 3);
      }
    },
    methods: {
      formatDate(timestamp) {
        if (!timestamp) return '';
        
        const date = new Date(timestamp);
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMins / 60);
        const diffDays = Math.floor(diffHours / 24);
        
        // Format relative time for recent entries
        if (diffMins < 1) {
          return 'à l\'instant';
        } else if (diffMins < 60) {
          return `il y a ${diffMins} minute${diffMins > 1 ? 's' : ''}`;
        } else if (diffHours < 24) {
          return `il y a ${diffHours} heure${diffHours > 1 ? 's' : ''}`;
        } else if (diffDays < 7) {
          return `il y a ${diffDays} jour${diffDays > 1 ? 's' : ''}`;
        } else {
          // Default to locale string for older entries
          return date.toLocaleString('fr-FR', {
            day: 'numeric',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit'
          });
        }
      },
      toggleShowAll() {
        this.showAll = !this.showAll;
      },
      clearHistory() {
        if (confirm('Êtes-vous sûr de vouloir effacer tout l\'historique?')) {
          this.$emit('clear-history');
        }
      },
      replayAnalysis(item) {
        this.$emit('select-prediction', item);
      },
      getConfidenceClass(confidence) {
        const percent = confidence * 100;
        if (percent >= 80) return 'high-confidence';
        if (percent >= 60) return 'medium-confidence';
        if (percent >= 40) return 'low-confidence';
        return 'very-low-confidence';
      }
    }
  };
  </script>
  
  <style scoped>
  .prediction-history {
    background-color: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 1.5rem;
    animation: fadeIn 0.5s ease;
  }
  
  .prediction-history:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  }
  
  .history-header {
    background: linear-gradient(90deg, #d9c5a0, #c5b288);
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
  
  .history-header h2 {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    flex: 1;
  }
  
  .history-actions {
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
  }
  
  .history-content {
    padding: 0.5rem;
  }
  
  .history-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
    position: relative;
  }
  
  .history-item {
    margin: 0.5rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    border-left: 3px solid transparent;
    position: relative;
  }
  
  .history-item:hover {
    background: #f2ebd9;
    transform: translateX(5px);
    border-left-color: #d9c5a0;
  }
  
  .item-content {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .item-prediction {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .item-species {
    font-weight: 600;
    font-size: 1rem;
    color: #2c3e50;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    transition: all 0.2s ease;
  }
  
  .item-confidence {
    font-size: 0.85rem;
    padding: 0.25rem 0.5rem;
    border-radius: 12px;
    transition: all 0.2s ease;
    font-weight: 600;
  }
  
  /* Classes de confiance */
  .high-confidence {
    color: #2c7a51;
    background-color: rgba(127, 169, 143, 0.15);
  }
  
  .medium-confidence {
    color: #3f7a9c;
    background-color: rgba(165, 205, 219, 0.15);
  }
  
  .low-confidence {
    color: #a67a28;
    background-color: rgba(217, 197, 160, 0.15);
  }
  
  .very-low-confidence {
    color: #c93636;
    background-color: rgba(229, 115, 115, 0.15);
  }
  
  .history-item:hover .item-confidence {
    color: white;
  }
  
  .history-item:hover .high-confidence {
    background-color: #7fa98f;
  }
  
  .history-item:hover .medium-confidence {
    background-color: #a5cddb;
  }
  
  .history-item:hover .low-confidence {
    background-color: #d9c5a0;
  }
  
  .history-item:hover .very-low-confidence {
    background-color: #e57373;
  }
  
  .item-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 0.25rem;
  }
  
  .item-timestamp {
    display: flex;
    align-items: center;
    font-size: 0.75rem;
    color: #6c757d;
  }
  
  .item-timestamp svg {
    width: 12px;
    height: 12px;
    stroke: #6c757d;
    margin-right: 0.25rem;
  }
  
  .item-play {
    background: none;
    border: none;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    opacity: 0.6;
  }
  
  .item-play:hover {
    opacity: 1;
    background-color: rgba(127, 169, 143, 0.2);
  }
  
  .item-play svg {
    width: 14px;
    height: 14px;
    stroke: #7fa98f;
  }
  
  .history-footer {
    display: flex;
    justify-content: center;
    padding: 0.5rem;
    border-top: 1px solid #f0f0f0;
    margin-top: 0.5rem;
  }
  
  .show-more-button {
    background: none;
    border: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #6c757d;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
  }
  
  .show-more-button:hover {
    background-color: #f2f2f2;
    color: #2c3e50;
  }
  
  .show-more-button svg {
    width: 16px;
    height: 16px;
    stroke: currentColor;
    transition: transform 0.2s ease;
  }
  
  .show-more-button svg.rotate {
    transform: rotate(180deg);
  }
  
  /* Animations */
  .list-enter-active,
  .list-leave-active {
    transition: all 0.5s ease;
  }
  
  .list-enter-from {
    opacity: 0;
    transform: translateX(-30px);
  }
  
  .list-leave-to {
    opacity: 0;
    transform: translateX(30px);
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
  
  /* Media queries */
  @media (max-width: 768px) {
    .history-item {
      padding: 0.75rem;
    }
    
    .item-species {
      font-size: 0.9rem;
    }
  }
  </style>