<template>
  <a class="list-group-item list-group-item-action active py-3 lh-tight" aria-current="true"  style="-webkit-user-select: none;">
    <div @click="click" class="d-flex w-100 align-items-center justify-content-between">
      <strong class="mb-1">{{ group.name }}</strong>
    </div>
  </a>
</template>

<script>
export default {
  name: "my-group",
  props:{
    group:{
      type: Object,
      required: true
    }
  },
  methods:{
    click(){
      return this.$emit('click');
    }
  }
}
</script>

<style scoped>
.group{
  width: 70%;

}
</style>