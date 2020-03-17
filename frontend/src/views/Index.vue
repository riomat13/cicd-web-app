<template>
  <div class="index-content">
    <h1 class="display-3 font-light" v-if="this.$store.getters.isLoggedIn" >Hello {{ username }}!</h1>
    <h1 class="display-3 font-light" v-else>Top page</h1>
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
