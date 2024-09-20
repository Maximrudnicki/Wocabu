<template>
  <div class="modal" v-if="show" @click="$emit('cancel')">
    <div class="modal-content" @click.stop>
      <div >
        <strong>{{ this.word.word }}</strong
        >: {{ this.word.definition }}
      </div>

      <button class="action-button" @click="showForm = true">Edit</button>

      <div>
        <div class="actions" v-if="showForm">
          <select v-model="isLearned" @change="changeStatus">
            <option value="true">Learned</option>
            <option value="false">Not learned</option>
          </select>
          <form @submit.prevent="submitForm">
            <input
              v-model="definition"
              type="text"
              placeholder="Definition"
              required
            />
            <button type="submit" class="action-button">Submit</button>
          </form>
        </div>
      </div>
      <button class="action-button" @click="$emit('cancel')">Back</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    word: Object,
  },
  data() {
    return {
      showForm: false,
      definition: "",
      isLearned: null,
    };
  },
  methods: {
    submitForm() {
      const updatedWord = {
        id: this.word.id,
        definition: this.definition,
      };
      this.$store.dispatch("updateWord", updatedWord);
      this.showForm = false;
    },
    changeStatus() {
      if (this.isLearned === "true") {
        const updatedWordStatus = {
          id: this.word.id,
          is_learned: true,
        };
        this.$store.dispatch("updateWordStatus", updatedWordStatus);
      } else if (this.isLearned === "false") {
        const updatedWordStatus = {
          id: this.word.id,
          is_learned: false,
        };
        this.$store.dispatch("updateWordStatus", updatedWordStatus);
      }
    },
  },
  mounted() {},
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

button {
  align-self: flex-end;
  margin-top: 15px;
  padding: 5px 10px;
  background-color: none;
  color: teal;
  border: 1px solid teal;
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

.action-button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #f0f0f0; /* Change button background color if needed */
  color: #333; /* Change button text color if needed */
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none; /* Удалите подчеркивание */
  text-align: center; /* Выровняйте текст по центру */
}

.action-button:hover {
  background-color: #ddd; /* Change button hover color if needed */
}
</style>
