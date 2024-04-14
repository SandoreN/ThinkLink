<template>
  <div class="register-container"
    ><div class="register-container1"
      ><register-header></register-header
      ><div class="register-body"
        ><div class="register-sidebar"></div
        ><div class="register-pagemain"
          ><div class="register-container2"
            ><div class="register-container3"
              ><div class="register-container4"
                ><span class="register-text">Register new user</span></div
              ></div
            ><div class="register-container5"
              ><form id="login_form" name="login_form" class="register-form"
                ><input
                  type="text"
                  id="user.name_register"
                  name="user.name_register"
                  placeholder="Full name"
                  class="register-textinput input" />
                <input
                  type="text"
                  id="user.username_register"
                  name="user.username_register"
                  placeholder="username"
                  class="register-textinput1 input" />
                <input
                  type="text"
                  id="user.email_register"
                  name="user.email_register"
                  placeholder="email"
                  class="register-textinput2 input" />
                <input
                  type="text"
                  id="password"
                  name="password"
                  placeholder="password"
                  class="register-textinput3 input" /><router-link
                  to="/dashboard"
                  id="register_login_button"
                  name="login_button"
                  class="register-navlink button"
                  ><span class="register-text1"
                    ><span>Sign up</span
                    ><br /></span></router-link></form></div></div></div
        ><div class="register-rightsidebar"></div></div></div
  ></div>
</template>

<script>
import axios from 'axios';
import RegisterHeader from '../components/register-header.vue';

export default {
  name: 'Register',
  components: {
    RegisterHeader,
  },
  data() {
    return {
      user: {
        fullname: '',
        username: '',
        email: '',
        password: '',
      },
      errors: []
    };
  },
  methods: {
    async submitRegistration() {
      try {
        const response = await axios.post(`${process.env.VUE_APP_URL}/register`, this.user);
        console.log('Registration successful:', response);
        this.$router.push('/login');
      } catch (error) {
        console.error('Registration failed:', error);
        this.errors.push('Failed to register. Please try again.');
      }
    }
  },
  metaInfo: {
    title: 'Register - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'Register - ThinkLink',
      },
    ],
  },
};
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
</style>
