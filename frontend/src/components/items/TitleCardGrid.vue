<script setup>
const props = defineProps({
  title: String,
  country: String,
  imageUrl: String,
});

</script>

<template>
  <div class="title-card">
    <img :src="imageUrl" alt="" class="title-card__image">
    <div class="title-card__caption">
      <div class="title-card__country">{{ country }}</div>
      <div class="title-card__title">{{ title }}</div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.title-card {
  min-width: 140px;
  font-size: 10pt;

  &__image {
    width: 140px;
    height: 200px;
    background-color: $main;
    border-radius: 3px;
  }

  &__country {
    color: $font-secondary;
  }

  &__title {

    color: $font-third;
  }
}
</style>
