<template>
  <v-dialog>
    <v-card>
      <v-card-title>Login</v-card-title>
      <v-card-subtitle>Login session is expired.</v-card-subtitle>
      <v-form ref="form" lazy-evaluation>
        <v-text-field
          v-model="username"
          label="Username"
        ></v-text-field>
        <v-text-field
          v-model="password"
          label="Submit"
        ></v-text-field>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data () {
    return {
      username: sessionStorage.username,
      password: ''
    }
  }  
}
</script>
