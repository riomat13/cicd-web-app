<template>
  <v-app>
    <v-app-bar class="deep-purple" app>
      <v-toolbar-title class="headline">CI/CD Practice App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn
          text
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          {{ item.title }}
        </v-btn>
        <v-btn text v-if="!loggedin" @click="loggedin=!loggedin">Login</v-btn>
        <v-btn text v-else @click="loggedin=!loggedin">Logout</v-btn>
      </v-toolbar-items>
    </v-app-bar>

    <v-content fluid>
      <div class="content">
        <router-view />
      </div>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      loggedin: false,
      menuItems: [
        { title: 'Home', path: '/' },
        { title: 'About', path: '/about' },
        { title: 'Blog', path: '/blog' }
      ]
    }
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
