import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Index from '@/views/Index'
import Login from '@/views/Login'
import Profile from '@/views/Profile'
import EditProfile from '@/views/EditProfile'
import Settings from '@/views/Settings'
import About from '@/views/About'
import Blog from '@/views/BlogTop'
import BlogContent from '@/views/BlogContent'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { hideNavigation: true }
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/account/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/account/profile/edit',
      name: 'profile-edit',
      component: EditProfile,
      props: true
    },
    {
      path: '/account/settings',
      name: 'settings',
      component: Settings
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
    },
    {
      path: '/blog/:slug',
      name: 'blog-content',
      component: BlogContent
    }
  ]
})
