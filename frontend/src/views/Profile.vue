<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10">
    <v-row
      id="profile-table"
      class="headline font-weight-light my-3 mx-auto"
      v-for="(item, index) in this.userItems"
      v-bind:key="index"
      align="center"
      justify="center"
    >
      <v-col class="col-5">
        {{ item.title | capitalize }} :
      </v-col>
      <v-col class="col-6">
        {{ item.value }}
      </v-col>

    </v-row>
    <v-row
      class="mt-10"
      justify="center"
    >
        <v-btn
        color="grey lighten-2"
        :to="{ name: 'profile-edit', params: {userInfo: userInfo} }"
        x-large
        v-bind:userInfo="userInfo"
        depressed
        >Edit</v-btn>
        <div class="mx-8"></div>
        <back-btn color="grey" />
    </v-row>

  </v-container>
</template>

<script>
import BackButton from '@/components/BackButton'

export default {
  components: {
    'back-btn': BackButton
  },
  data () {
    return {
      userItems: [],
      userInfo: {}
    }
  },
  mounted () {
    this.extractUserInfo()
  },
  methods: {
    checkAuthentication: async function () {
      await this.$http.get(
        '/api/account/login/token/refresh'
      )
        .then((response) => {
          const access = response.data.access
          sessionStorage.setItem('at', access)
        })
        .catch(() => {
          this.$store.dispatch('logout').then(() => {
            if (this.$route.path !== '/index') {
              this.$router.push('/index')
            }
          })
        })
    },
    extractUserInfo: async function () {
      const res = await this.$http.get(
        '/api/account/profile/' + sessionStorage.username, {
          headers: {
            Authorization: `Bearer ${sessionStorage.getItem('at')}`
          }
        }
      ).catch(() => {
        this.$router.push({ name: 'index', params: {} })
      })
      this.userItems = [
        { title: 'username', value: sessionStorage.username },
        { title: 'first name', value: res.data.firstname },
        { title: 'last name', value: res.data.lastname },
        { title: 'email', value: res.data.email }
      ]
      this.userInfo = {
        username: res.data.username,
        firstname: res.data.firstname,
        lastname: res.data.lastname,
        email: res.data.email
      }
    },
    back () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
@media only screen and (max-width: 600px) {
  #profile-table {
    font-size: 1.2rem !important;
  }
}
</style>
