<template>
    <div>
      <button class="projectsidebarinner-container" @click="changeTab('Drafts')">Drafts</button>
      <button class="projectsidebarinner-container" @click="changeTab('Tasks')">Tasks</button>
      <button class="projectsidebarinner-container" @click="changeTab('Resources')">Resources</button>
    </div>
</template>
  
<script>
export default {
methods: {
    changeTab(tab) {
    this.$emit('change-tab', tab);
    }
}
};
</script>

<style scoped>
.projectsidebarinner-sidebar {
flex: 1;
width: 225px;
height: 100%;
display: flex;
align-self: stretch;
align-items: stretch;
flex-direction: column;
justify-content: flex-start;
background-color: rgba(4, 0, 72, 0.31);
}
.projectsidebarinner-sidebarheader {
width: 225px;
height: 76px;
display: flex;
align-self: flex-start;
align-items: center;
margin-left: 0px;
padding-top: 10px;
flex-direction: column;
padding-bottom: 10px;
justify-content: center;
background-color: #d5d5e1;
}
.projectsidebarinner-container {
width: 199px;
height: 100%;
display: flex;
align-self: center;
align-items: center;
flex-direction: column;
vertical-align: center;
justify-content: center;
}
.projectsidebarinner-navlink {
flex: 1;
height: 100%;
display: flex;
padding: 0px;
align-self: stretch;
align-items: center;
border-width: 0px;
flex-direction: column;
justify-content: center;
text-decoration: none;
background-color: transparent;
}
.projectsidebarinner-text {
font-size: 20px;
align-self: center;
font-style: normal;
text-align: center;
font-weight: 600;
margin-left: 0px;
margin-bottom: 0px;
}

.projectsidebarinner-icon {
width: 40px;
height: 40px;
align-self: center;
margin-top: 0px;
padding-top: 2px;
margin-bottom: 0px;
padding-bottom: 2px;
background-color: transparent;
}
.projectsidebarinner-text02 {
font-size: 22px;
align-self: center;
font-style: normal;
text-align: left;
font-family: "Inter";
font-weight: 700;
margin-left: 8px;
}
.projectsidebarinner-container3 {
flex: 0 0 auto;
width: auto;
height: auto;
display: flex;
align-self: flex-start;
align-items: flex-start;
padding-top: 5px;
padding-bottom: 5px;
justify-content: center;
background-color: transparent;
}
@media(max-width: 991px) {
.projectsidebarinner-sidebarheader {
    padding-left: var(--dl-space-space-halfunit);
    padding-right: var(--dl-space-space-halfunit);
}
}
@media(max-width: 479px) {
.projectsidebarinner-sidebarheader {
    width: auto;
    align-self: stretch;
    align-items: center;
    justify-content: center;
}
.projectsidebarinner-container {
    align-self: center;
    align-items: center;
    justify-content: center;
}
}
</style>