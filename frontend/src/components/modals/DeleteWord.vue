<template>
  <div class="modal" v-if="show" @click="$emit('cancel')">
    <div class="modal-content" @click.stop>
      <p>Are you sure you want to delete this word?</p>
      <div class="actions">
        <button @click="$emit('delete')" class="action-button">OK</button>
        <button @click="$emit('cancel')" class="action-button">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    wordId: Number,
  },
};
</script>

<style scoped>
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
</style>
