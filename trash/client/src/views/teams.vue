<template>
  <div class="teams-container"
    ><div class="teams-container1"
      ><app-header rootClassName="header-root-class-name8"></app-header
      ><div class="teams-body"
        ><app-leftsidebar></app-leftsidebar><div class="teams-pagemain"></div
        ><app-rightsidebar></app-rightsidebar></div></div
  ></div>
</template>

<script>
import AppHeader from '../components/header'
import AppLeftsidebar from '../components/leftsidebar'
import AppRightsidebar from '../components/rightsidebar'

export default {
  name: 'Teams',
  props: {},
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
  },
  metaInfo: {
    title: 'teams - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'teams - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.teams-container {
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
.teams-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.teams-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}
.teams-pagemain {
  flex: 1;
  width: 200px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
</style>
