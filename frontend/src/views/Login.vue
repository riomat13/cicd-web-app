<template>
  <v-container id="login-form-container" fill-height>
    <v-row align="center" justify="center">
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
