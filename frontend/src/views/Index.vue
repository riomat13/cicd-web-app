<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10" fill-height>
    <v-container class="pa-0 ma-0">
    <v-row>
      <h1 class="display-2 font-weight-light">Welcome to my page!</h1>
    </v-row>

    <v-row align="start" justify="start">
      <v-col>
      <v-card flat>
        <v-list-item
          class="col-6"
          two-line
          v-for="(page, index) in pages"
          v-bind:key="index"
          :to="page.path"
        >
          <v-list-item-content>
            <v-list-item-title class="headline font-light">
              {{ page.name }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ page.text }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card>
      </v-col>
    </v-row>
    </v-container>

  </v-container>
</template>

<script>
export default {
  data () {
    return {
      pages: [
        {
          name: 'Home',
          text: 'Navigation index page(current page)'
        },
        {
          name: 'About',
          text: 'Explanation of this application',
          path: '/about'
        },
        {
          name: 'Blog',
          text: 'Blogs for any topics, currently only random strings',
          path: '/blog/'
        },
        {
          name: 'Login/Logout',
          text: 'Sample authentication',
          path: '/login/'
        },
        {
          name: 'Others',
          text: 'Coming soon?'
        }
      ]
    }
  }
}
</script>
