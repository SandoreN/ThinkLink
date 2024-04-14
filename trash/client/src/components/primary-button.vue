<template>
  <div class="primary-button-container"
    ><button class="primary-button-button MediumLabel button"
      >{{ button }}</button
    ></div
  >
</template>

<script>
export default {
  name: 'PrimaryButton',
  props: {
    button: {
      type: String,
      default: 'Button',
    },
  },
}
</script>

<style scoped>
.primary-button-container {
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.primary-button-button {
  color: var(--dl-color-gray-white);
  align-self: center;
  transition: 0.3s;
  padding-top: 12px;
  border-width: 0px;
  padding-left: 32px;
  border-radius: var(--dl-radius-radius-radius6);
  padding-right: 32px;
  padding-bottom: 12px;
  background-color: var(--dl-color-purple-default);
}


</style>
