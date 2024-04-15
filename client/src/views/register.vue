<template>
  <div class="register-container">
    <div class="register-container1">
      <register-header></register-header>
      <div class="register-body">
        <div class="register-sidebar"></div>
        <div class="register-pagemain">
          <div class="register-container2">
            <div class="register-container3">
              <div class="register-container4">
                <span class="register-text">Register new user</span>
              </div>
            </div>
            <div class="register-container5">
              <form id="register_form" name="register_form" class="register-form" @submit.prevent="register">
    <input
      v-model="user.name"
      type="text"
      id="user.name_register"
      name="user.name_register"
      placeholder="Full name"
      class="register-textinput input" 
    />
    <input
      v-model="user.username"
      type="text"
      id="user.username_register"
      name="user.username_register"
      placeholder="username"
      class="register-textinput1 input" 
    />
    <input
      v-model="user.email"
      type="text"
      id="user.email_register"
      name="user.email_register"
      placeholder="email"
      class="register-textinput2 input" 
    />
    <input
      v-model="user.password"
      type="text"
      id="password"
      name="password"
      placeholder="password"
      class="register-textinput3 input" 
    />
    <button
      type="submit"
      id="register_button"
      name="register_button"
      class="register-navlink button">
      <span class="register-text1">
        <span>Sign up</span
      ><br /></span>
    </button>
  </form></div></div></div
        ><div class="register-rightsidebar"></div></div></div
  ></div>
</template>

<script>
import axios from 'axios'
import RegisterHeader from '../components/register-header'

export default {
  name: 'Register',
  props: {},
  components: {
    RegisterHeader,
  },
  data() {
    return {
      user: {
        name: '',
        username: '',
        email: '',
        password: ''
      },
      error: null,
    }
  },
  methods: {
    async register() {
      console.log('register method called with user data:', this.user);
      try {
        const response = await axios.post('http://localhost:5000/register', this.user);
        console.log('server response:', response);
        // handle response
      } catch (error) {
        console.log('error:', error);
        // handle error
      }
    }
  },
  metaInfo: {
    title: 'register - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'register - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.register-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  border-color: var(--dl-color-gray-black);
  border-width: 0px;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.register-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.register-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
  background-color: var(--dl-color-gray-900);
}
.register-sidebar {
  width: 225px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: stretch;
  flex-direction: column;
  justify-content: flex-start;
}
.register-pagemain {
  flex: 1;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.register-container2 {
  flex: 0 0 auto;
  width: 600px;
  height: 600px;
  display: flex;
  padding: 80px;
  margin-top: 0px;
  align-items: flex-start;
  padding-top: 30px;
  padding-left: 30px;
  padding-right: 30px;
  flex-direction: column;
  padding-bottom: 30px;
  justify-content: flex-start;
  background-color: var(--dl-color-gray-white);
}
.register-container3 {
  width: 100%;
  height: 30%;
  display: flex;
  align-self: center;
  margin-top: 0px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.register-container4 {
  flex: 1;
  width: 100%;
  height: 10%;
  display: flex;
  align-self: center;
  align-items: center;
  justify-content: center;
}
.register-text {
  font-size: 30px;
  align-self: center;
  font-style: normal;
  text-align: center;
  font-family: "Inter";
  font-weight: 700;
}
.register-container5 {
  flex: 1;
  width: 100%;
  height: 60%;
  display: flex;
  align-self: flex-end;
  align-items: flex-start;
  flex-direction: column;
}
.register-form {
  width: 100%;
  height: 90%;
  display: flex;
  align-self: center;
  align-items: center;
  padding-top: 0px;
  flex-direction: column;
  justify-content: space-between;
}
.register-textinput {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.register-textinput1 {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.register-textinput2 {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.register-textinput3 {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.register-navlink {
  color: var(--dl-color-gray-white);
  width: 65%;
  height: 70px;
  padding: 15px;
  align-self: center;
  margin-top: 30px;
  text-align: center;
  border-width: 0px;
  text-decoration: none;
  background-color: rgb(38, 20, 96);
}
.register-text1 {
  font-size: 30px;
  align-self: center;
  font-style: normal;
  text-align: center;
  font-weight: 700;
  vertical-align: middle;
}
.register-rightsidebar {
  flex: 0 0 auto;
  width: 225px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
#register_button {
  cursor: pointer;
}
</style>



