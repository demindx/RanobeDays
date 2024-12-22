<script setup>
import TitleCardGrid from "./components/items/TitleCardGrid.vue";

</script>

<template>
  <div class="carousel">
    <div class="carousel__wrapper">
      <TitleCardGrid v-for="item in 14" class="carousel__item" title="title" country="China"
        image-url="https://remanga.org/media/titles/one_hundred_to_make_god/86a77e61b95507bda3d352fb3dbbbb65.jpg" />
    </div>
  </div>
  <div class="main">
    <div class="main__left">
    </div>
    <div class="main__right">
    </div>
  </div>
</template>

<style lang="scss" scoped>
.carousel {
  // width: fit-content;
  // margin: 0 auto;

  &__wrapper {
    display: flex;
  }

  &__item {
    margin: 10px;
  }
}
</style>
