<template>
  <div class="projects-container">
    <div class="projects-container1">
      <app-header rootClassName="header-root-class-name5"></app-header>
      <div class="projects-body">
        <app-leftsidebar></app-leftsidebar>
        <div class="projects-pagemain">
          <div>
            <router-link
              v-for="project in projects"
              :key="project.id"
              :to="`/project_workspace/${project.id}`"
              tag="button"
            >
              {{ project.name }}
            </router-link>
          </div>
          <form @submit.prevent="createProject">
            <input type="text" v-model="newProject.name" placeholder="Project name">
            <textarea v-model="newProject.description" placeholder="Project description"></textarea>
            <button type="submit">Create Project</button>
          </form>
        </div>
        <app-rightsidebar></app-rightsidebar>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import AppHeader from '../components/header';
import AppLeftsidebar from '../components/leftsidebar';
import AppRightsidebar from '../components/rightsidebar';
import axios from 'axios';

export default {
  name: 'Projects',
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
  },
  computed: {
    ...mapGetters(['currentUserId']),
  },
  data() {
    return {
      projects: [],
      newProject: {
        name: '',
        description: '',
        resource_dir: '',
      },
    };
  },
  created() {
  // Check if the user ID is stored in localStorage or cookies
      const userIdValue = localStorage.getItem('userId') || getCookie('userId');
      if (userIdValue) {
        // If we have a user ID, dispatch the login action
        this.$store.dispatch('login', userIdValue);
        // Now you can fetch projects or do other actions that require the user ID
        this.fetchProjects();
      } else {
        // Handle the situation where there is no user ID (e.g., redirect to login page)
        console.error('No user ID found, redirecting to login.');
        this.$router.push('/login');
  }
},
  methods: {
    fetchProjects() {
      if (!this.currentUserId) {
        console.error('Creator ID is missing');
        return;
      }
      axios.get(`${process.env.VUE_APP_FLASK_APP_URL}/projects/${this.currentUserId}`)
        .then(response => {
          this.projects = response.data;
        })
        .catch(error => {
          console.error('Error fetching projects:', error);
        });
    },
    createProject() {
      axios.post(`${process.env.VUE_APP_FLASK_APP_URL}/projects/${this.currentUserId}`, {
        ...this.newProject,
        user_id: this.currentUserId, // Make sure this is uncommented if the server expects user_id in the body
      })
      .then(response => {
        this.projects.push(response.data);
        this.newProject = { name: '', description: '', resource_dir: '' };
      })
      .catch(error => {
        console.error('Error creating project:', error);
      });
    },
  },
};
</script>

<style scoped>
.projects-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  background-color: var(--dl-color-gray-white);
}

.projects-container1 {
  flex: 1;
  width: 100%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: flex-start;
}

.projects-body {
  flex: 1;
  width: 100%;
  display: flex;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: row;
  justify-content: flex-start;
}

.projects-pagemain {
  flex: 1;
  display: flex;
  position: relative;
  align-self: stretch;
  align-items: flex-start;
  flex-direction: column;
}
</style>