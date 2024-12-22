<script setup>
const props = defineProps({
  text: String,
});
</script>


<template>
  <button type="button" class="button">
    {{ text }}
  </button>
</template>


<style lang="scss" scoped>
.button {

  border-style: none;
  border-radius: 100px;
  background-color: $main;
  color: #494949;
  padding: 2px 8px;

  &:hover {
    cursor: pointer;
  }

  &:active {}

  &[data-size="large"] {
    font-size: 20pt;
  }

  &[data-size="regular"] {
    font-size: 12pt;
  }

  &[data-size="small"] {
    font-size: 5pt;
  }
}
</style>
