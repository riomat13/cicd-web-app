<template>
    <v-app-bar
      v-if="!$route.meta.hideNavigation"
      class="white"
      height="75"
      :elevation="isScrolled ? 6 : 0"
      app
    >
    <router-link to="/" id="logo">
      <v-toolbar-title
        class="headline
               pa-4
               font-italic
               font-weight-regular"
      >
        CI/CD Blog App
      </v-toolbar-title></router-link>
      <v-spacer></v-spacer>
      <v-toolbar-items id="nav-bar-items">
        <v-btn
          class="px-7 grey--text text--darken-3"
          text
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path"
        >{{ item.title }}</v-btn>
        <v-btn
          text
          v-if="!isAuthenticated"
          :key="loginSet.title"
          :to="loginSet.path"
        >Login</v-btn>
        <v-menu v-else open-on-click offset-y>
          <template v-slot:activator="{ on }">
            <v-btn
              class="grey--text text--darken-3"
              text
              v-on="on"
            ><v-icon>arrow_drop_down</v-icon>Account</v-btn>
          </template>
          <v-list elevation="2">
            <v-list-item to="/account/profile">
              <v-list-item-title
              ><v-icon>account_box</v-icon> Profile</v-list-item-title>
            </v-list-item>
            <v-list-item to="/account/settings">
              <v-list-item-title
              ><v-icon>settings</v-icon> Settings</v-list-item-title>
            </v-list-item>
            <v-divider class="mx-2"></v-divider>
            <v-list-item @click.stop="loggingOut = true">
              <v-list-item-title><v-icon>exit_to_app</v-icon> Logout</v-list-item-title>
            </v-list-item>
          </v-list>
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
        </v-menu>
      </v-toolbar-items>
    </v-app-bar>
</template>

<script>
export default {
  props: ['isScrolled'],
  data () {
    return {
      menuItems: [
        { title: 'Home', path: '/index' },
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
      this.loggingOut = false
      this.$store.dispatch('logout').then(() => {
        if (this.$route.path !== '/index') {
          this.$router.push('/index')
        }
      })
    }
  }
}
</script>

<style scoped>
#logo {
  color: #424242;
  text-decoration: none;
}
</style>
