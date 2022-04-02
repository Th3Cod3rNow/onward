<template>

  <div v-if="sing"><my-singup
      @success="sing_up"
      @swap="swap">

  </my-singup></div>
  <div v-else><my-register
      @success="sing_in"
      @swap="swap"
  ></my-register></div>


</template>

<script>
export default {
  name: "my-entry",
  components: {},
 data(){
    return{
      sing:false
    }
 },
  methods:{
    swap(){
      this.sing = !this.sing;
    },
    send(Username,Password,Email){
      this.$emit('send',Username,Password,Email);
    },
    sing_up(groups,Username){
      return this.$emit('sing_up',groups,Username);
    },
    sing_in(Username){

      return this.$emit('sing_in',Username);
    }
  }
}
</script>

<style scoped>

</style>