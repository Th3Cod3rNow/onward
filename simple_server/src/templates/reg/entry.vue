<template>

  <div v-if="sing"><my-singup @send="send" @swap="swap"></my-singup></div>
  <div v-else><my-register @send="send" @swap="swap"></my-register></div>


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
      if(this.sing)
        this.sing = false;
      else
        this.sing=true;
    },
    send(Username,Password,Email){
      this.$emit('send',Username,Password,Email);
    }
  }
}
</script>

<style scoped>

</style>