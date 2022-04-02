<template>
<add-group
  @click="addGroup"
></add-group>
  <a class="list-group-item list-group-item-action active py-3 lh-tight" aria-current="true"  style="-webkit-user-select: none; background:  #D56A1EFF; border: none">
    <div  class="d-flex w-100 align-items-center justify-content-between" style="background:  #D56A1EFF; border: none">
      <my-inp @input="setname" placeholder="enter name"></my-inp>
    </div>
  </a>
</template>

<script>
import axios from "axios";

export default {
  name: "new_group",
  components: {},
  props:{
    Username:{
      type:[String],
      required:true
    }
  },
  data(){
    return{
      groupname:''
    }
  },
  methods: {
    async addGroup() {
      const res = await axios.get('http://127.0.0.1:8888/addGroup/' + 'Username=' + this.Username + '&Groupname=' + this.groupname)
      if (res.data.status === 'success') {
        return this.$emit('success', res.data.groups, res.data.group);
      }

    },
    setname(event){
      this.groupname=event.target.value;
    }
  }

}

</script>

<style scoped>

</style>