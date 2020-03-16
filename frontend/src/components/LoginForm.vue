<template>
  <v-card class="elevation-8 mt-10 mx-auto" width="350px">
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>
        <h3>Login</h3>
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text class="pa-3 my-4">
      <v-form ref="form" lazy-validation>
        <v-text-field
          class="my-3"
          v-model="username"
          :rules="nameRules"
          label="Username"
          prepend-icon="mdi-account-circle"
          required
        ></v-text-field>
        <v-text-field
          class="mt-7"
          v-model="password"
          :rules="passwordRules"
          type="password"
          label="Password"
          prepend-icon="mdi-lock"
          append-icon="mdi-eye-off"
          required
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="pa-4">
      <v-spacer></v-spacer>
      <v-btn color="normal" :to="'/'" text>Back</v-btn>
      <v-btn color="primary" v-on:click="login()">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      nameRules: [
        v => !!v || 'Username is required',
        v => v.length <= 20 || 'Username must be less than 20 characters'
      ],
      passwordRules: [
        v => !!v || 'Password is required',
        v => v.length > 7 || 'Password length is at least 8 characters',
        v => v.length <= 20 || 'Password length must be less than 20 characters'
      ]
    }
  },
  methods: {
    login () {
      const username = this.username
      const password = this.password
      this.$store
        .dispatch('login', { username, password })
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
</style>
