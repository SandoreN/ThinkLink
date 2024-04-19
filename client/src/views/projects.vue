<template>
  <div class="projects-container"
    ><div class="projects-container1"
      ><app-header rootClassName="header-root-class-name5"></app-header
      ><div class="projects-body"
        ><app-leftsidebar></app-leftsidebar>
        <div class="projects-pagemain">
          <div>
            <router-link
              v-for="project in projects"
              :key="project.id"
              :to="`/project_workspace/${project.project_id}`"
              tag="button">
              {{ project.name }}
            </router-link>
          </div>
        </div>
        <app-rightsidebar></app-rightsidebar></div></div
  ></div>
</template>

<script>
import AppHeader from '../components/header'
import AppLeftsidebar from '../components/leftsidebar'
import AppRightsidebar from '../components/rightsidebar'
import axios from 'axios'

export default {
  name: 'Projects',
  props: {},
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
  },
  data() {
    return {
      projects: [],
    };
  },
  async created() {
    try {
      const token = this.$store.state.user.token; // Access the token from the user state

      const response = await axios.get(
        `${process.env.VUE_APP_FLASK_APP_URL}/projects/${this.$store.state.user.id}`, 
        {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        }
      );
      this.projects = response.data;
    } catch (error) {
      console.error('Error fetching projects:', error);
    }
  },
  metaInfo: {
    title: 'projects - ThinkLink',
    meta: [
      {
        property: 'og:title',
        content: 'projects - ThinkLink',
      },
    ],
  },
}
</script>

<style scoped>
.projects-container {
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
.projects-container1 {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}
.projects-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}
.projects-pagemain {
  flex: 1;
  width: 200px;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
</style>
