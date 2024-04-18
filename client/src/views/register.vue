<template>
  <div class="register-container">
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
            <form @submit.prevent="register" class="register-form">
              <input
                type="text"
                id="fullname"
                name="fullname"
                placeholder="Full name"
                class="register-textinput input"
                v-model="user.fullname" />
              <input
                type="text"
                id="username"
                name="username"
                placeholder="Username"
                class="register-textinput1 input"
                v-model="user.username" />
              <input
                type="email"
                id="email"
                name="email"
                placeholder="Email"
                class="register-textinput2 input"
                v-model="user.email" />
              <input
                type="password"
                id="password"
                name="password"
                placeholder="Password"
                class="register-textinput3 input"
                v-model="user.password" />
              <button type="submit" class="register-navlink button" @click="register">
                <span class="register-text1">Sign up</span>
              </button>
            </form>
          </div>
        </div>
      </div>
      <div class="register-rightsidebar"></div>
    </div>
  </div>
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
      fullname: '',
      username: '',
      email: '',
      password: ''
    }
  }
},
  methods: {
    async register() {
      const user_data = {
        name: this.user.fullname,
        username: this.user.username,
        email: this.user.email,
        password: this.user.password_hash
      }
      console.log('register method called with user data:', user_data);
      try {
        const response = await axios.post(`${process.env.VUE_APP_FLASK_APP_URL}/register`, user_data);
        console.log('server response:', response);
        this.$router.push('/login');
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
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.register-container1 {
  flex: 1;
  width: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.register-body {
  flex: 1;
  display: flex;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
  background-color: var(--dl-color-gray-900);
}
.register-sidebar {
  width: 225px;
  display: flex;
  flex-direction: column;
}
.register-pagemain {
  flex: 1;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.register-container2 {
  width: 600px;
  padding: 80px;
  display: flex;
  flex-direction: column;
  background-color: var(--dl-color-gray-white);
}
.register-container3 {
  align-self: center;
  display: flex;
  flex-direction: column;
}
.register-container4 {
  align-items: center;
  justify-content: center;
  display: flex;
}
.register-text {
  font-size: 30px;
  font-weight: 700;
  font-family: "Inter";
}
.register-container5 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.register-form {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.register-textinput, .register-textinput1, .register-textinput2, .register-textinput3 {
  width: 65%;
  margin-bottom: 20px;
  border-bottom-width: 1px;
}
.register-navlink {
  width: 65%;
  padding: 15px;
  text-align: center;
  background-color: rgb(38, 20, 96);
  color: var(--dl-color-gray-white);
  text-decoration: none;
  margin-top: 30px;
}
.register-rightsidebar {
  width: 225px;
  display: flex;
  flex-direction: column;
}
#register_button {
  cursor: pointer;
}
</style>



