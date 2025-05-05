<template>
    <div class="learning-quiz" v-if="quizQuestion">
      <!-- En-tête du quiz avec animation de défilement d'icône -->
      <div class="quiz-header">
        <div class="quiz-title">
          <div class="quiz-icon">
            <span class="icon-brain">🧠</span>
            <span class="icon-bird">🦜</span>
          </div>
          <h2>Quiz Ornithologique</h2>
        </div>
        <div class="quiz-progress">
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: `${(questionsAnswered / totalQuestions) * 100}%` }"></div>
          </div>
          <span class="progress-text">{{ questionsAnswered }}/{{ totalQuestions }}</span>
        </div>
      </div>
  
      <!-- Corps du quiz avec animation de transition entre questions -->
      <transition name="question-fade" mode="out-in">
        <div class="quiz-body" :key="quizQuestion.question">
          <p class="quiz-question">{{ quizQuestion.question }}</p>
          
          <div class="options-container">
            <transition-group name="option-list" tag="ul" class="quiz-options">
              <li 
                v-for="(option, idx) in quizQuestion.options" 
                :key="option"
                :class="[
                  'quiz-option', 
                  { 
                    'selected': userAnswer === option, 
                    'correct': showAnswer && option === quizQuestion.answer, 
                    'wrong': showAnswer && userAnswer === option && option !== quizQuestion.answer,
                    'disabled': showAnswer
                  }
                ]"
                @click="selectAnswer(option)"
              >
                <div class="option-marker">{{ ['A', 'B', 'C', 'D'][idx] }}</div>
                <div class="option-text">{{ option }}</div>
                <div class="option-status">
                  <svg v-if="showAnswer && option === quizQuestion.answer" class="check-icon" viewBox="0 0 24 24">
                    <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z" />
                  </svg>
                  <svg v-if="showAnswer && userAnswer === option && option !== quizQuestion.answer" class="cross-icon" viewBox="0 0 24 24">
                    <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z" />
                  </svg>
                </div>
              </li>
            </transition-group>
          </div>
        </div>
      </transition>
  
      <!-- Feedback après réponse -->
      <transition name="feedback-slide">
        <div v-if="showAnswer" class="quiz-feedback" :class="userAnswer === quizQuestion.answer ? 'correct-feedback' : 'wrong-feedback'">
          <div class="feedback-icon">
            <span v-if="userAnswer === quizQuestion.answer">🎉</span>
            <span v-else>🔍</span>
          </div>
          
          <div class="feedback-content">
            <h3 v-if="userAnswer === quizQuestion.answer" class="correct-title">Excellente réponse !</h3>
            <h3 v-else class="wrong-title">Pas tout à fait...</h3>
            
            <p v-if="userAnswer === quizQuestion.answer" class="feedback-text">
              Vous connaissez bien vos oiseaux. Continuez ainsi !
            </p>
            <p v-else class="feedback-text">
              La bonne réponse était <strong>{{ quizQuestion.answer }}</strong>. 
              N'abandonnez pas, l'ornithologie s'apprend avec le temps.
            </p>
            
            <button @click="loadNewQuestion" class="next-button">
              <span>Question suivante</span>
              <svg class="arrow-icon" viewBox="0 0 24 24">
                <path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z" />
              </svg>
            </button>
          </div>
        </div>
      </transition>
      
      <!-- Score du quiz -->
      <div class="quiz-score">
        <div class="score-circle" :class="{'perfect-score': correctAnswers === questionsAnswered && questionsAnswered > 0}">
          <span class="score-number">{{ correctAnswers }}</span>
          <svg class="score-ring" viewBox="0 0 36 36">
            <path
              class="score-background"
              d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              fill="none"
              stroke="#e5e5e5"
              stroke-width="3"
            />
            <path
              class="score-progress"
              :stroke-dasharray="`${(correctAnswers / Math.max(questionsAnswered, 1)) * 100}, 100`"
              d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
              fill="none"
              stroke="#7fa98f"
              stroke-width="3"
            />
          </svg>
        </div>
        <div class="score-text">
          <p>Score</p>
          <p class="score-percentage">{{ questionsAnswered > 0 ? Math.round((correctAnswers / questionsAnswered) * 100) : 0 }}%</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        quizData: [
          {
            question: "Quel oiseau chante ainsi ?",
            options: ["Rouge-gorge", "Merle noir", "Mésange bleue", "Pinson des arbres"],
            answer: "Merle noir",
            info: "Le merle noir a un chant flûté, mélodieux et varié qui est souvent entendu à l'aube et au crépuscule."
          },
          {
            question: "Quel est le nom scientifique du pigeon ramier ?",
            options: ["Columba livia", "Columba palumbus", "Turdus merula", "Parus caeruleus"],
            answer: "Columba palumbus",
            info: "Le pigeon ramier (Columba palumbus) est le plus grand des pigeons européens, reconnaissable à son collier blanc."
          },
          {
            question: "Quel oiseau est souvent entendu au printemps et dit « coucou » ?",
            options: ["Rossignol", "Geai", "Coucou gris", "Fauvette"],
            answer: "Coucou gris",
            info: "Le coucou gris (Cuculus canorus) est connu pour son chant caractéristique qui a donné son nom à l'espèce."
          },
          {
            question: "Quelle est la caractéristique du plumage du chardonneret élégant ?",
            options: ["Entièrement bleu", "Tête rouge et face jaune", "Dos rayé de noir et blanc", "Ventre orange"],
            answer: "Tête rouge et face jaune",
            info: "Le chardonneret élégant possède un plumage très coloré avec une face rouge écarlate bordée de noir et de jaune."
          },
          {
            question: "Quel est l'oiseau le plus rapide en vol piqué ?",
            options: ["Aigle royal", "Martinet noir", "Faucon pèlerin", "Épervier d'Europe"],
            answer: "Faucon pèlerin",
            info: "Le faucon pèlerin peut atteindre plus de 300 km/h en vol piqué, ce qui en fait l'animal le plus rapide du monde."
          }
        ],
        quizQuestion: null,
        userAnswer: null,
        showAnswer: false,
        questionsAnswered: 0,
        correctAnswers: 0,
        usedQuestions: []
      };
    },
    computed: {
      totalQuestions() {
        return this.quizData.length;
      }
    },
    methods: {
      loadNewQuestion() {
        // Réinitialiser l'état
        this.userAnswer = null;
        this.showAnswer = false;
        
        // Si toutes les questions ont été utilisées, réinitialiser
        if (this.usedQuestions.length >= this.quizData.length) {
          this.usedQuestions = [];
        }
        
        // Sélectionner une nouvelle question non utilisée
        let availableQuestions = this.quizData.filter(
          (_, index) => !this.usedQuestions.includes(index)
        );
        
        if (availableQuestions.length > 0) {
          const randomIndex = Math.floor(Math.random() * availableQuestions.length);
          const questionIndex = this.quizData.findIndex(q => q === availableQuestions[randomIndex]);
          this.usedQuestions.push(questionIndex);
          this.quizQuestion = this.quizData[questionIndex];
        } else {
          // Fallback au cas où
          const randomIndex = Math.floor(Math.random() * this.quizData.length);
          this.quizQuestion = this.quizData[randomIndex];
        }
      },
      
      selectAnswer(option) {
        if (!this.showAnswer) {
          this.userAnswer = option;
          this.showAnswer = true;
          this.questionsAnswered++;
          
          if (option === this.quizQuestion.answer) {
            this.correctAnswers++;
          }
        }
      },
      
      resetQuiz() {
        this.questionsAnswered = 0;
        this.correctAnswers = 0;
        this.usedQuestions = [];
        this.loadNewQuestion();
      }
    },
    mounted() {
      this.loadNewQuestion();
    }
  };
  </script>
  
  <style scoped>
  .learning-quiz {
    background: linear-gradient(135deg, #f9fcff, #f5f7fa);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05), 
                0 5px 10px rgba(0, 0, 0, 0.02),
                0 1px 2px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 2rem;
  }
  
  .learning-quiz:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07), 
                0 10px 15px rgba(0, 0, 0, 0.03);
  }
  
  .learning-quiz::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, #a5cddb, #7fa98f);
    z-index: 1;
  }
  
  /* Header styles */
  .quiz-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  }
  
  .quiz-title {
    display: flex;
    align-items: center;
  }
  
  .quiz-icon {
    position: relative;
    width: 40px;
    height: 40px;
    margin-right: 12px;
    perspective: 800px;
  }
  
  .icon-brain, .icon-bird {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    backface-visibility: hidden;
    transition: transform 0.6s ease;
  }
  
  .icon-brain {
    transform: rotateY(0deg);
  }
  
  .icon-bird {
    transform: rotateY(180deg);
  }
  
  .quiz-icon:hover .icon-brain {
    transform: rotateY(180deg);
  }
  
  .quiz-icon:hover .icon-bird {
    transform: rotateY(0deg);
  }
  
  .quiz-title h2 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0;
    background: linear-gradient(90deg, #2c3e50, #4a7c59);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .quiz-progress {
    display: flex;
    align-items: center;
  }
  
  .progress-bar {
    width: 100px;
    height: 6px;
    background-color: #e9ecef;
    border-radius: 3px;
    overflow: hidden;
    margin-right: 8px;
  }
  
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #a5cddb, #7fa98f);
    border-radius: 3px;
    transition: width 0.5s ease;
  }
  
  .progress-text {
    font-size: 14px;
    color: #6c757d;
    font-weight: 500;
  }
  
  /* Body styles */
  .quiz-body {
    margin-bottom: 1.5rem;
  }
  
  .quiz-question {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    text-align: center;
    position: relative;
    padding: 0 1rem;
    line-height: 1.6;
  }
  
  .quiz-question::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 50px;
    height: 3px;
    background: linear-gradient(90deg, #a5cddb, #7fa98f);
    border-radius: 3px;
  }
  
  .options-container {
    margin-top: 2rem;
  }
  
  .quiz-options {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .quiz-option {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 1rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    cursor: pointer;
    transition: all 0.3s ease;
    border-left: 4px solid transparent;
    position: relative;
    overflow: hidden;
  }
  
  .quiz-option:hover:not(.disabled) {
    transform: translateX(8px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    border-left-color: #a5cddb;
  }
  
  .quiz-option.selected {
    background-color: #f3f9ff;
    border-left-color: #a5cddb;
  }
  
  .quiz-option.correct {
    background-color: #f1f9f4;
    border-left-color: #7fa98f;
    animation: correct-pulse 1s ease;
  }
  
  .quiz-option.wrong {
    background-color: #fff5f5;
    border-left-color: #e57373;
    opacity: 0.8;
    animation: wrong-shake 0.5s ease;
  }
  
  .quiz-option.disabled {
    cursor: default;
  }
  
  .option-marker {
    width: 30px;
    height: 30px;
    background: #f3f9ff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 1rem;
    font-weight: 600;
    color: #6c757d;
    transition: all 0.2s ease;
    flex-shrink: 0;
  }
  
  .quiz-option:hover:not(.disabled) .option-marker,
  .quiz-option.selected .option-marker {
    background: #a5cddb;
    color: white;
  }
  
  .quiz-option.correct .option-marker {
    background: #7fa98f;
    color: white;
  }
  
  .quiz-option.wrong .option-marker {
    background: #e57373;
    color: white;
  }
  
  .option-text {
    flex: 1;
    font-size: 1rem;
    font-weight: 500;
    color: #2c3e50;
  }
  
  .option-status {
    width: 24px;
    height: 24px;
    margin-left: 1rem;
    opacity: 0;
    transition: opacity 0.3s ease;
    flex-shrink: 0;
  }
  
  .check-icon, .cross-icon {
    width: 24px;
    height: 24px;
    fill: currentColor;
  }
  
  .quiz-option.correct .option-status {
    opacity: 1;
    color: #7fa98f;
  }
  
  .quiz-option.wrong .option-status {
    opacity: 1;
    color: #e57373;
  }
  
  /* Feedback styles */
  .quiz-feedback {
    display: flex;
    align-items: flex-start;
    padding: 1.25rem;
    margin: 1.5rem 0;
    border-radius: 12px;
    transition: all 0.3s ease;
  }
  
  .correct-feedback {
    background-color: #f1f9f4;
    border-left: 4px solid #7fa98f;
  }
  
  .wrong-feedback {
    background-color: #fff5f5;
    border-left: 4px solid #e57373;
  }
  
  .feedback-icon {
    font-size: 2rem;
    margin-right: 1rem;
    animation: bounce 0.6s ease;
  }
  
  .feedback-content {
    flex: 1;
  }
  
  .correct-title {
    color: #7fa98f;
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
  }
  
  .wrong-title {
    color: #e57373;
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
  }
  
  .feedback-text {
    color: #4a5568;
    margin: 0 0 1rem 0;
    font-size: 0.95rem;
    line-height: 1.5;
  }
  
  .next-button {
    display: flex;
    align-items: center;
    padding: 0.5rem 1rem;
    background-color: #a5cddb;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .next-button:hover {
    background-color: #8fb8c9;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }
  
  .next-button:active {
    transform: translateY(0);
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .arrow-icon {
    width: 20px;
    height: 20px;
    margin-left: 5px;
    fill: currentColor;
    transition: transform 0.2s ease;
  }
  
  .next-button:hover .arrow-icon {
    transform: translateX(4px);
  }
  
  /* Score styles */
  .quiz-score {
    display: flex;
    align-items: center;
    margin-top: 1rem;
    padding: 1rem;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }
  
  .score-circle {
    position: relative;
    width: 60px;
    height: 60px;
    margin-right: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .score-number {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2c3e50;
    z-index: 1;
  }
  
  .score-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    transform: rotate(-90deg);
  }
  
  .score-background {
    stroke-opacity: 0.2;
  }
  
  .score-progress {
    transition: stroke-dasharray 1s ease;
  }
  
  .perfect-score .score-progress {
    stroke: #7fa98f;
    animation: pulse-ring 2s infinite;
  }
  
  .score-text {
    flex: 1;
  }
  
  .score-text p {
    margin: 0;
    color: #6c757d;
    font-size: 0.9rem;
  }
  
  .score-percentage {
    font-size: 1.25rem;
    font-weight: 700;
    color: #2c3e50;
  }
  
  /* Animations */
  @keyframes correct-pulse {
    0% {
      box-shadow: 0 0 0 0 rgba(127, 169, 143, 0.7);
    }
    70% {
      box-shadow: 0 0 0 10px rgba(127, 169, 143, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(127, 169, 143, 0);
    }
  }
  
  @keyframes wrong-shake {
    0%, 100% {
      transform: translateX(0);
    }
    20%, 60% {
      transform: translateX(-5px);
    }
    40%, 80% {
      transform: translateX(5px);
    }
  }
  
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-15px);
    }
    60% {
      transform: translateY(-7px);
    }
  }
  
  @keyframes pulse-ring {
    0% {
      stroke-opacity: 1;
      stroke-width: 3;
    }
    50% {
      stroke-opacity: 0.7;
      stroke-width: 5;
    }
    100% {
      stroke-opacity: 1;
      stroke-width: 3;
    }
  }
  
  /* Transitions */
  .question-fade-enter-active,
  .question-fade-leave-active {
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  
  .question-fade-enter-from,
  .question-fade-leave-to {
    opacity: 0;
    transform: translateY(20px);
  }
  
  .option-list-enter-active,
  .option-list-leave-active {
    transition: all 0.3s ease;
  }
  
  .option-list-enter-from,
  .option-list-leave-to {
    opacity: 0;
    transform: translateX(30px);
  }
  
  .option-list-move {
    transition: transform 0.5s ease;
  }
  
  .feedback-slide-enter-active,
  .feedback-slide-leave-active {
    transition: all 0.5s ease;
  }
  
  .feedback-slide-enter-from,
  .feedback-slide-leave-to {
    opacity: 0;
    transform: translateY(-20px);
  }
  
  @media (max-width: 768px) {
    .quiz-header {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .quiz-progress {
      margin-top: 1rem;
    }
    
    .quiz-feedback {
      flex-direction: column;
    }
    
    .feedback-icon {
      margin-right: 0;
      margin-bottom: 1rem;
    }
  }
  </style>