<template>
  <div>
    <h2>All Together</h2>
    <router-link class="button" to="/training">Exit</router-link>

    <Cards v-if="currentTraining === 'cards'" :words="randomWords" />
    <WordTranslate v-if="currentTraining === 'wordTranslate'" :words="randomWords" />
    <Constructor v-if="currentTraining === 'constructor'" :words="randomWords" />
    <WordAudio v-if="currentTraining === 'wordAudio'" :words="randomWords" />
    
    
    <br />
    <button @click="nextTraining" v-if="currentTraining !== 'completed'"  class="action-button">Next Training</button>

  </div>
</template>

<script>
import Cards from "./Cards.vue";
import WordTranslate from "./WordTranslate.vue";
import Constructor from "./Constructor.vue";
import WordAudio from "./WordAudio.vue";

export default {
  components: { Cards, WordTranslate, Constructor, WordAudio },
  data() {
    return {
      currentTraining: 'cards',
    }
  },
  mounted() {
    this.$store.dispatch("fetchWords");
  },
  computed: {
    randomWords() {
      const shuffledWords = this.shuffleArray(this.$store.getters.unlearnedWords);
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
    nextTraining() {
      switch (this.currentTraining) {
        case 'cards':
          this.currentTraining = 'wordTranslate';
          break;
        case 'wordTranslate':
          this.currentTraining = 'constructor';
          break;
        case 'constructor':
          this.currentTraining = 'wordAudio';
          break;
        case 'wordAudio':
          this.currentTraining = 'completed';
          break;
        default:
          break;
      }
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
</style>
