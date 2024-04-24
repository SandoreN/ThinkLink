<template>
  <div class="stats-card-container"
    ><img :alt="imageAlt" :src="imageSrc" class="stats-card-image" /><div
      class="stats-card-container1"
      ><h1 class="Headline4">{{ number }}</h1
      ><span class="Body1">{{ description }}</span></div
    ></div
  >
</template>

<script>
export default {
  name: 'StatsCard',
  props: {
    number: {
      type: String,
      default: '10',
    },
    description: {
      type: String,
      default: 'Description',
    },
    imageAlt: {
      type: String,
      default: 'image',
    },
    imageSrc: {
      type: String,
      default: 'a92fab0e-1be3-4dc3-847c-96e878a6375d',
    },
  },
}
</script>

<style scoped>
.stats-card-container {
  width: 200px;
  margin: var(--dl-space-space-unit);
  display: flex;
  position: relative;
  align-items: center;
  flex-direction: row;
}
.stats-card-image {
  width: 32px;
  object-fit: cover;
  margin-right: var(--dl-space-space-unit);
}
.stats-card-container1 {
  flex: 0 0 auto;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
</style>
