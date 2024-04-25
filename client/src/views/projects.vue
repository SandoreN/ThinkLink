<template>
  <div class="projects-container">
    <div class="projects-container1">
      <app-header rootClassName="header-root-class-name5"></app-header>
      <div class="projects-body">
        <app-leftsidebar></app-leftsidebar>
        <div class="projects-pagemain">
          <div class="project-list">
            <div class="project-list-header" @click="toggleProjectList">
              <h2 class="project-list-heading">Your Projects</h2>
              <i class="fas" :class="{'fa-chevron-down': !isProjectListOpen, 'fa-chevron-up': isProjectListOpen}"></i>
            </div>
            <div class="project-grid-wrapper" :class="{'open': isProjectListOpen}">
              <div class="project-grid">
                <router-link
                  v-for="(project, index) in projects"
                  :key="project.id"
                  :to="`/project_workspace/${project.id}`"
                  tag="div"
                  class="project-card"
                  :style="{ animationDelay: `${index * 0.1}s` }"
                >
                  <div class="project-card-content">
                    <h3 class="project-card-title">{{ project.name }}</h3>
                    <p class="project-card-description">{{ project.description }}</p>
                    <div class="project-card-overlay"></div>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
          <div class="create-project">
            <div class="create-project-header" @click="toggleCreateProject">
              <h2 class="create-project-heading">Create a New Project</h2>
              <i class="fas" :class="{'fa-chevron-down': !isCreateProjectOpen, 'fa-chevron-up': isCreateProjectOpen}"></i>
            </div>
            <form @submit.prevent="createProject" class="project-form" :class="{'open': isCreateProjectOpen}">
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
      isProjectListOpen: true,
      isCreateProjectOpen: false,
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
        await this.fetchProjects();
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
    toggleProjectList() {
      this.isProjectListOpen = !this.isProjectListOpen;
    },
    toggleCreateProject() {
      this.isCreateProjectOpen = !this.isCreateProjectOpen;
    },
  },
  created() {
    this.fetchProjects();
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
:root {
  --sidebar-color: #6c63ff;
  --sidebar-text-color: #ffffff;
  --page-background-color: #f5f5f5;
  --project-card-background-color: #6c63ff;
  --project-card-hover-background-color: #554fd6;
  --project-card-border-color: #e0e0e0;
  --project-card-title-color: #ffffff;
  --project-card-description-color: #f0f0f0;
  --create-project-background-color: #ffffff;
  --create-project-border-color: #e0e0e0;
  --create-project-heading-color: #333333;
  --form-label-color: #4a4a4a;
  --form-input-background-color: #f5f5f5;
  --form-input-focus-shadow-color: rgba(108, 99, 255, 0.4);
  --form-highlight-color: #6c63ff;
  --create-button-background-color: #6c63ff;
  --create-button-hover-background-color: #554fd6;
  --create-button-text-color: #ffffff;
}

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
  background-color: var(--page-background-color);
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
  background-color: var(--page-background-color);
}

.project-list {
  margin-bottom: 60px;
}

.project-list-header,
.create-project-header {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.project-list-header i,
.create-project-header i {
  margin-left: 10px;
  transition: transform 0.3s ease;
}

.project-list-heading {
  font-size: 28px;
  font-weight: bold;
  margin-right: 40px;
  color: var(--sidebar-color);
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

.project-grid-wrapper {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease;
}

.project-grid-wrapper.open {
  max-height: 400px;
  overflow-y: auto;
}

.project-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  padding-right: 20px;
}

.project-card {
  position: relative;
  background-color: var(--project-card-background-color);
  border: 1px solid var(--project-card-border-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  cursor: pointer;
  width: 200px;
  animation: fadeInUp 0.6s ease forwards;
  opacity: 0;
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

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  background-color: var(--project-card-hover-background-color);
}

.project-card-content {
  padding: 20px;
  position: relative;
  z-index: 1;
}

.project-card-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: var(--project-card-title-color);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.project-card-description {
  font-size: 16px;
  color: var(--project-card-description-color);
}

.project-card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(108, 99, 255, 0.8);
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
  padding: 40px;
  background-color: var(--create-project-background-color);
  border: 1px solid var(--create-project-border-color);
  border-radius: 10px;
  box-shadow: 0 16px 32px rgba(0, 0, 0, 0.1);
  background-image: linear-gradient(135deg, var(--sidebar-color) 0%, var(--create-project-background-color) 100%);
}

.create-project-heading {
  font-size: 36px;
  font-weight: bold;
  margin-right: 40px;
  color: var(--create-project-heading-color);
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  flex-shrink: 0;
}

.project-form {
  margin-top: 50px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease;
}

.project-form.open {
  max-height: 1000px;
}

.form-group {
  position: relative;
  margin-bottom: 40px;
}

label {
  display: block;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
  color: var(--form-label-color);
}

input,
textarea {
  width: 100%;
  padding: 15px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  background-color: var(--form-input-background-color);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease, background-color 0.3s ease;
}

input:hover,
textarea:hover {
  background-color: #eeeeee;
}

input:focus,
textarea:focus {
  outline: none;
  box-shadow: 0 4px 8px var(--form-input-focus-shadow-color);
  background-color: #ffffff;
}

.input-highlight {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--form-highlight-color);
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
  padding: 20px;
  font-size: 20px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 2px;
  background-color: var(--create-button-background-color);
  color: var(--create-button-text-color);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.create-button:hover {
  background-color: var(--create-button-hover-background-color);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
</style>