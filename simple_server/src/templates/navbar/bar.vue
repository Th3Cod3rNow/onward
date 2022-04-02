<template>
  <div class="d-flex flex-column align-items-stretch flex-shrink-0" style="width: 10vw;height: 100vh; background: #c4631c">
    <a href="/" class="d-flex align-items-center flex-shrink-0 p-3 link-dark text-decoration-none border-bottom">
      <svg class="bi me-2" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
      <span class="fs-5 fw-semibold" style="color: white">List group</span>
    </a>
    <div class="list-group list-group-flush border-bottom scrollarea">
      <my-entry
          v-if="show"
          @sing_in="sing_in"
          @sing_up="sing_up"
          @close="this.show=false"
      ></my-entry>
      <my-btn
          style=""

          @click="this.show=true"
          v-else-if="btnshow">sing up
      </my-btn>
      <my-group
          v-for="group in groups"
          v-bind:key="group.id"
          v-bind:group="group"
          @click="$emit('go',group)"
      ></my-group>
      <add-group></add-group>
    </div>
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
    sing_up(groups,Username){
      this.show = false;
      return this.$emit('sing_up',groups,Username);
    },
    sing_in(Username,Password){
      this.show = false;
      return this.$emit('sing_in',Username,Password);
    }
  }
}
</script>

<style scoped>
.bar{
  background: chocolate;
  width: 10vw;
  height: 100vh;
}
.btn{
  background: #ef7722; border: none;
}
</style>