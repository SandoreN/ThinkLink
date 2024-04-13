<template>
  <header data-role="Header" class="header-header" v-bind:class="rootClassName"
    ><div class="header-main"
      ><div class="header-container"
        ><router-link to="/dashboard" class="header-navlink button"
          ><img :alt="imageAlt" :src="imageSrc" class="header-image" />{{ button
          }}</router-link
        ></div
      ><div class="header-container1"
        ><div class="header-container2"></div></div></div
  ></header>
</template>

<script>
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
.header-root-class-name {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header-root-class-name1 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header-root-class-name2 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header-root-class-name3 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header-root-class-name4 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header-root-class-name5 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name6 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name7 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name8 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name9 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name10 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name11 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name12 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header-root-class-name13 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
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
