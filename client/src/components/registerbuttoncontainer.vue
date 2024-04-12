<template>
  <div id="register_button_container" class="registerbuttoncontainer-register"
    ><button
      id="register_button"
      name="register_button"
      type="button"
      class="registerbuttoncontainer-button button"
      ><span class="registerbuttoncontainer-text"
        ><span>Sign up</span><br /></span></button
  ></div>
</template>

<script>
export default {
  name: 'Registerbuttoncontainer',
  props: {},
}
</script>

<style scoped>
.registerbuttoncontainer-register {
  width: 225px;
  height: 100%;
  display: flex;
  padding: 10px;
  position: relative;
  align-self: flex-end;
  align-items: center;
  flex-direction: column;
  justify-content: center;
}
.registerbuttoncontainer-button {
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
}
.registerbuttoncontainer-text {
  color: var(--dl-color-custom-primary2);
  font-size: 30px;
}
</style>
