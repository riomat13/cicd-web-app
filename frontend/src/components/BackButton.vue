<template>
  <v-btn
    :color="color"
    @click="back"
    outlined
    x-large
  >Back</v-btn>
</template>

<script>
export default {
  props: ['color'],
  methods: {
    back () { this.$router.go(-1) }
  }
}
</script>
