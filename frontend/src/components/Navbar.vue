<template>
  <div class="navbar">
    <div @click="$router.push('/')">Pardo</div>
    <div class="navbar__btns">
      <button @click="$router.push('/')" class="action-button">Words</button>
      <button style="margin-left: 20px" @click="$router.push('/groups')" class="action-button">
        Groups
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
