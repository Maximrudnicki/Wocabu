<template>
  <div>
    <h2>Words Training</h2>

    <router-link class="button" to="/training/all-together">All together</router-link>
    <p></p>
    <router-link class="button" to="/training/cards">Cards</router-link>
    <p></p>
    <router-link class="button" to="/training/word-translate">Word - Translation</router-link>
    <p></p>
    <router-link class="button" to="/training/constructor">Constructor</router-link>
    <p></p>
    <router-link class="button" to="/training/word-audio">Word Audio</router-link>
  </div>
</template>

<script>
export default {};
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
