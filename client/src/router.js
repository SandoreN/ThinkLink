<<<<<<< HEAD
import { createRouter, createWebHistory } from 'vue-router'
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
=======
import Vue from 'vue';
import VueRouter from 'vue-router';

import Login from './views/login';
import Projectworkspace from './views/projectworkspace';
import Teams from './views/teams';
import Projects from './views/projects';
import Library from './views/library';
import Messages from './views/messages';
import Root from './views/root';
import Profile from './views/profile';
import Template from './views/template';
import Dashboard from './views/dashboard';
import Register from './views/register';
import NotFound from './views/not-found';
>>>>>>> 877966aa5120b70c87fb43d591acbba184ed2ef3
import store from './store';

const routes = [
<<<<<<< HEAD
  {
    name: 'login',
    path: '/login',
    component: Login,
  },
  {
    name: 'projectworkspace',
    path: '/project_workspace/:project_id',
    component: Projectworkspace,
  },
  {
    name: 'teams',
    path: '/teams/:user_id',
    component: Teams,
  },
  {
    name: 'projects',
    path: '/projects/:user_id',
    component: Projects,
  },
  {
    name: 'library',
    path: '/library',
    component: Library,
  },
  {
    name: 'messages',
    path: '/messages/:receiver_id',
    component: Messages,
  },
  {
    name: 'root',
    path: '/',
    component: Root,
  },
  {
    name: 'profile',
    path: '/profile/:user_id',
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
    component: Dashboard
  },
  {
    name: 'dashboarduser',
    path: '/dashboard/:user_id',
    component: Dashboard,
    meta: { requiresAuth: true, roles: ['admin', 'user'] }
  },
  {
    name: 'register',
    path: '/register',
    component: Register,
  },
  {
    name: '404 - Not Found',
    path: '/**',
    component: NotFound,
    fallback: true,
  },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !store.state.user) {
    next('/login');
  } else {
    next();
  }
=======
  { name: 'login', path: '/login', component: Login },
  { name: 'projectworkspace', path: '/project_workspace/:projectId', component: Projectworkspace, props: true },
  { name: 'teams', path: '/teams', component: Teams },
  { name: 'projects', path: '/projects', component: Projects },
  { name: 'library', path: '/library', component: Library },
  { name: 'messages', path: '/messages', component: Messages },
  { name: 'root', path: '/', component: Root },
  { name: 'profile', path: '/profile', component: Profile },
  { name: 'template', path: '/template', component: Template },
  { name: 'dashboard', path: '/dashboard', component: Dashboard },
  { name: 'register', path: '/register', component: Register },
  { name: '404 - Not Found', path: '*', component: NotFound },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
>>>>>>> 877966aa5120b70c87fb43d591acbba184ed2ef3
});

export default router;
