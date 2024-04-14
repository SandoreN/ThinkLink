<template>
  <header data-role="Header" class="header1-header" v-bind:class="rootClassName"
    ><div class="header1-main"
      ><div class="header1-container"
        ><button type="button" class="header1-button button"
          ><img :alt="imageAlt" :src="imageSrc" class="header1-image" />{{ button
          }}</button
        ></div
      ><div class="header1-container1"
        ><div class="header1-container2"></div></div></div
  ></header>
</template>

<script>
export default {
  name: 'Header1',
  props: {
    rootClassName: String,
    imageSrc: {
      type: String,
      default: '056f094a-c183-4f12-bcbd-d7d82777014b',
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
.header1-header {
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
.header1-main {
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
.header1-container {
  flex: 0 0 auto;
  width: 225px;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: space-between;
}
.header1-button {
  color: transparent;
  width: 225px;
  height: 100%;
  padding: 10px;
  align-self: center;
  border-width: 0px;
  text-decoration: none;
}
.header1-image {
  width: 200px;
  height: auto;
  margin: auto;
  align-self: center;
  object-fit: cover;
  vertical-align: middle;
}
.header1-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: flex-start;
}
.header1-container2 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-start;
  align-items: center;
  justify-content: flex-start;
}
.header1-root-class-name {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header1-root-class-name1 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header1-root-class-name2 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header1-root-class-name3 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header1-root-class-name4 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: absolute;
}
.header1-root-class-name5 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name6 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name7 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name8 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name9 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name10 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name11 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name12 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
.header1-root-class-name13 {
  top: 0px;
  left: 0px;
  bottom: 0px;
  position: static;
  align-self: flex-start;
}
@media(max-width: 767px) {
  .header1-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .header1-header {
    padding: var(--dl-space-space-unit);
  }
}
</style>
