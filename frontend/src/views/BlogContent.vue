<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10">
    <h1 class="display-2 font-weight-light mb-3">{{ content.title }}</h1>
    <v-row justify="end">
      <v-col id="content-date" class="col-4">
        <p class="body-1 font-weight-light">Created: {{ content.created_at | formatDate }}</p>
        <p class="body-1 font-weight-light">Last update: {{ content.updated_at | formatDate }}</p>
      </v-col>
    </v-row>
    <blockquote
      class="headline font-weight-light py-3"
      v-for="(paragraph, index) in content.body"
      v-bind:key=index
    >
      {{ paragraph }}
    </blockquote>
    <v-row align="center" justify="center">
      <v-btn class="my-4" text x-large @click="back">>> Back</v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      content: {}
    }
  },
  mounted () {
    this.getBlogContent()
  },
  methods: {
    getBlogContent: async function () {
      const response = await this.$http.get('/api/blog/item/' + this.$route.params.slug)
      this.content = response.data
    },
    back: function () {
      this.$router.push('/blog/')
    }
  }
}
</script>

<style scoped>
#content-date p {
  margin: 0 !important;
}
</style>
