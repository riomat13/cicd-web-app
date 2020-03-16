<template>
  <v-app>
    <navBar />
    <v-content fluid>
      <div class="content">
        <router-view />
      </div>
    </v-content>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    navBar: NavBar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.content-title {
  margin: 10px;
}
.content {
  margin: 0;
  padding: 40px;
}
</style>
