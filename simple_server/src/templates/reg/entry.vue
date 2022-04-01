<template>
  <div v-if="sing"><my-singup></my-singup></div>
  <div v-else><my-register></my-register></div>
  <my-btn
  @click = 'swap'
  ></my-btn>
</template>

<script>
import MyBtn from "@/templates/custom/btn";
export default {
  name: "my-entry",
  components: {MyBtn},
 data(){
    return{
      sing:true
    }
 },
  methods:{
    swap(){
      this.sing = !this.sing;
    }
  }
}
</script>

<style scoped>

</style>