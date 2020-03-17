<template>
    <v-app-bar v-if="!$route.meta.hideNavigation" class="deep-purple" app>
      <v-toolbar-title class="headline">CI/CD Practice App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text v-for="item in menuItems" :key="item.title" :to="item.path">{{ item.title }}</v-btn>
        <v-btn text v-if="!isAuthenticated" :key="loginSet.title" :to="loginSet.path">Login</v-btn>
        <v-btn text v-else @click.stop="loggingOut = true">Logout</v-btn>
        <v-dialog v-model="loggingOut" max-width="300">
          <v-card>
            <v-card-title class="headline">Logout</v-card-title>
            <v-card-text>Are you sure to log out?</v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="loggingOut=false">Back</v-btn>
              <v-btn color="error" text @click="logout">Logout</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar-items>
    </v-app-bar>
</template>

<script>
export default {
  data () {
    return {
      menuItems: [
        { title: 'Home', path: '/' },
        { title: 'About', path: '/about' },
        { title: 'Blog', path: '/blog' }
      ],
      loginSet: { title: 'Login', path: '/login' },
      loggingOut: false
    }
  },
  computed: {
    isAuthenticated () {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout').then(() => {
        this.loggingOut = false
        if (this.$route.path !== '/') {
          this.$router.push('/')
        }
      })
    }
  }
}
</script>

<style>
</style>
