<template>
  <div class="feature-card1-container"
    ><img :alt="imageAlt" :src="imageSrc" class="feature-card1-image" /><h5
      class="feature-card1-text Headline5"
      >{{ cardTitle }}</h5
    ><span class="feature-card1-text1">{{ text }}</span></div
  >
</template>

<script>
export default {
  name: 'FeatureCard1',
  props: {
    cardTitle: {
      type: String,
      default: 'Title',
    },
    imageSrc: {
      type: String,
      default: 'e9dbc055-76e2-4092-9b43-b0236e095961',
    },
    imageAlt: {
      type: String,
      default: 'image',
    },
    text: {
      type: String,
      default:
        'At ThinkLink, effortlessly share research findings, resources, and insights with peers, using intuitive tools to foster seamless communication and collaboration, breaking down barriers in your academic network.',
    },
  },
}
</script>

<style scoped>
.feature-card1-container {
  width: 320px;
  margin: var(--dl-space-space-halfunit);
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: column;
}
.feature-card1-image {
  width: var(--dl-size-size-doubleunit);
  height: var(--dl-size-size-doubleunit);
  object-fit: cover;
}
.feature-card1-text {
  margin-top: var(--dl-space-space-unit);
  margin-bottom: var(--dl-space-space-unit);
}
.feature-card1-text1 {
  text-align: center;
}
</style>
