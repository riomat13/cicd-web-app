<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10">
    <h1 class="display-3 font-light">Blog</h1>
    <v-container v-if="blogs" fluid>
      <blogCard
        v-for="blog in blogs"
        v-bind:key="blog.updated_at"
        v-bind:blog="blog"
      ></blogCard>
    </v-container>
    <h2 v-else>Nothing to show...</h2>
    <go-to-top />
  </v-container>
</template>

<script>
import BlogCard from '@/components/BlogCard.vue'
import GoToTop from '@/components/GoToTop.vue'

export default {
  components: {
    blogCard: BlogCard,
    'go-to-top': GoToTop
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
      const response = await this.$http.get('/api/blog/')
      this.blogs = response.data
    }
  }
}
</script>
