<template>
  <v-btn
    class="mr-5 mb-5"
    v-show="activated"
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
  props: ['activated'],
  methods: {
    goToTop () {
      this.$vuetify.goTo(0)
    }
  }
}
</script>
