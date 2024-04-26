<template>
  <div class="projectworkspace-container">
    <div class="projectworkspace-container1">
      <app-header rootClassName="header-root-class-name5"></app-header>
      <div class="projectworkspace-body">
        <app-leftsidebar></app-leftsidebar>
        <div class="projectworkspace-pagemain">
          <input class="draft-name-input" v-model="draftName" placeholder="Enter draft name" />
          <div v-html="compiledMarkdown" class="markdown-preview"></div>
          <textarea id="markdown-editor" v-model="markdown"></textarea>
          <savedraftbuttoncontainer @click="saveDraft"></savedraftbuttoncontainer>
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
import Savedraftbuttoncontainer from '../components/savedraftbuttoncontainer'
import { ref, computed } from 'vue';
import MarkdownIt from 'markdown-it';
import jsPDF from 'jspdf';

export default {
  name: 'Projectworkspace',
  components: {
    AppHeader,
    AppLeftsidebar,
    AppRightsidebar,
    Savedraftbuttoncontainer
  },
    setup() {
    const draftName = ref('');
    const markdown = ref('');
    const md = MarkdownIt();

    const compiledMarkdown = computed(() => {
      return md.render(markdown.value);
    });

    const saveDraft = () => {
      const doc = new jsPDF();
      doc.text(markdown.value, 10, 10);
      doc.save(`${draftName.value}.pdf`);
    };

    return {
      draftName,
      markdown,
      compiledMarkdown,
      saveDraft,
    };
  },
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
  align-items: stretch;
  flex-direction: row;
  justify-content: flex-start;
}

.projectworkspace-pagemain {
  justify-content: center;
  align-items: flex-start;
  align-self: stretch;
  flex-direction: row;
  padding-top: 30px;
  width: 800px;
  flex: 1;
  margin: 0 auto; 
  position: relative;

}

#markdown-editor {
  width: 100%; /* fill the parent div */
  height: 100%; /* fill the parent div */
}

.projectworkspace-projectsidebar {
  flex: 0 0 auto;
  width: 225px;
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
  overflow-y: auto; /* Add a scrollbar if the content is too long to fit in the pane */
  height: 200px;
  border: 1px solid black;
}
</style>
