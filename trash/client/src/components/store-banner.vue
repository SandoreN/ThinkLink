<template>
  <div class="store-banner-store-banner"
    ><img :alt="imageAlt1" :src="imageSrc1" class="store-banner-image" /><img
      :alt="imageAlt"
      :src="imageSrc"
      class="store-banner-image1"
  /></div>
</template>

<script>
export default {
  name: 'StoreBanner',
  props: {
    imageAlt1: {
      type: String,
      default: 'image',
    },
    imageAlt: {
      type: String,
      default: 'image',
    },
    imageSrc: {
      type: String,
      default: 'a78f3331-ffb7-4d77-bad3-60f013f62c40',
    },
    imageSrc1: {
      type: String,
      default: '4a5d6ca8-cd8a-4487-a3de-c71224c4b944',
    },
  },
}
</script>

<style scoped>
.store-banner-store-banner {
  display: flex;
  align-items: flex-start;
  flex-direction: row;
  justify-content: space-between;
}
.store-banner-image {
  width: 135px;
  object-fit: cover;
}
.store-banner-image1 {
  width: 135px;
  object-fit: cover;
  margin-left: var(--dl-space-space-halfunit);
}
</style>
