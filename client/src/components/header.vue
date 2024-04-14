<template>
  <header data-role="Header" class="header-header" v-bind:class="rootClassName">
    <div class="header-main">
      <div class="header-container">
        <router-link to="/dashboard" class="header-navlink button">
          <img :alt="imageAlt" :src="imageSrc" class="header-image" />{{ button }}
        </router-link>
      </div>
      <div class="header-container1">
        <div class="header-container2"></div>
      </div>
    </div>
    <!-- Logout Button only shown when user is authenticated -->
    <button @click="logout" v-if="isAuthenticated" class="logout-button">Logout</button>
  </header>
</template>

<script>
import axios from 'axios'; // Assuming axios might be needed elsewhere, not needed for current functionality

export default {
  name: 'Header',
  props: {
    rootClassName: String,
    imageSrc: {
      type: String,
      default: '/thinklink-200h.png',
    },
    button: {
      type: String,
      default: 'Button',
    },
    imageAlt: {
      type: String,
      default: 'image',
    },
  },
  computed: {
    // Computed property to determine if the user is authenticated
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    // Method to handle logout
    async logout() {
      try {
        await this.$store.dispatch('logout');
        this.$router.push('/login'); // Redirect to login after logout
      } catch (error) {
        console.error('Logout failed:', error);
        // Optionally show an error message to the user
      }
    }
  },
}
</script>

<style scoped>
.header-header {
  width: 100%;
  height: 75px;
  display: flex;
  position: relative;
  max-width: 100%;
  align-self: flex-start;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.header-main {
  flex: 0 0 auto;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  border-color: var(--dl-color-gray-700);
  border-width: 1px;
  justify-content: center;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 2px;
}
.header-container {
  flex: 0 0 auto;
  width: 225px;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: space-between;
}
.header-navlink {
  color: transparent;
  width: 225px;
  height: 100%;
  padding: 10px;
  align-self: center;
  border-width: 0px;
  text-decoration: none;
}
.header-image {
  width: 200px;
  height: auto;
  margin: auto;
  align-self: center;
  object-fit: cover;
  vertical-align: middle;
}
.header-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.header-container2 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: flex-start;
}
.logout-button {
  padding: 10px 20px;
  background-color: #f00;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-top: 20px;
}
@media(max-width: 767px) {
  .header-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .header-header {
    padding: var(--dl-space-space-unit);
  }
}
</style>
