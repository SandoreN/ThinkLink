import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: null  // Assuming you can set this directly for demonstration purposes
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId;
    }
  },
  actions: {
    login({ commit }, userId) {
      commit('setUserId', userId); // Directly set the user ID, maybe from a form or a static value
    },
    logout({ commit }) {
      commit('setUserId', null);
    }
  },
  getters: {
    currentUserId(state) {
      return state.userId;
    }
  }
});
