<template>
          <my-inp @input="user" class="in" placeholder="Username"></my-inp>
          <my-inp @input="pass" class="in" placeholder="Password"></my-inp>
          <my-btn
            style="width: 35%; background: chocolate; border: none; margin-right: 10%"
            @click="SendUser"
          >Sing up</my-btn>
          <my-btn style="background: chocolate; border: none; margin-right: 10%"
              @click="$emit('swap')"
          >swap</my-btn>
          <my-btn class="btn-danger" style = "border: none"
              @click="$emit('close')"
          >close</my-btn>

</template>

<script>
import axios from "axios";

export default {
  name: "my-register",
  components: {},
  data(){
    return {
      Username: '',
      Password: ''
    }
  },
  methods:{
   async SendUser() {
     const res = await axios.get('http://127.0.0.1:8888/createUser/'+'Username='+this.Username+'&Password='+this.Password);
     if(res.data.status==='success')
        return this.$emit('success',this.Username,this.Password);
     else
       return  this.$emit('not',"выберете другое имя");
   },
    user(event){
      this.Username=event.target.value;
    },
    pass(event){
      this.Password=event.target.value;
    },



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
  flex-direction: row;
}
</style>