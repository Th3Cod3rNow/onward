<template>
      <my-inp @input="user" class="in" placeholder="Username"></my-inp>
      <my-inp @input="pass"  class="in" placeholder="Password"></my-inp>
      <my-btn
        @click="SendUser"
      >Sing in</my-btn>

      <my-btn
          @click="$emit('swap')"
      >swap</my-btn>
</template>

<script>
import axios from "axios";

export default {
  name: "my-singup",
  data(){
    return{
      Username: '',
      Password: ''
    }
  },
  methods:{
    async SendUser(){
      const res = await axios.get('http://127.0.0.1:8888/login/'+'Username='+this.Username+'&Password='+this.Password);

      if(res.data.status==='success')
        return this.$emit('success',res.data.groups,this.Username);
      else
        return this.$emit('not','пользовательне найден');
    },
    user(event){
      this.Username=event.target.value;
    },
    pass(event){
      this.Password=event.target.value;
    }
  }
}
</script>

<style scoped>
.dialog{
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  margin: auto ;
  max-width: 20%;
  max-height: 12%;
  -webkit-user-select: none;
}
.reg{
  position: center;
  background: black;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}

.in{
  margin-bottom: 10px;
}
.btn{
  margin: auto;
}
</style>