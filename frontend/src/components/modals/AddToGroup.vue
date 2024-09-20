<template>
  <div class="modal" v-if="show" @click="$emit('exit')">
    <div class="modal-content" @click.stop>
      <p>Are you sure you want to join?</p>
      <form @submit.prevent="submitForm">
        <input
          v-focus
          v-model="groupId"
          type="text"
          placeholder="Group ID"
          required
        />
        <div class="actions">
            <button class="action-button" type="submit">Submit</button>
            <button @click="$emit('exit')" class="action-button">Exit</button>
        </div>
    </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
  },
  data() {
    return {
      groupId: "",
    };
  },
  methods: {
    submitForm() {
      const formData = {
        group_id: this.groupId,
      };
      this.$store.dispatch("addToGroup", formData);
      this.groupId = "";
    },
  },
};
</script>

<style scoped>
input {
  width: 200px;
  height: 40px;
  margin: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #fff;
  color: #000;

  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.2);
}

.actions {
  display: flex;
  justify-content: space-around;
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
  background-color: rgba(0, 0, 0, 0.5);
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
</style>
