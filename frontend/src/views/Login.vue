<template>
  <v-container>
    <v-row align="center" justify="center" height="100%">
      <login-form />
    </v-row>
  </v-container>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'
export default {
  components: {
    'login-form': LoginForm
  }
}
</script>

<style scoped>
</style>
