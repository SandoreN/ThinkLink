<template>
  <div class="leftsidebar-sidebar"
    ><app-leftsidebarinner
      rootClassName="leftsidebarinner-root-class-name6"
    ></app-leftsidebarinner
  ></div>
</template>

<script>
import AppLeftsidebarinner from './leftsidebarinner'

export default {
  name: 'Leftsidebar',
  props: {},
  components: {
    AppLeftsidebarinner,
  },
}
</script>

<style scoped>
.leftsidebar-sidebar {
  width: 225px;
  flex-grow: 1;
  position: relative;
  align-self: stretch;
  align-items: stretch;
  flex-direction: column;
  justify-content: flex-start;
}
</style>
