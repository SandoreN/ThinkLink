<template>
  <div class="projectworkspace-container"
    ><div class="projectworkspace-container1"
      ><header data-role="Header" class="projectworkspace-projectheader"
        ><div class="projectworkspace-main"
          ><router-link to="/" class="projectworkspace-navlink button"
            ><img
              alt="image"
              src="3904a565-f753-4912-9d2d-a54dc279be92"
              class="projectworkspace-image"
            />Button</router-link
          ><div class="projectworkspace-container2"></div
          ><div class="projectworkspace-container3"
            ><span id="project.name" class="projectworkspace-text"
              ><span>Name of <span v-html="raw7fpt"></span></span
              ><span>project</span><br /></span></div></div></header
      ><div class="projectworkspace-body"
        ><app-leftsidebar></app-leftsidebar
        ><div class="projectworkspace-pagemain"></div
        ><div class="projectworkspace-projectsidebar"
          ><div class="projectworkspace-container4"></div
          ><div class="projectworkspace-container5"></div
          ><div class="projectworkspace-container6"></div
          ><div class="projectworkspace-container7"></div></div></div></div
  ></div>
</template>

<script>
import AppLeftsidebar from '../components/leftsidebar'

export default {
  name: 'Projectworkspace',
  props: {},
  components: {
    AppLeftsidebar,
  },
  data() {
    return {
      raw7fpt: ' ',
    }
  },
  metaInfo: {
    title: 'projectworkspace - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'projectworkspace - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.projectworkspace-container {
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
.projectworkspace-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.projectworkspace-projectheader {
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
.projectworkspace-main {
  flex: 0 0 auto;
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
.projectworkspace-navlink {
  color: transparent;
  width: 225px;
  height: 100%;
  align-self: flex-start;
  border-width: 0px;
  text-decoration: none;
}
.projectworkspace-image {
  width: 200px;
  align-self: center;
  object-fit: cover;
}
.projectworkspace-container2 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: flex-end;
  align-items: stretch;
  flex-direction: row;
  justify-content: flex-start;
}
.projectworkspace-container3 {
  width: 225px;
  height: 100%;
  display: flex;
  align-self: flex-end;
  align-items: stretch;
  flex-direction: row;
  justify-content: flex-end;
}
.projectworkspace-text {
  color: var(--dl-color-gray-700);
  width: 100%;
  height: auto;
  font-size: 18px;
  align-self: flex-end;
  font-style: normal;
  font-weight: 700;
  padding-bottom: 8px;
}
.projectworkspace-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}
.projectworkspace-pagemain {
  flex: 1;
  width: 200px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.projectworkspace-projectsidebar {
  flex: 0 0 auto;
  width: 225px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
.projectworkspace-container4 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: flex-start;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
}
.projectworkspace-container5 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: flex-start;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
}
.projectworkspace-container6 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: flex-start;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
}
.projectworkspace-container7 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: center;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
  justify-content: center;
}
@media(max-width: 767px) {
  .projectworkspace-projectheader {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .projectworkspace-projectheader {
    padding: var(--dl-space-space-unit);
  }
}
</style>
