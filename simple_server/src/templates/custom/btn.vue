<template>
  <button type="button" class="btn btn-success">
    <strong><slot></slot></strong>
  </button>
</template>

<script>
export default {
  name: "my-btn",
  }


</script>

<style scoped>
.btn{
  border-radius: 4px;
  border-color: black;
  padding: 2px;
}
</style>