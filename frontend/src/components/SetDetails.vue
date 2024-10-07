<template>
  <div>
    <p></p>
    <router-link class="button" to="/sets/">Back</router-link>
    <button
      v-if="!showAddWord"
      style="margin-left: 10px"
      @click="showAddWord = true"
      class="button"
    >
      Add Word
    </button>
    <button
      v-if="showAddWord"
      style="margin-left: 10px"
      @click="showAddWord = false"
      class="button"
    >
      Close
    </button>
    <AddToSet v-if="showAddWord" />
    <div v-if="set">
      <p>
        <strong style="font-size: 20px">{{ set.name }}</strong>
        <span style="margin-left: 20px; font-size: 18px">{{ set._id }}</span>
      </p>
      <div class="words-list">
        <ul>
          <li v-for="word in set.words" :key="word.id" class="word-card">
            <div class="word-content">
              <strong>{{ word.word }}</strong>
              <p>{{ word.definition }}</p>
              <WordDetails
                :word="word"
                :show="showWordDetails"
                @cancel="cancelWordDetails"
              />
            </div>
            <div class="word-actions">
              <!-- <router-link :to="'/words/' + word.id" class="action-button">View</router-link> -->
              <button @click="showDetails(word.id)" class="action-button">
                View
              </button>
              <button @click="confirmRemoveWord(word.id)" class="action-button">
                Remove
              </button>
              <!-- <button class="action-button" @click="playSound(word.word)">📢</button> -->
            </div>
            <RemoveFromSet
              :show="selectedWordId"
              :wordId="selectedWordId"
              @delete="removeWordFromSet(set._id)"
              @cancel="cancelDeleteWord"
            />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import WordDetails from "./modals/WordDetails.vue";
import RemoveFromSet from "./modals/RemoveFromSet.vue";
import AddToSet from "./AddToSet.vue";

export default {
  components: {
    WordDetails,
    RemoveFromSet,
    AddToSet,
  },
  data() {
    return {
      showForm: false,
      showAddWord: false,
      showWordDetails: null,
      selectedWordId: null,
      voicesLoaded: false,
    };
  },
  mounted() {
    this.$store.dispatch("fetchSet", this.$route.params.id);
  },
  computed: {
    set() {
      return this.$store.state.set;
    },
  },
  methods: {
    showDetails(wordId) {
      this.showWordDetails = wordId;
    },
    confirmRemoveWord(wordId) {
      this.selectedWordId = wordId;
    },
    removeWordFromSet(setId) {
      const formData = {
        setId: setId,
        wordId: this.selectedWordId,
      };
      this.$store.dispatch("removeWordFromSet", formData);
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
.action-button {
  background-color: #fff;
  border: none;
  color: teal;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid teal;
}

.button {
  background-color: #fff;
  border: none;
  color: teal;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid teal;
  text-decoration: none;
}

.button:hover {
  background-color: #f0f0f0;
}
.action-button:hover {
  background-color: #f0f0f0;
}
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
