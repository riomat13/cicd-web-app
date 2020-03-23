<template>
  <v-btn
    class="mr-5 mb-5"
    v-scroll="onScroll"
    v-show="isScrolled"
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
</template>

<script>
export default {
  data () {
    return {
      isScrolled: false
    }
  },
  methods: {
    goToTop () {
      this.$vuetify.goTo(0)
    },
    onScroll (entry) {
      if (typeof window !== 'undefined') {
        const top = window.pageYOffset || entry.target.scrollTop || 0
        this.isScrolled = top > window.innerHeight / 2
      }
    }
  }
}
</script>
