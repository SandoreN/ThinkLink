<template>
  <nav class="navigation-links1-nav" v-bind:class="rootClassName"
    ><span class="navigation-links1-text">{{ text }}</span
    ><span class="navigation-links1-text1">{{ text1 }}</span
    ><span class="navigation-links1-text2">{{ text2 }}</span
    ><span class="navigation-links1-text3">{{ text3 }}</span
    ><span class="navigation-links1-text4">{{ text4 }}</span></nav
  >
</template>

<script>
export default {
  name: 'NavigationLinks1',
  props: {
    text3: {
      type: String,
      default: 'Team',
    },
    text4: {
      type: String,
      default: 'Blog',
    },
    rootClassName: String,
    text2: {
      type: String,
      default: 'Pricing',
    },
    text1: {
      type: String,
      default: 'Features',
    },
    text: {
      type: String,
      default: 'About',
    },
  },
}
</script>

<style scoped>
.navigation-links1-nav {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.navigation-links1-text1 {
  margin-left: var(--dl-space-space-twounits);
}
.navigation-links1-text2 {
  margin-left: var(--dl-space-space-twounits);
}
.navigation-links1-text3 {
  margin-left: var(--dl-space-space-twounits);
}
.navigation-links1-text4 {
  margin-left: var(--dl-space-space-twounits);
}








@media(max-width: 767px) {
  .navigation-links1-nav {
    align-items: flex-start;
    flex-direction: column;
  }
  .navigation-links1-text {
    margin-bottom: var(--dl-space-space-unit);
  }
  .navigation-links1-text1 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .navigation-links1-text2 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .navigation-links1-text3 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
  .navigation-links1-text4 {
    margin-left: 0;
    margin-bottom: var(--dl-space-space-unit);
  }
}
</style>
