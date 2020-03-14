import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/Index'
import About from '@/views/About'
import Blog from '@/views/BlogTop'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog
    }
  ]
})
