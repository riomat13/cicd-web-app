<template>
  <v-card class="mx-auto col-8" max-width="500" flat>
    <v-toolbar flat>
      <v-toolbar-title class="pa-2 mb-3">
        <h1 class="display-2 font-weight-regular blue--text">Login</h1>
      </v-toolbar-title>
    </v-toolbar>
    <v-alert
      class="ma-5 body-2"
      v-if="invalidInput"
      border="top"
      colored-border
      type="error"
      elevation=2
    >
      Wrong username and/or password
    </v-alert>
    <v-alert
      class="ma-5 body-2"
      v-if="this.$store.getters.isLoggedIn"
      border="top"
      colored-border
      type="info"
      elevation=2
    >
      You are already logged in
    </v-alert>
    <v-card-text class="pa-2 my-4">
      <v-form ref="form" lazy-validation>
        <v-text-field
          class="my-3"
          v-model="username"
          :rules="nameRules"
          :disabled="this.$store.getters.isLoggedIn"
          label="Username"
          prepend-icon="mdi-account-circle"
          required
        ></v-text-field>
        <v-text-field
          class="mt-7"
          v-model="password"
          :rules="passwordRules"
          :disabled="this.$store.getters.isLoggedIn"
          type="password"
          label="Password"
          append-icon="mdi-eye-off"
          prepend-icon="mdi-lock"
          required
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="my-4">
      <v-row align="center" justify="center">
        <v-col class="col-10">
          <v-btn
            color="primary"
            height="45"
            v-on:click="login()"
            :disabled="!(validUsername && validPassword)"
            block
          >Login</v-btn>
        </v-col>
        <v-col class="col-10">
          <v-btn
            color="normal"
            height="45"
            v-on:click="back()"
            text
            block
          >Back</v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      validUsername: false,
      validPassword: false,
      invalidInput: false,
      nameRules: [
        v => !!v || 'Username is required',
        v => v.length > 4 || 'Username must be at least 5 characters',
        v => v.length <= 20 || 'Username must be less than 20 characters'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => v.length > 7 || 'Password length is at least 8 characters',
        v => v.length <= 20 || 'Password length must be less than 20 characters'
      ]
    }
  },
  watch: {
    username: function (username) {
      if (username.length > 4 && username.length < 21) {
        this.validUsername = true
      } else {
        this.validUsername = false
      }
    },
    password: function (password) {
      if (password.length > 7 && password.length < 21) {
        this.validPassword = true
      } else {
        this.validPassword = false
      }
    }
  },
  methods: {
    login () {
      const self = this
      const username = this.username
      const password = this.password
      this.$store
        .dispatch('login', { username, password })
        .then(() => this.$router.push('/index'))
        .catch(function (err) {
          self.invalidInput = err !== null // how to handle error?
        })
    },
    back () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
</style>
