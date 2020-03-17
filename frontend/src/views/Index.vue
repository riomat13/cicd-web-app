<template>
  <div class="index-content">
    <h1 v-if="this.$store.getters.isLoggedIn" >Hello {{ username }}!</h1>
    <h1 v-else class="content-title">Top page</h1>
  </div>
</template>

<script>
export default {
  name: 'Top',
  data () {
    return {
      username: ''
    }
  },
  mounted () {
    if (localStorage.username) {
      this.username = localStorage.username
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
