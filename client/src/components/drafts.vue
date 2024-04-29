<template>
    <input class="draft-name-input" v-model="draftName" placeholder="Enter draft name" />
    <div v-html="compiledMarkdown" class="markdown-preview"></div>
    <textarea id="markdown-editor" v-model="markdown"></textarea>
    <!--<loadbuttoncontainer class="load-button" @click="load"></loadbuttoncontainer>
    <ul>
        <li v-for="draft in drafts" :key="draft.id">
            {{ draft.name }}
        </li>
    </ul>
    <savebuttoncontainer class="save-button" @click="save"></savebuttoncontainer>
-->
</template>
  
<script>
import loadbuttoncontainer from '../components/loadbuttoncontainer'
import savebuttoncontainer from '../components/savebuttoncontainer'
import { ref, computed, watch } from 'vue';
import MarkdownIt from 'markdown-it';
import { jsPDF } from 'jspdf';
import axios from 'axios';

export default {
    name: 'Drafts',
    components: {
        savebuttoncontainer,
        loadbuttoncontainer
    },
    props: {
        project_id: {
            type: String,
            required: true,
        },
    },
    setup(props) {
        const draftName = ref('');
        const markdown = ref('');
        const md = new MarkdownIt();
        const project_id = ref(props.project_id);
        const drafts = ref([]);

        watch(props, (newProps) => {
            project_id.value = newProps.project_id;
        });

        const compiledMarkdown = computed(() => {
            return md.render(markdown.value);
        });
        
        const load = async () => {
            try {
                const response = await axios.get(`${process.env.VUE_APP_FLASK_APP_URL}/project_workspace/${props.project_id}`)
                console.log('Server response:', response.data);
                if (response.status === 200) {
                    console.log('response.data.drafts:', response.data.drafts); 
                    drafts.value = response.data.drafts;
                } else {
                    console.log('Failed to load drafts');
                }
            } catch (error) {
                console.error('An error occurred while loading drafts:', error);
            }
        };

        const loadDraft = (draft) => {
            markdown.value = draft.content;
        }

        const save = async () => {
            const doc = new jsPDF();
            doc.html(markdown.value, options);
            const pdf = doc.output('blob');
            const options = {
                x: 10,
                y: 10,
                callback: function () {
                    // This will be called when the conversion is done
                }
            };


            try {
                const formData = new FormData();
                formData.append('action', 'create_draft');
                formData.append('file', pdf, `${draftName.value}.pdf`);
                formData.append('file_data', JSON.stringify({
                    content: markdown.value,
                    filename: `${draftName.value}.pdf`
                }));
                console.log('formData:', formData);

                const response = await axios.post(`${process.env.VUE_APP_FLASK_APP_URL}/project_workspace/${props.project_id}`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                if (response.status === 200) {
                    console.log('Draft saved successfully');
                } else {
                    console.log('Failed to save draft');
                }
            } catch (error) {
                console.error('An error occurred while saving the draft:', error);
            }
        };
        
        return {
            draftName,
            markdown,
            compiledMarkdown,
            save,
            drafts,
            load,
            loadDraft
        };
    },
};
</script>

<style scoped>
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
  display: flex;
  width: 500px;
  height: 450px;
  border: 1px solid black;
}

.draft-name-input {
  height: 55px;
  padding: 10px;
  font-size: 30px;
  margin-bottom: 20px;
  border: 2px solid black;
  border-radius: 4px;
  align-items: center;
  justify-content: center;
}

.markdown-preview {
  margin-top: 10px;
  margin-bottom: 10px;
  overflow-y: auto;
  height: 200px;
  width: 500px;
  border: 1px solid black;
}

.save-button {
  align-self: center;
}

.load-button {
  align-self: center;
}
</style>