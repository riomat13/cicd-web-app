<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10">
    <v-card class="mx-auto col-8" max-width="500" flat>
      <v-card-text>
        <v-alert
          v-if="is_submitted"
          type="info"
          outlined
        >Submission success
        </v-alert>
        <v-alert
          v-if="is_submit_error"
          type="error"
          outlined
        >Submission failed
        </v-alert>
        <v-form ref="form" lazy-validation>
          <v-text-field
            v-model="username"
            label="Username"
            :placeholder="username"
            readonly
          ></v-text-field>
          <v-text-field
            v-model="email"
            label="Email"
            :placeholder="email"
          ></v-text-field>
          <v-text-field
            v-model="firstname"
            label="First name"
            :placeholder="firstname"
          ></v-text-field>
          <v-text-field
            v-model="lastname"
            label="Last name"
            :placeholder="lastname"
          ></v-text-field>
        </v-form>
      </v-card-text>

    </v-card>
    <div class="my-12"></div>
    <v-row justify="center">
      <v-btn
        class="white--text"
        @click="confirm"
        color="indigo accent-2"
        x-large
        depressed
      >Update
      </v-btn>
      <div class="mx-12"></div>
      <back-btn color="grey" />
    </v-row>

  </v-container>
</template>

<script>
import BackButton from '@/components/BackButton'

export default {
  props: ['userInfo'],
  components: {
    'back-btn': BackButton
  },
  data () {
    return {
      username: this.userInfo ? this.userInfo.username : '',
      firstname: this.userInfo ? this.userInfo.firstname : '',
      lastname: this.userInfo ? this.userInfo.lastname : '',
      email: this.userInfo ? this.userInfo.email : '',
      is_submitted: false,
      is_submit_error: false
    }
  },
  mounted () {
    if (this.userInfo == null) {
      this.$router.push('/account/profile')
    } else if (this.userInfo.username == null) {
      this.$router.push('')
    }
  },
  methods: {
    confirm () {
      this.$http.put(
        `/api/account/profile/${this.username}/edit`,
        {
          data: {
            email: this.email,
            firstname: this.firstname,
            lastname: this.lastname
          },
          headers: {
            Authorization: `Bearer ${sessionStorage.getItem('at')}`
          }
        }
      ).then(() => {
        this.is_submitted = true

        const sleep = (milliseconds) => {
          return new Promise(resolve => setTimeout(resolve, milliseconds))
        }
        sleep(1000).then(() => {
          this.$router.push('/account/profile')
        })
      }).catch(() => {
        this.is_sibmit_error = true
      })
    }
  }
}
</script>
