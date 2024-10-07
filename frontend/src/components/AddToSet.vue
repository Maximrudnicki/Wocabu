<template>
  <div class="set-form">
    <h5>Add:</h5>
    <form @submit.prevent="submitForm">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search for a word"
        @input="filterWords"
        required
      />

      <!-- Dropdown for filtered words -->
      <ul v-if="filteredWords.length" class="suggestions-list">
        <li
          v-for="word in filteredWords"
          :key="word.id"
          @click="selectWord(word)"
          class="suggestion-item"
        >
          {{ word.word }} ({{ word.definition }})
        </li>
      </ul>

      <button type="submit" class="action-button">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "", // stores search input
      filteredWords: [], // stores filtered suggestions
      selectedWord: null, // stores selected word object
    };
  },
  mounted() {
    this.$store.dispatch("fetchWords");
  },
  computed: {
    words() {
      return this.$store.state.words;
    },
  },
  methods: {
    filterWords() {
      if (this.searchQuery.trim() === "") {
        this.filteredWords = [];
        return;
      }

      const query = this.searchQuery.toLowerCase();
      this.filteredWords = this.words.filter(
        (word) =>
          word.word.toLowerCase().includes(query) ||
          word.definition.toLowerCase().includes(query)
      );
    },
    selectWord(word) {
      this.selectedWord = word;
      this.searchQuery = word.word; // display selected word in input field
      this.filteredWords = []; // hide suggestions after selection
    },
    async submitForm() {
      if (this.selectedWord) {
        const formData = {
          wordId: this.selectedWord.id,
          setId: this.$route.params.id, // assuming set ID is passed in the route
        };
        try {
          await this.$store.dispatch("addToSet", formData);
          this.searchQuery = "";
          this.selectedWord = null;
        } catch (error) {
          console.error("Failed to add word to the set", error);
        }
      } else {
        alert("Please select a word from the suggestions.");
      }
    },
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

input {
  width: 100%;
  border: 2px solid teal;
  padding: 10px 15px;
  margin-top: 15px;
}

.suggestions-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  border: 1px solid #ccc;
  max-height: 150px;
  overflow-y: auto;
  background-color: white;
}

.suggestion-item {
  padding: 10px;
  cursor: pointer;
}

.suggestion-item:hover {
  background-color: #f0f0f0;
}

button {
  align-self: flex-end;
  margin-top: 15px;
  padding: 5px 10px;
  background-color: none;
  color: teal;
  border: 1px solid teal;
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

.action-button:hover {
  background-color: #f0f0f0;
}
</style>
