<template>
<div class="bar">
  <my-group v-for="group in groups"
    v-bind:key="group.id"
    v-bind:group="group"
  ></my-group>
</div>
</template>

<script>
export default {
  name: "my-bar",
  components: {},

  props:{
    groups:{
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>
.bar{
}
</style>