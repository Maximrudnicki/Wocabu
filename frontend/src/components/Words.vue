<template>
  <div class="container">
    <header class="header">
      <h1>MY DICTIONARY</h1>
    </header>
    <WordForm v-if="showForm" />
    <main class="content">
      <button @click="showForm = true" class="action-button">Add Word</button>
      <div class="words-list">
        <ul>
          <li v-for="word in words" :key="word.id" class="word-card">
            <div class="word-content">
              <strong>{{ word.word }}</strong>
              <p>{{ word.definition }}</p>
              <WordDetails :word="word" :show="showWordDetails" @cancel="cancelWordDetails"/>
            </div>
            <div class="word-actions">
              <!-- <router-link :to="'/words/' + word.id" class="action-button">View</router-link> -->
              <button @click="showDetails(word.id)" class="action-button">View</button>
              <button @click="confirmDeleteWord(word.id)" class="action-button">
                Delete
              </button>
              <!-- <button class="action-button" @click="playSound(word.word)">📢</button> -->
            </div>
            <DeleteWord :show="selectedWordId" :wordId="selectedWordId" @delete="deleteWord" @cancel="cancelDeleteWord" />
          </li>
        </ul>
      </div>
    </main>
  </div>
</template>

<script>
import WordForm from "./WordForm.vue";
import WordDetails from "./modals/WordDetails.vue";
import DeleteWord from "./modals/DeleteWord.vue";

export default {
  components: {
    WordForm,
    WordDetails,
    DeleteWord,
  },
  data() {
    return {
      showForm: false,
      showWordDetails: null,
      selectedWordId: null,
      voicesLoaded: false,
    };
  },
  computed: {
    words() {
      return this.$store.state.words;
    },
  },
  mounted() {
    this.$store.dispatch("fetchWords");
    this.loadVoices();
  },
  methods: {
    showDetails(wordId) {
      this.showWordDetails = wordId;
    },
    confirmDeleteWord(wordId) {
      this.selectedWordId = wordId;
    },
    deleteWord() {
      this.$store.dispatch("deleteWord", this.selectedWordId);
      this.selectedWordId = null;
    },
    cancelDeleteWord() {
      this.selectedWordId = null;
    },
    cancelWordDetails() {
      this.showWordDetails = null;
    },
    async loadVoices() {
      return new Promise((resolve) => {
        window.speechSynthesis.onvoiceschanged = () => {
          this.voicesLoaded = true;
          resolve();
        };
      });
    },
    async playSound(text) {
      if (!this.voicesLoaded) {
        await this.loadVoices();
      }

      const synthesis = window.speechSynthesis;
      const voices = synthesis.getVoices();
      const britishVoice = voices.find((voice) => voice.lang === "en-GB");

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.voice = britishVoice;

      synthesis.speak(utterance);
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: Arial, sans-serif;
  color: #333;
}

.header {
  text-align: center;
  padding: 20px;
  background-color: #f0f0f0;
}

.h1 {
  font-size: 24px;
  margin: 0;
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.words-list {
  flex: 1;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-bottom: 20px;
}

.word-card {
  width: 50vw;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 20px;
  display: flex;
}

.word-content {
  flex: 1;
}

.word-actions {
  display: flex;
  justify-content: flex-end;
  .action-button {
    margin-right: 10px;
  }
}

.action-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #f0f0f0; 
  color: #333;  
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  text-align: center;
}

.action-button:hover {
  background-color: #ddd; 
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.05);
  z-index: 100;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  text-align: center;
}

.actions {
  display: flex;
  justify-content: space-around;
}
</style>
