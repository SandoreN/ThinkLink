<template>
  <div class="template-container"
    ><div class="template-container1"
      ><app-header rootClassName="header-root-class-name11"></app-header
      ><div class="template-body"
        ><app-leftsidebar></app-leftsidebar><app-pagemain></app-pagemain
        ><app-rightsidebar></app-rightsidebar></div></div
  ></div>
</template>

<script>
import AppHeader from '../components/header'
import AppLeftsidebar from '../components/leftsidebar'
import AppPagemain from '../components/pagemain'
import AppRightsidebar from '../components/rightsidebar'

export default {
  name: 'Template',
  props: {},
  components: {
    AppHeader,
    AppLeftsidebar,
    AppPagemain,
    AppRightsidebar,
  },
  metaInfo: {
    title: 'template - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'template - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.template-container {
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
.template-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.template-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}
</style>
