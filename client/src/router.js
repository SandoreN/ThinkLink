import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import Teams from './views/teams'
import Projects from './views/projects'
import Library from './views/library'
import Messages from './views/messages'
import Root from './views/root'
import Profile from './views/profile'
import Template from './views/template'
import Dashboard from './views/dashboard'
import NotFound from './views/not-found'
import './style.css'

Vue.use(Router)
Vue.use(Meta)
export default new Router({
  mode: 'history',
  routes: [
    {
      name: 'teams',
      path: '/template3',
      component: Teams,
    },
    {
      name: 'projects',
      path: '/template',
      component: Projects,
    },
    {
      name: 'library',
      path: '/template4',
      component: Library,
    },
    {
      name: 'messages',
      path: '/template2',
      component: Messages,
    },
    {
      name: 'root',
      path: '/',
      component: Root,
    },
    {
      name: 'profile',
      path: '/template5',
      component: Profile,
    },
    {
      name: 'template',
      path: '/template6',
      component: Template,
    },
    {
      name: 'dashboard',
      path: '/template1',
      component: Dashboard,
    },
    {
      name: '404 - Not Found',
      path: '**',
      component: NotFound,
      fallback: true,
    },
  ],
})
