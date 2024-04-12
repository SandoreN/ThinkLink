<template>
  <div class="profile-container"
    ><div class="profile-container1"
      ><app-header rootClassName="header-root-class-name10"></app-header
      ><div class="profile-body"
        ><app-leftsidebar></app-leftsidebar><div class="profile-pagemain"></div
        ><app-rightsidebar></app-rightsidebar></div></div
  ></div>
</template>

<script>
import AppHeader from '../components/header'
import AppLeftsidebar from '../components/leftsidebar'
import AppRightsidebar from '../components/rightsidebar'

export default {
  name: 'Profile',
  props: {},
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
  },
  metaInfo: {
    title: 'profile - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'profile - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.profile-container {
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
.profile-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.profile-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}
.profile-pagemain {
  flex: 1;
  width: 200px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
</style>
