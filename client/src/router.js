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
import store from './store';

Vue.use(VueRouter);

const routes = [
  { name: 'login', path: '/login', component: Login },
  { name: 'projectworkspace', path: '/project_workspace', component: Projectworkspace },
  { name: 'teams', path: '/teams', component: Teams },
  { name: 'projects', path: '/projects', component: Projects },
  { name: 'library', path: '/library', component: Library },
  { name: 'messages', path: '/messages', component: Messages },
  { name: 'root', path: '/', component: Root },
  { name: 'profile', path: '/profile', component: Profile },
  { name: 'template', path: '/template', component: Template },
  { name: 'dashboard', path: '/dashboard', component: Dashboard },
  { name: 'register', path: '/register', component: Register },
  { name: '404 - Not Found', path: '**', component: NotFound },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
