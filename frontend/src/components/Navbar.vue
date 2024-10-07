<template>
  <div class="navbar">
    <div @click="$router.push('/')" class="logo-text">Wocabu</div>
    <div class="navbar__btns">
      <button @click="$router.push('/')" class="action-button">Words</button>
      <button style="margin-left: 20px" @click="$router.push('/sets')" class="action-button">
        Sets
      </button>
      <button style="margin-left: 20px" @click="$router.push('/training')" class="action-button">
        Training
      </button>
      <button style="margin-left: 20px" @click="$router.push('/about')" class="action-button">
        About
      </button>
      <button style="margin-left: 20px" @click="$router.push('/log-in')" class="action-button">
        LogIn
      </button>
      <button style="margin-left: 20px" @click="$router.push('/sign-up')" class="action-button">
        SignUp
      </button>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style scoped>
.navbar {
  height: 50px;
  background-color: lightgray;
  box-shadow: 2px 2px 4px gray;
  display: flex;
  align-items: center;
  padding: 0 15px;
}
.navbar__btns {
  margin-left: auto;
}
button {
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

.action-button:hover {
  background-color: #f0f0f0;
}

.logo-text {
  font-weight: bold;
  font-size: 1.5em;
  color: #007BFF;
  cursor: pointer;
}

.logo-text:hover {
  color: #0056b3;
}
</style>
