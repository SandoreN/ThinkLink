<template>
  <div class="projectworkspace-container">
    <div class="projectworkspace-container1">
      <app-header rootClassName="header-root-class-name5"></app-header>
      <div class="projectworkspace-body">
        <app-leftsidebar></app-leftsidebar>
        <div class="projectworkspace-pagemain">
          <component :is="currentTab" v-bind:project_id="project_id"></component>
        </div>
        <app-rightsidebar>
          <app-projectsidebarinner @change-tab="changeTab"></app-projectsidebarinner>
        </app-rightsidebar>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '../components/header'
import AppLeftsidebar from '../components/leftsidebar'
import AppRightsidebar from '../components/rightsidebar'
import AppProjectsidebarinner from '../components/projectsidebarinner'
import Drafts from '../components/drafts.vue'
import Tasks from '../components/tasks.vue'
import Resources from '../components/resources.vue'
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'Projectworkspace',
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
    AppProjectsidebarinner,
    Drafts,
    Tasks,
    Resources
  },
  setup() {
    const route = useRoute();
    const project_id = ref(route.params.project_id);

    return {
      project_id,
    };
  },
  data() {
    return {
      currentTab: 'Drafts',
    }
  },
  methods: {
    changeTab(tab) {
      this.currentTab = tab;
    }
  }
};

</script>

<style scoped>
.projectworkspace-container {
  width: 100%;
  display: flex;
  min-height: 100vh;
  align-items: stretch;
  border-color: var(--dl-color-gray-black);
  border-width: 0px;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}
.projectworkspace-container1 {
  flex: 1;
  width: 100%;
  display: flex;
  align-items: stretch;
  flex-direction: column;
  justify-content: flex-start;
}

.projectworkspace-body {
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-self: stretch;
  align-items: center;
  flex-direction: row;
  /*justify-content: center;*/
}

.projectworkspace-pagemain {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
  justify-content: center;
  padding-top: 30px;
  max-width: 100%;
  height: 100%;
  position: relative;
  flex-grow: 1;
}

#markdown-editor {
  /*flex: 1;*/
  display: flex;
  width: 500px; /* fill the parent div */
  height: 450px; /* fill the parent div */
  /*align-self: stretch;*/
  /*position: relative;*/
  border: 1px solid black;
}

.projectworkspace-projectsidebar {
  flex: 0 0 auto;
  width: 225px;
  height: 100%;
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
.draft-name-input {
  height: 55px; /* Adjust the height as needed */
  padding: 10px;
  font-size: 30px; /* Adjust the font size as needed */
  margin-bottom: 20px;
  border: 2px solid black;
  border-radius: 4px;
  align-items: center;
  justify-content: center;
  /* Add other styling properties as needed */
}
.markdown-preview {
  margin-top: 10px; /* Add some space above the preview pane */
  margin-bottom: 10px; /* Add some space below the preview pane */
  overflow-y: auto;/* Add a scrollbar if the content is too long to fit in the pane */
  height: 200px;
  width: 500px;
  border: 1px solid black;
}

.save-button {
  align-self: center;
  /* Other CSS properties... */
}
</style>
