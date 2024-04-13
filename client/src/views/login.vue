<template>
  <div class="login-container"
    ><div class="login-container1"
      ><login-header></login-header
      ><div class="login-body"
        ><div class="login-sidebar"></div
        ><div class="login-pagemain"
          ><div class="login-container2"
            ><div class="login-container3"
              ><img
                alt="image"
                src="/thinklink_logo-300h.png"
                class="login-image"
              /><div class="login-container4"
                ><span class="login-text">Sign in</span></div
              ></div
            ><div class="login-container5"
              ><form id="login_form" name="login_form" class="login-form"
                ><input
                  type="text"
                  id="email"
                  name="email"
                  placeholder="email"
                  class="login-textinput input" /><input
                  type="text"
                  id="password"
                  name="password"
                  placeholder="password"
                  class="login-textinput1 input" /><router-link
                  to="/dashboard"
                  id="login_button"
                  name="login_button"
                  class="login-navlink button"
                  ><span class="login-text1"
                    ><span>Sign in</span
                    ><br /></span></router-link></form></div></div></div
        ><div class="login-rightsidebar"></div></div></div
  ></div>
</template>

<script>
import LoginHeader from '../components/login-header'

export default {
  name: 'Login',
  props: {},
  components: {
    LoginHeader,
  },
  metaInfo: {
    title: 'login - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'login - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.login-container {
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
.login-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.login-body {
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
.login-sidebar {
  width: 225px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: stretch;
  flex-direction: column;
  justify-content: flex-start;
}
.login-pagemain {
  flex: 1;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.login-container2 {
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
.login-container3 {
  width: 100%;
  height: 40%;
  display: flex;
  align-self: center;
  margin-top: 0px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.login-image {
  width: 100px;
  align-self: center;
  object-fit: cover;
}
.login-container4 {
  flex: 1;
  width: 100%;
  height: 10%;
  display: flex;
  align-self: flex-end;
  align-items: center;
  justify-content: center;
}
.login-text {
  font-size: 30px;
  font-style: normal;
  text-align: center;
  font-family: "Inter";
  font-weight: 700;
}
.login-container5 {
  flex: 1;
  width: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
.login-form {
  width: 100%;
  height: 90%;
  display: flex;
  align-self: center;
  align-items: center;
  padding-top: 30px;
  flex-direction: column;
  justify-content: space-between;
}
.login-textinput {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.login-textinput1 {
  width: 65%;
  border-color: var(--dl-color-gray-500);
  border-width: 1px;
  border-radius: 0px;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 1px;
}
.login-navlink {
  color: var(--dl-color-gray-white);
  width: 65%;
  height: 70px;
  padding: 15px;
  position: relative;
  align-self: center;
  margin-top: 30px;
  text-align: center;
  border-width: 0px;
  text-decoration: none;
  background-color: rgb(38, 20, 96);
}
.login-text1 {
  font-size: 30px;
  align-self: center;
  font-style: normal;
  text-align: center;
  font-weight: 700;
  vertical-align: middle;
}
.login-rightsidebar {
  flex: 0 0 auto;
  width: 225px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
</style>
