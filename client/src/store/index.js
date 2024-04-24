import { createStore } from 'vuex';
import api from '@/services/api';
import axios from 'axios';

export default createStore({
  state: {
    user: null,
    token: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
  },
  actions: {
    async login({ commit }, { email, password }) {
      try {
        const response = await axios.post('http://localhost:5000/login', { email, password });
        commit('setUser', response.data.user);
        return response.data;
      } catch (error) {
        console.error('Login error:', error);
        throw error;
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
        commit('setUser', null);
      } catch (error) {
        // Handle logout error
      }
    }
  },
  getters: {
    currentUser(state) {
      return state.user;
    }
  }
});