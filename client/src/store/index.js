import { createStore } from 'vuex';
import api from '@/services/api';


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
    async login({ commit }, credentials) {
      try {
        const response = await api.post('/login', credentials);
        if (response.data.message === 'Login successful') {
          console.log(response.data.user); // Log the user data
          commit('setUser', response.data.user);  // Store the user's ID

          if (response.data.token) {
            commit('setToken', response.data.token);  // Store the token in the store
          }
        }
        return response.data;
      } catch (error) {
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