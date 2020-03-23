<template>
<v-hover
  v-slot:default="{ hover }"
  open-delay="200"
>
  <v-card
    class="mx-auto my-10"
    width="85%"
    max-width="800px"
    :elevation="hover ? 10 : 4"
    :to="'#'"
  >
    <v-img
      class="white--text align-end"
      height="250px"
      v-bind:src="blog.image.path"
    >
      <v-card-title>{{ blog.title }}</v-card-title>
    </v-img>
    <v-card-subtitle class="pb-0 my-5">{{ blog.headline }}</v-card-subtitle>
    <v-card-text>Last update: {{ blog.updated_at | formatDate }}</v-card-text>
  </v-card>
</v-hover>
</template>

<script>
export default {
  props: ['blog'],
  data () {
    return {
      hover: false
    }
  }
}
</script>

<style scoped>
.v-card {
  transition: .4s;
}
.v-card:hover {
  opacity: 0.9;
  transform: translateY(-3px);
}
</style>
