<template>
  <v-app>
    <navBar v-if="this.$route.path!='/'" />
    <v-content fluid>
      <div class="content">
        <router-view ref="chileComponent" />
      </div>
    </v-content>
    <v-btn
      v-show="isIntersecting"
      fab
      dark
      fixed
      bottom
      right
      color="pink"
      @click="goToTop"
    >
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
    <v-footer class="justify-center">
      <div class="text-center body-1 font-weight-regular my-2">
        &copy; {{ new Date().getFullYear() }} - <span id="footer-link"><img id="footer-icon" class="mx-2" :src="require('@/assets/media/images/github-mark-32px.png')" alt="" /><a href="https://github.com/riomat13/cicd-web-app">riomat13</a></span>
      </div>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    navBar: NavBar
  },
  data () {
    return {
      isIntersecting: false
    }
  },
  methods: {
    goToTop () {
      this.$vuetify.goTo(0)
    },
    onIntersect (entries, observer) {
      this.isIntersecting = entries[0].isIntersecting
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
}
#footer-link a {
  color: black;
  text-decoration: underline;
}
#footer-icon {
  transform: translateY(3px);
  height: 17px;
  display: inline-block;
}
</style>
