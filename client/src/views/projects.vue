<template>
  <div class="projects-container">
    <div class="projects-container1">
      <app-header rootClassName="header-root-class-name5"></app-header>
      <div class="projects-body">
        <app-leftsidebar></app-leftsidebar>
        <div class="projects-pagemain">
          <div class="project-list">
            <h2 class="project-list-heading">Your Projects</h2>
            <div class="project-grid">
              <router-link
                v-for="project in projects"
                :key="project.id"
                :to="`/project_workspace/${project.id}`"
                tag="div"
                class="project-card"
              >
                <div class="project-card-content">
                  <h3 class="project-card-title">{{ project.name }}</h3>
                  <p class="project-card-description">{{ project.description }}</p>
                  <div class="project-card-overlay"></div>
                </div>
              </router-link>
            </div>
          </div>
          <div class="create-project">
            <h2 class="create-project-heading">Create a New Project</h2>
            <form @submit.prevent="createProject" class="project-form">
              <div class="form-group">
                <label for="project-name">Project Name:</label>
                <input type="text" id="project-name" v-model="newProject.name" required>
                <span class="input-highlight"></span>
              </div>
              <div class="form-group">
                <label for="project-description">Project Description:</label>
                <textarea id="project-description" v-model="newProject.description" rows="4"></textarea>
                <span class="input-highlight"></span>
              </div>
              <button type="submit" class="create-button">Create Project</button>
            </form>
          </div>
        </div>
        <app-rightsidebar></app-rightsidebar>
      </div>
    </div>
  </div>
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
      newProject: {
        name: '',
        description: '',
      },
    };
  },
  methods: {
    async createProject() {
      try {
        const response = await axios.post(
        `${process.env.VUE_APP_FLASK_APP_URL}/projects/${this.$store.state.user.id}`,
      {
        name: this.newProject.name,
        description: this.newProject.description,
        resource_dir: this.$store.state.user.id.toString(),
      }
    );
    this.newProject.name = '';
    this.newProject.description = '';
    this.projects.unshift(response.data); // Add the newly created project to the beginning of the array
  } catch (error) {
    console.error('Error creating project:', error);
  }
},
    async fetchProjects() {
      try {
        const response = await axios.get(`${process.env.VUE_APP_FLASK_APP_URL}/projects/${this.$store.state.user.id}`);
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    },
  },
  created() {
    this.fetchProjects(); // Fetch projects when the component is created
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
  padding: 40px;
}


.project-list {
  margin-bottom: 60px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.project-list-heading {
  font-size: 36px;
  font-weight: bold;
  margin-right: 40px;
  color: #333;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

.project-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
}

.project-card {
  position: relative;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  cursor: pointer;
  width: 300px;
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 16px 32px rgba(0, 0, 0, 0.3);
}

.project-card-content {
  padding: 30px;
  position: relative;
  z-index: 1;
}

.project-card-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.project-card-description {
  font-size: 18px;
  color: #666;
}

.project-card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 123, 255, 0.8);
  opacity: 0;
  transition: opacity 0.4s ease;
  pointer-events: none;
}

.project-card:hover .project-card-overlay {
  opacity: 1;
}

.create-project {
  max-width: 800px;
  margin: 0 auto;
  padding: 60px;
  background-color: #f8f8f8;
  border-radius: 10px;
  box-shadow: 0 16px 32px rgba(0, 0, 0, 0.1);
  animation: fadeInUp 0.6s ease;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.create-project-heading {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 50px;
  color: #333;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

.project-form {
  margin-top: 50px;
}

.form-group {
  position: relative;
  margin-bottom: 50px;
}

label {
  display: block;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

input,
textarea {
  width: 100%;
  padding: 20px;
  font-size: 20px;
  border: none;
  border-radius: 4px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

input:focus,
textarea:focus {
  outline: none;
  box-shadow: 0 8px 16px rgba(0, 123, 255, 0.4);
}

.input-highlight {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #007bff;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

input:focus + .input-highlight,
textarea:focus + .input-highlight {
  transform: scaleX(1);
}

.create-button {
  display: block;
  width: 100%;
  padding: 24px;
  font-size: 24px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 2px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 123, 255, 0.4);
}

.create-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 123, 255, 0.6);
}
</style>