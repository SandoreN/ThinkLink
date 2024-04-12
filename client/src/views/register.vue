<template>
  <div class="register-container"
    ><div class="register-container1"
      ><header data-role="Header" class="register-header"
        ><div class="register-main"
          ><router-link to="/" class="register-navlink button"
            ><img
              alt="image"
              src="3904a565-f753-4912-9d2d-a54dc279be92"
              class="register-image"
            />Button</router-link
          ><div class="register-container2"
            ><div class="register-container3"></div
            ><div id="register_button_container" class="register-register"
              ><button
                id="login_register_button"
                name="login_register_button"
                type="button"
                class="register-button button"
                ><span class="register-text"
                  ><span>Sign in</span
                  ><br /></span></button></div></div></div></header
      ><div class="register-body"
        ><div class="register-sidebar"></div
        ><div class="register-pagemain"
          ><div class="register-container4"
            ><div class="register-container5"
              ><div class="register-container6"
                ><span class="register-text3">Register new user</span></div
              ></div
            ><div class="register-container7"
              ><form id="login_form" name="login_form" class="register-form"
                ><input
                  type="text"
                  id="user.name_register"
                  name="user.name_register"
                  placeholder="Full name"
                  class="register-textinput input" /><input
                  type="text"
                  id="user.username_register"
                  name="user.username_register"
                  placeholder="username"
                  class="register-textinput1 input" /><input
                  type="text"
                  id="user.email_register"
                  name="user.email_register"
                  placeholder="email"
                  class="register-textinput2 input" /><input
                  type="text"
                  id="password"
                  name="password"
                  placeholder="password"
                  class="register-textinput3 input" /><button
                  id="register_login_button"
                  name="login_button"
                  type="register_login_button"
                  class="register-button1 button"
                  ><span class="register-text4"
                    ><span>Sign up</span
                    ><br /></span></button></form></div></div></div
        ><div class="register-rightsidebar"></div></div></div
  ></div>
</template>

<script>
export default {
  name: 'Register',
  props: {},
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
.register-header {
  width: 100%;
  height: 75px;
  display: flex;
  position: relative;
  max-width: var(--dl-size-size-maxwidth);
  align-self: flex-start;
  align-items: center;
  flex-direction: row;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.register-main {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  border-color: var(--dl-color-gray-700);
  border-width: 1px;
  justify-content: flex-start;
  border-top-width: 0px;
  border-left-width: 0px;
  border-right-width: 0px;
  border-bottom-width: 2px;
}
.register-navlink {
  color: transparent;
  width: 225px;
  height: 100%;
  align-self: flex-start;
  padding-top: 0px;
  border-width: 0px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
  text-decoration: none;
}
.register-image {
  width: 200px;
  align-self: center;
  object-fit: cover;
}
.register-container2 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.register-container3 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: stretch;
  justify-content: space-between;
}
.register-register {
  width: 225px;
  height: 100%;
  display: flex;
  padding: 10px;
  position: relative;
  align-self: flex-end;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.register-button {
  color: var(--dl-color-gray-white);
  width: 200px;
  height: 100%;
  font-size: 30px;
  align-self: center;
  font-style: normal;
  font-weight: 700;
  padding-top: 0px;
  border-color: var(--dl-color-custom-primary2);
  border-width: 2px;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: 0px;
  background-color: transparent;
}
.register-text {
  color: var(--dl-color-custom-primary2);
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
.register-container4 {
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
.register-container5 {
  width: 100%;
  height: 30%;
  display: flex;
  align-self: center;
  margin-top: 0px;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.register-container6 {
  flex: 1;
  width: 100%;
  height: 10%;
  display: flex;
  align-self: center;
  align-items: center;
  justify-content: center;
}
.register-text3 {
  font-size: 30px;
  align-self: center;
  font-style: normal;
  text-align: center;
  font-family: "Inter";
  font-weight: 700;
}
.register-container7 {
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
.register-button1 {
  color: var(--dl-color-gray-white);
  width: 65%;
  height: 70px;
  margin-top: 30px;
  border-width: 0px;
  background-color: rgb(38, 20, 96);
}
.register-text4 {
  font-size: 30px;
  font-style: normal;
  text-align: center;
  font-weight: 700;
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
@media(max-width: 767px) {
  .register-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .register-header {
    padding: var(--dl-space-space-unit);
  }
}
</style>
