import Vue from 'vue';
import Vuex from 'vuex';
import api from '@/services/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    token: localStorage.getItem('token')
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await api.post('/login', credentials);
        const token = response.data.token;
        localStorage.setItem('token', token);
        commit('setToken', token);
        const user = await api.get('/protected');
        commit('setUser', user.data.user);
      } catch (error) {
        // Handle login error
      }
    },
    async register(_, userData) {
      try {
        await api.post('/register', userData);
        // Handle successful registration
      } catch (error) {
        // Handle registration error
      }
    },
    async logout({ commit }) {
      try {
        await api.post('/logout');
        localStorage.removeItem('token');
        commit('setToken', null);
        commit('setUser', null);
      } catch (error) {
        // Handle logout error
      }
    }
  },
  getters: {
    isAuthenticated(state) {
      return !!state.token;
    },
    currentUser(state) {
      return state.user;
    }
  }
});