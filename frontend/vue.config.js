module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: 'http://localhost:8000'
      }
    }
  },
  transpileDependencies: [
    'vuetify'
  ],
  chainWebpack: config => {
    config.module
      .rule('vue')
      .use('vue-loader')
      .loader('vue-loader')
      .tap(options => Object.assign(options, {
        transformAssetUrls: {
          'v-img': ['src', 'lazy-src']
        }
      }))
  }
}
