<template>
  <v-container class="pa-4 mt-4 col-lg-6 col-md-8 col-10">
    <h1 class="display-2 font-weight-light mb-5">Settings</h1>

    <v-card class="pa-5" width="100%" :elevation="$vuetify.theme.dark ? 0 : -5">
      <v-card-title class="headline font-weight-light">Theme</v-card-title>
      <v-row align="center" justify="center">
        <v-col class="col-3 title font-weight-light">Dark theme</v-col>
        <v-col class="col-7">
          <v-switch v-model="$vuetify.theme.dark"></v-switch>
        </v-col>
      </v-row>
    </v-card>
    <div class="my-12"></div>
    <v-row justify="center">
      <back-btn color="grey" />
    </v-row>

  </v-container>
</template>

<script>
import BackButton from '@/components/BackButton'

export default {
  components: {
    'back-btn': BackButton
  }
}
</script>
