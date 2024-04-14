import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import Login from './views/login'
import Projectworkspace from './views/projectworkspace'
import Teams from './views/teams'
import Projects from './views/projects'
import Library from './views/library'
import Messages from './views/messages'
import Root from './views/root'
import Profile from './views/profile'
import Template from './views/template'
import Dashboard from './views/dashboard'
import Register from './views/register'
import NotFound from './views/not-found'
import './style.css'
import VueRouter from 'vue-router'
import store from './store';

Vue.use(VueRouter);

const routes = [
  {
    name: 'login',
    path: '/login',
    component: Login,
  },
  {
    name: 'projectworkspace',
    path: '/project_workspace',
    component: Projectworkspace,
  },
  {
    name: 'teams',
    path: '/teams',
    component: Teams,
  },
  {
    name: 'projects',
    path: '/projects',
    component: Projects,
  },
  {
    name: 'library',
    path: '/library',
    component: Library,
  },
  {
    name: 'messages',
    path: '/messages',
    component: Messages,
  },
  {
    name: 'root',
    path: '/',
    component: () => import('./views/root.vue'),
  },
  {
    name: 'profile',
    path: '/profile',
    component: Profile,
  },
  {
    name: 'template',
    path: '/template',
    component: Template,
  },
  {
    name: 'dashboard',
    path: '/dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    name: 'register',
    path: '/register',
    component: Register,
  },
  {
    name: '404 - Not Found',
    path: '**',
    component: NotFound,
    fallback: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = store.getters.isAuthenticated;

  if (requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;

