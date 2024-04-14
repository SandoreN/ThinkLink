<template>
  <header
    data-role="Header"
    class="register-header-header"
    v-bind:class="rootClassName"
    ><div class="register-header-main"
      ><div class="register-header-container"
        ><button type="button" class="register-header-button button"
          ><img
            alt="image"
            src="/external/thinklink-200h-200h.png"
            class="register-header-image"
          />{{ button }}</button
        ></div
      ><div class="register-header-container1"
        ><div class="register-header-container2"></div></div
      ><div id="register_button_container" class="register-header-register"
        ><router-link
          to="/login"
          id="login_button"
          name="login_button"
          class="register-header-navlink button"
          ><span class="register-header-text"
            ><span>{{ text }}</span><br /></span></router-link></div></div
  ></header>
</template>

<script>
export default {
  name: 'RegisterHeader',
  props: {
    rootClassName: String,
    imageSrc: {
      type: String,
      default: 'fffe1f7b-f004-491f-a196-afe3d8e0e92a',
    },
    button: {
      type: String,
      default: 'Button',
    },
    imageAlt: {
      type: String,
      default: 'image',
    },
    text: {
      type: String,
      default: 'Sign in',
    },
  },
}
</script>

<style scoped>
.register-header-header {
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
.register-header-main {
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
.register-header-container {
  flex: 0 0 auto;
  width: 225px;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: space-between;
}
.register-header-button {
  color: transparent;
  width: 225px;
  height: 100%;
  padding: 10px;
  align-self: center;
  border-width: 0px;
  text-decoration: none;
}
.register-header-image {
  width: 200px;
  height: auto;
  margin: auto;
  align-self: center;
  object-fit: cover;
  vertical-align: middle;
}
.register-header-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.register-header-container2 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: flex-start;
}
.register-header-register {
  flex: 0;
  width: 225px;
  display: flex;
  padding: 10px;
  position: relative;
  align-self: stretch;
  align-items: stretch;
  flex-direction: column;
  justify-content: space-between;
}
.register-header-navlink {
  color: var(--dl-color-gray-white);
  width: 200px;
  height: 100%;
  padding: auto;
  font-size: 30px;
  align-self: center;
  font-style: normal;
  text-align: center;
  align-items: center;
  font-weight: 700;
  padding-top: 0px;
  border-color: var(--dl-color-custom-primary2);
  border-width: 2px;
  padding-left: 0px;
  align-content: center;
  padding-right: 0px;
  padding-bottom: 0px;
  text-decoration: none;
  background-color: transparent;
}
.register-header-text {
  color: var(--dl-color-custom-primary2);
  font-size: 30px;
  align-self: center;
  text-align: center;
  vertical-align: middle;
}
.register-header-root-class-name {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.register-header-root-class-name1 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.register-header-root-class-name2 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.register-header-root-class-name3 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.register-header-root-class-name4 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.register-header-root-class-name5 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name6 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name7 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name8 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name9 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name10 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name11 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name12 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.register-header-root-class-name13 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
@media(max-width: 767px) {
  .register-header-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .register-header-header {
    padding: var(--dl-space-space-unit);
  }
}
</style>
