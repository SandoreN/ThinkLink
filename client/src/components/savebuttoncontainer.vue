<template>
    <div id="save_button_container" class="savebuttoncontainer">
        <button
        id="save_button"
        name="save_button"
        type="button"
        class="savebuttoncontainer-button button"
        @click="$emit('click')"
        ><span class="savebuttoncontainer-text"
          ><span>Save</span><br /></span>
        </button>
    </div>
</template>
  
<script>
export default {
    name: 'savebuttoncontainer',
    props: {},
  }
</script>
  
<style scoped>
  .savebuttoncontainer {
    width: 225px;
    height: 75px;
    display: flex;
    position: relative;
    padding: 10px;
    align-self: flex-start;
    align-items: flex-start;
    flex-direction: column;
    justify-content: left;
  }
  .savebuttoncontainer-button {
    color: var(--dl-color-gray-white);
    width: 200px;
    height: 100%;
    font-size: 30px;
    align-self: center;
    font-style: normal;
    font-weight: 700;
    padding-top: 0px;
    border-color: var(--dl-color-custom-primary2);
    border-width: 2px;
    padding-left: 0px;
    padding-right: 0px;
    padding-bottom: 0px;
    background-color: transparent;
    cursor: pointer;
  }
  .savebuttoncontainer-text {
    color: var(--dl-color-custom-primary2);
    font-size: 30px;
  }
  </style>r