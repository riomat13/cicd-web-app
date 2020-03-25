<template>
  <v-app>
    <nav-bar v-bind:isScrolled="activateElevation" />
    <v-content v-scroll="onScroll" fluid>
      <router-view />
      <go-to-top
       v-if="this.$route.path!='/login'"
       v-bind:activated="activateGoToTop" />
    </v-content>
    <v-footer class="justify-center">
      <div class="text-center body-1 font-weight-regular my-2">
        &copy; {{ new Date().getFullYear() }} - <span id="footer-link"><img id="footer-icon" class="mx-2" :src="require('@/assets/media/images/github-mark-32px.png')" alt="" /><a href="https://github.com/riomat13/cicd-web-app">riomat13</a></span>
      </div>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import GoToTop from '@/components/GoToTop.vue'

export default {
  name: 'App',
  components: {
    'nav-bar': NavBar,
    'go-to-top': GoToTop
  },
  data () {
    return {
      activateGoToTop: false,
      activateElevation: false
    }
  },
  methods: {
    onScroll (entry) {
      if (typeof window !== 'undefined') {
        const top = window.pageYOffset || entry.target.scrollTop || 0
        this.activateGoToTop = top > window.innerHeight / 2
        this.activateElevation = top > 0
      }
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
