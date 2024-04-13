<template>
  <div class="projectworkspace-container"
    ><div class="projectworkspace-container1"
      ><app-header1></app-header1
      ><div class="projectworkspace-body"
        ><app-leftsidebar></app-leftsidebar
        ><div class="projectworkspace-pagemain"></div
        ><div class="projectworkspace-projectsidebar"
          ><div class="projectworkspace-container2"></div
          ><div class="projectworkspace-container3"></div
          ><div class="projectworkspace-container4"></div
          ><div class="projectworkspace-container5"></div></div></div></div
  ></div>
</template>

<script>
import AppHeader1 from '../components/header1'
import AppLeftsidebar from '../components/leftsidebar'

export default {
  name: 'Projectworkspace',
  props: {},
  components: {
    AppHeader1,
    AppLeftsidebar,
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
.projectworkspace-container2 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: flex-start;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
}
.projectworkspace-container3 {
  flex: 0 0 auto;
  width: 100%;
  height: 50px;
  display: flex;
  align-items: flex-start;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
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
  align-items: center;
  border-color: var(--dl-color-gray-500);
  border-style: dashed;
  border-width: 1px;
  justify-content: center;
}
</style>
