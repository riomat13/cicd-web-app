<template>
  <v-content>
    <v-parallax
      v-resize="onResize"
      dark
      :src="require('@/assets/media/images/home1.jpg')"
      :height="windowSize.y"
      jumbotoron
    >
      <v-row align="center" justify="center">
        <v-col class="top-title text-md-left text-center">
          <h1 class="display-3 font-light" v-if="this.$store.getters.isLoggedIn">Hello {{ username }}!</h1>
          <h1 class="display-3 font-light" v-else>Top page</h1>
        </v-col>
      </v-row>
    </v-parallax>
    <section id="about">
      <div class="py-12"></div>

      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">About</h2>
        <div class="py-4"></div>
        <v-responsive class="mx-auto title font-weight-light mb-8">
          This is a sample blog app developed to learn CI/CD process.
        </v-responsive>
        <v-btn color="grey" href="/about/" outlined large>
          <span class="grey--text text--darken-1 font-weight-bold">
            Go to About page
          </span>
        </v-btn>
      </v-container>

      <div class="py-12"></div>
    </section>

    <section
      id="tools"
      class="grey lighten-3"
    >
      <div class="py-12"></div>

      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">Tools</h2>
      </v-container>

      <v-row class="px-10">
        <v-col
          v-for="tool in tools"
          :key="tool.title"
          cols="12"
          md="4"
        >
          <v-card class="py-12 px-4 text-center" color="grey lighten-5" flat>
            <v-card-title class="justify-center font-weight-black"
              v-text="tool.title"
            ></v-card-title>

            <v-card-text class="subtitle-1" v-text="tool.text"></v-card-text>
            <v-btn color="grey" :href="tool.link" outlined>
              <span class="grey--text text--darken-1 font-weight-bold">Link</span>
            </v-btn>
          </v-card>
        </v-col>
      </v-row>

      <div class="py-12"></div>
    </section>

    <section id="img-div">
      <v-parallax
        :height="$vuetify.breakpoint.smAndDown ? 700 : 500"
        :src="require('@/assets/media/images/home2.jpg')"
      ></v-parallax>
    </section>

    <section id="features">
      <div class="py-12"></div>

      <v-container class="text-center">
        <h2 class="display-2 font-weight-bold mb-3">Features</h2>
      </v-container>

      <v-container class="text-center">
        <blockquote class="title font-weight-light pd-3">
          As a web app, following features are implemented.
        </blockquote>
      </v-container>

      <v-container
        v-for="(feature, index) in features"
        :key="feature.title"
        class="col-xl-6 col-lg-7 col-9"
      >
        <v-divider class="my-4"></v-divider>
        <v-row
          justify="space-around"
          class="pa-6"
          v-if="index%2==0"
          no-gutters
        >
          <v-col class="text-center" cols="3">
            <v-icon class="pa-3 mb-2" x-large>{{ feature.icon }}</v-icon>
            <h3 class="headline font-weight-regular">{{ feature.title }}</h3>
          </v-col>
          <v-col cols="6">
            <blockquote class="py-3">{{ feature.text }}</blockquote>
            <v-btn v-if="feature.path" :href="feature.path" text>>> Go to {{ feature.linkname }}</v-btn>
          </v-col>
        </v-row>

        <v-row
          justify="space-around"
          class="pa-4"
          v-else
          no-gutters
        >
          <v-col cols="6">
            <blockquote class="py-3">{{ feature.text }}</blockquote>
            <v-btn v-if="feature.path" :href="feature.path" text>>> Go to {{ feature.linkname }}</v-btn>
          </v-col>
          <v-col class="text-center" cols="3">
            <v-icon class="pa-3 mb-2" x-large>{{ feature.icon }}</v-icon>
            <h3 class="headline font-weight-regular">{{ feature.title }}</h3>
          </v-col>
        </v-row>
      </v-container>
      <div class="py-12"></div>
    </section>
    <go-to-top />

  </v-content>
</template>

<script>
import GoToTop from '@/components/GoToTop.vue'

export default {
  name: 'Top',
  components: {
    'go-to-top': GoToTop
  },
  data () {
    return {
      username: '',
      windowSize: {
        x: window.innerWidth,
        y: window.innerHeight
      },
      tools: [
        {
          title: 'Django',
          link: 'https://www.djangoproject.com/',
          text: 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.'
        },
        {
          title: 'Vue.js/Vuetify',
          link: 'https://vuetifyjs.com/en/',
          text: 'Vuetify is a Vue UI Library with beautifully handcrafted Material Components. No design skills required — everything you need to create amazing applications is at your fingertips.'
        },
        {
          title: 'Jenkins Blue Ocean?',
          link: 'https://jenkins.io/projects/blueocean/',
          text: 'Blue Ocean puts Continuous Delivery in reach of any team without sacrificing the power and sophistication of Jenkins.'
        }
      ],
      features: [
        {
          title: 'Blog',
          path: '/blog/',
          linkname: 'blog page',
          icon: 'create',
          text: 'Lorem ipsum dolor sit amet, reque integre aliquando mei ne, perfecto honestatis at nec. Alii atqui an has, et has nisl case velit, posse latine nam et.'
        },
        {
          title: 'Authentication',
          path: '/login',
          linkname: 'login page',
          icon: 'security',
          text: 'Lorem ipsum dolor sit amet, reque integre aliquando mei ne, perfecto honestatis at nec. Alii atqui an has, et has nisl case velit, posse latine nam et.'
        },
        {
          title: 'API',
          path: '',
          linkname: '',
          icon: 'sync',
          text: 'Lorem ipsum dolor sit amet, reque integre aliquando mei ne, perfecto honestatis at nec. Alii atqui an has, et has nisl case velit, posse latine nam et.'
        }
      ]
    }
  },
  mounted () {
    this.onResize()

    if (localStorage.username) {
      this.username = localStorage.username
    }
  },
  methods: {
    onResize () {
      this.windowSize = { x: window.innerWidth, y: window.innerHeight }
    }
  }
}
</script>

<style scoped>
.top-title {
  padding-left: 10%;
}
</style>
