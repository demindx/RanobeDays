<script setup>
const props = defineProps({
  image: String
})
</script>

<template>
  <div class="w-fit">
    <img :src="image" alt="" class="rounded-full size-24 shadow-inner bg-green-200 shadow-background">
    <div class="w-full text-center">
      <slot></slot>
    </div>
  </div>
</template>
