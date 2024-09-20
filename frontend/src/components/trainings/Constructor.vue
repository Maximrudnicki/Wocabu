<template>
  <div>
    <h2>Constructor</h2>
    <router-link  class="button" to="/training" v-if="!this.words" @click="submitResult">Exit</router-link>

    <div v-if="currentWord">
      <p style="font-size: 20px;">
        <strong>{{ currentWord.definition }} </strong> -
        <span v-if="isAnswerSubmitted">{{ currentWord.word }}</span>
      </p>
      <p>
        <span
          v-for="letter in displayWord"
          :key="letter"
          class="word-letter"
          :class="{
            'before-check': !isAnswerSubmitted,
            'is-correct': isCorrect,
            'is-incorrect': !isCorrect,
          }"
        >
          {{ letter }}
        </span>
      </p>
      <div>
        <button
          class="letter"
          v-for="(letter, index) in shuffledLetters"
          :key="index"
          @click="selectLetter(letter)"
        >
          {{ letter }}
        </button>
      </div>
      <button @click="checkAnswer" v-if="!isAnswerSubmitted" class="action-button">Check</button>
      <button @click="nextWord" v-if="isAnswerSubmitted" class="action-button">Next</button>
    </div>
    <div v-else>
      <p>No more words</p>
      <div>
        <h3>Result:</h3>
        <ul>
          <li v-for="(answer, index) in result" :key="index">
            {{ answer }}
          </li>
        </ul>
      </div>
      <!-- <button @click="submitResult">Submit Result</button> -->
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
      selectedLetters: [],
      result: [],
      isAnswerSubmitted: false,
      isCorrect: null,
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
    shuffledLetters() {
      const letters = this.shuffleArray(this.currentWord.word.split(""));
      return letters.filter((letter, index) => {
        return letters.indexOf(letter, index + 1) === -1;
      });
    },
    displayWord() {
      return this.selectedLetters.join("");
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
    selectLetter(letter) {
      this.selectedLetters.push(letter);
    },
    checkAnswer() {
      this.isAnswerSubmitted = true;
      const userAnswer = this.selectedLetters.join("");
      if (userAnswer === this.currentWord.word) {
        const wordId = this.currentWord.id;
        this.result.push({ word_id: wordId, is_learned: true });
        this.isCorrect = true;
      } else {
        const wordId = this.currentWord.id;
        this.result.push({ word_id: wordId, is_learned: false });
        this.isCorrect = false;
      }
    },
    nextWord() {
      if (this.currentIndex < this.$store.state.words.length - 1) {
        this.currentIndex++;
        this.selectedLetters = [];
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
            result: this.result[i].is_learned,
            training: "constructor",
          };
          axios.patch(
            `/api/v1/vocab/${this.result[i].word_id}/trainings`,
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
.letter {
  width: 40px;
  height: 40px;
  margin: 5px;
  padding: 10px;
  background-color: #d3d3d3;
  color: #000;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.letter:hover {
  background-color: #c2c2c2;
}
.word-letter {
  display: inline-block;
  width: 40px;
  height: 40px;
  margin: 5px;
  padding: 10px;
  background-color: #d3d3d3;
  color: #000;
  border: none;
  border-radius: 5px;
  text-align: center;

  &.is-correct {
    background-color: lightgreen;
  }

  &.is-incorrect {
    background-color: lightcoral;
  }

  &.before-check {
    background-color: #d3d3d3;
  }
}

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

</style>
