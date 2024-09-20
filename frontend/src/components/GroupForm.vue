<template>
  <div class="group-form">
    <h5>Add: </h5>
    <form @submit.prevent="submitForm">
      <input v-focus v-model="title" type="text" placeholder="Title" required />
      <button type="submit" class="action-button">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "",
    };
  },
  methods: {
    submitForm() {
      const formData = {
        title: this.title,
      };
      this.$store.dispatch("addGroup", formData);
      this.title = "";
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
