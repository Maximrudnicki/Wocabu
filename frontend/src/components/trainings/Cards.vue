<template>
  <div>
    <h2>Cards</h2>
    <router-link class="button" to="/training" v-if="!this.words" @click="submitResult">Exit</router-link>

    <div v-if="currentWord" style="margin-top: 10px;">
      <p>
        <strong>{{ currentWord.word }} </strong> -
        <span v-if="isAnswerSubmitted">{{ currentWord.definition }}</span>
      </p>
      <button @click="checkWord" v-if="!isAnswerSubmitted" class="action-button">Check</button>
      <button @click="nextWord" v-if="isAnswerSubmitted" class="action-button">Next</button>
    </div>
    <div v-else>
      <p>No more words</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    words: {
      type: Array,
      required: false,
    },
  },
  data() {
    return {
      currentIndex: 0,
      isAnswerSubmitted: false,
      result: [],
    };
  },
  mounted() {
    if (!this.words) {
      this.$store.dispatch("fetchWords");
    }
  },
  computed: {
    currentWord() {
      return this.randomWords[this.currentIndex];
    },
    randomWords() {
      let shuffleWords;
      if (this.words) {
        shuffleWords = this.shuffleArray(this.words);
      } else {
        shuffleWords = this.shuffleArray(this.$store.state.words);
      }
      const shuffledWords = shuffleWords;
      return shuffledWords.slice(0, 5);
    },
  },
  methods: {
    shuffleArray(array) {
      const shuffledArray = array.slice();
      for (let i = shuffledArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledArray[i], shuffledArray[j]] = [
          shuffledArray[j],
          shuffledArray[i],
        ];
      }
      return shuffledArray;
    },
    checkWord() {
      this.isAnswerSubmitted = true;
      const wordId = this.currentWord.id;
      this.result.push({ word_id: wordId, is_learned: true });
      this.playSound();
    },
    playSound() {
      const synthesis = window.speechSynthesis;
      const voices = synthesis.getVoices();
      const selectedVoice = voices.find((voice) => voice.lang === "en-GB");

      const utterance = new SpeechSynthesisUtterance(this.currentWord.word);
      utterance.voice = selectedVoice;

      synthesis.speak(utterance);
    },
    nextWord() {
      if (this.currentIndex < this.$store.state.words.length - 1) {
        this.currentIndex++;
        this.isAnswerSubmitted = false;
        this.submitResult();
      } else {
        this.currentIndex = 0;
      }
    },
    submitResult() {
      if (this.result.length === 5) {
        const token = localStorage.getItem("token");
        const config = {
          headers: { Authorization: `Bearer ${token}` },
        };
        for (let i = 0; i < this.result.length; i++) {
          const formData = {
            cards: this.result[i].is_learned,
          };
          axios.patch(
            `/api/v1/vocab/${this.result[i].word_id}`,
            formData,
            config
          );
        }
        // this.$emit("trainingCompleted");
      }
    },
  },
};
</script>

<style scoped>
.action-button {
  background-color: #fff;
  border: none;
  color: #007BFF;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid #007BFF;
}

.button {
  background-color: #fff;
  border: none;
  color: #007BFF;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  border: 1px solid #007BFF;
  text-decoration: none;
}

.button:hover {
  background-color: #f0f0f0;
}
.action-button:hover {
  background-color: #f0f0f0;
}
</style>
