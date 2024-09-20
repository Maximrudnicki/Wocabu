<template>
  <div>
    <br>
    <router-link class="button" :to="'/groups/' + groupId">Back</router-link>

    <strong style="font-size: 24px; margin-left: 20px;" v-if="stats">{{stats.student.username}}, 
      {{stats.student.email}} - Statistics</strong>
    <br />
    <div class="word-form" v-if="showForm">
      <br>
      <h5>Add Word:</h5>
      <form @submit.prevent="submitForm">
        <input v-focus v-model="word" type="text" placeholder="Word" required />

        <input
          v-model="definition"
          type="text"
          placeholder="Definition"
          required
        />
        <button type="submit" class="action-button">Submit</button>
      </form>
    </div>
    <button v-if="!showForm" @click="showForm = true" class="action-button">
      Add Word
    </button>
    <button v-if="showForm" @click="showForm = false" class="action-button">
      Close
    </button>
  </div>

  <div v-if="stats">
    <table class="word-table">
      <thead>
        <tr>
          <th>Word</th>
          <th>Definition</th>
          <th>Learned</th>
          <th>Cards</th>
          <th>Translation</th>
          <th>Constructor</th>
          <th>Audio</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="word in stats.words" :key="word.id">
          <td>{{ word.word }}</td>
          <td>{{ word.definition }}</td>
          <td :class="{
            'is-true': word.is_learned,
            'is-false': !word.is_learned
          }">{{ word.is_learned }}</td>
          <td :class="{
            'is-true': word.cards,
            'is-false': !word.cards
          }">{{ word.cards }}</td>
          <td :class="{
            'is-true': word.word_translation,
            'is-false': !word.word_translation
          }">{{ word.word_translation }}</td>
          <td :class="{
            'is-true': word.constructor,
            'is-false': !word.constructor
          }">{{ word.constructor }}</td>
          <td :class="{
            'is-true': word.word_audio,
            'is-false': !word.word_audio
          }">{{ word.word_audio }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <br />
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
      groupId: this.$route.params.id,
      studentId: this.$route.params.student,
      word: "",
      definition: "",
      stats: null,
    };
  },
  mounted() {
    const formData = {
      group_id: this.groupId,
      student_id: parseInt(this.studentId),
    };
    const statsPromise = this.$store.dispatch("fetchStats", formData);
    statsPromise.then((statsDetails) => {
      this.stats = statsDetails;
    });
  },
  methods: {
    submitForm() {
      const formData = {
        word: this.word,
        definition: this.definition,
        group_id: this.groupId,
        user_id: parseInt(this.studentId),
      };
      this.$store.dispatch("addWordToStudent", formData);
      this.word = "";
      this.definition = "";
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

button {
  align-self: flex-end;
  margin-top: 15px;
  padding: 5px 10px;
  background-color: none;
  color: teal;
  border: 1px solid teal;
}

.word-table {
  margin: 20px auto;
  width: 80%;
  border-collapse: collapse;
}

table {
  width: 100%;
  border: 1px solid #ddd;
}

th, td {
  padding: 8px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f0f0f0;
  font-weight: bold;
}

tbody tr:nth-child(odd) {
  background-color: #fff;
}

tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}

.is-true {
  background-color: lightgreen;
}

.is-false {
  background-color: lightcoral;
}
</style>
