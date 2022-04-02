<template>

</template>

<script>
import axios from "axios";

export default {
  name: "new_group",
  data(){
    return{
      groupname:''
    }
  },
  methods:{
    async addGroup(){
      const res =await axios.get('http://127.0.0.1:8888/addGroup/'+'Username='+this.Username+'&Groupname='+this.groupname)
      if(res.data.status ==='success'){
        return this.$emit('success',res.data.groups,res.data.group);
    }

  }

}

</script>

<style scoped>

</style>