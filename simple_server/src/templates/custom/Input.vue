<template>
    <input :value="modelValue" @input="updateInput" class="form-control flex-nowrap" placeholder=""  aria-describedby="addon-wrapping" >
</template>

<script>
export default {
  name: "my-inp",
  props:{
    modelValue: [String]
  },
  methods:{
    updateInput(event){
      this.$emit('update:modelValue',event.target.value)
    }
  }
}
</script>

<style scoped>
</style>