<template>
    <div class="word-form">
        <h5>Add Word:</h5>
        <form @submit.prevent="submitForm">
            <input v-focus v-model="word" type="text" placeholder="Word" required/>
      
            <input v-model="definition" type="text" placeholder="Definition" required/>
            <button type="submit" class="action-button">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            word: '',
            definition: ''
        };
    },
    methods: {
        submitForm() {
            const formData = {
                word: this.word,
                definition: this.definition
            };
            this.$store.dispatch('addWord', formData);
            this.word = '';
            this.definition = '';
        }
  }
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
}

input {
  width: 100%;
  border: 2px solid #007BFF;
  padding: 10px 15px;
  margin-top: 15px;
}

button {
    align-self: flex-end;
    margin-top: 15px;
    padding: 5px 10px;
    background-color: none;
    color: #007BFF;
    border: 1px solid #007BFF;
}

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