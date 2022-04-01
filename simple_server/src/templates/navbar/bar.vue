<template>
<div class="bar">
  <my-group v-for="group in groups"
    v-bind:key="group.id"
    v-bind:group="group"
            @click="$emit('go',group)"
  ></my-group>
  <my-entry v-if="show" @send="entry"></my-entry>
  <my-btn
      @click="this.show=true"
      v-else-if="btnshow">sing up</my-btn>
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
  },
  data(){
    return{
      show:false,
      btnshow:true
    }
  },
  methods:{
    entry(Username,Password,Email){
      this.btnshow=false;
      this.show=false;
      return this.$emit('send',Username,Password,Email);
    }
  }
}
</script>

<style scoped>
.bar{
}
</style>