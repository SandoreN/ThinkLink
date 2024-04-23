import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userId: null
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId;
    }
  },
  actions: {
    login({ commit }, userId) {
      commit('setUserId', userId );
    },
  },
  getters: {
    currentUserId(state) {
      return state.userId;
    }
  }
});