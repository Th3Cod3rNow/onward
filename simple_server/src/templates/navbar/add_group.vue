<template>
  <a class="list-group-item list-group-item-action active py-3 lh-tight" aria-current="true" style="background: #ef7722; border: none">
    <div @click="$emit('click')" class="d-flex w-100 align-items-center justify-content-between" style="border: none">
      <strong class="mb-1" style="-webkit-user-select: none;">Add group</strong>
    </div>
  </a>
</template>

<script>
export default {
  name: "add-group"
}
</script>

<style scoped>
.group{
  width: 80%;
}
</style>