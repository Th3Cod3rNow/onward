<template>
  <button class="group">{{group.name}}</button>

</template>

<script>
export default {
  name: "my-group",
  props:{
    group:{
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.group{
  width: 100%;
  height: 100%;
}
</style>