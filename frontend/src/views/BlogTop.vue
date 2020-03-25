<template>
  <v-container
    class="pa-4 mt-4 col-lg-6 col-md-8 col-10"
  >
    <h1 class="display-2 font-weight-light">Blog</h1>
    <v-container v-if="blogs" fluid>
      <blog-card
        v-for="(blog, index) in blogs"
        v-bind:key="index"
        v-bind:blog="blog"
      >
    </blog-card>
    </v-container>
    <h2 v-else>Nothing to show...</h2>
  </v-container>
</template>

<script>
import BlogCard from '@/components/BlogCard.vue'

export default {
  components: {
    'blog-card': BlogCard
  },
  data () {
    return {
      blogs: []
    }
  },
  mounted () {
    this.extractBlogData()
  },
  methods: {
    extractBlogData: async function () {
      const response = await this.$http.get('/api/blog/all/headlines')
      this.blogs = response.data
    }
  }
}
</script>
