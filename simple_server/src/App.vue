<template>
<div class="app">
  <div class="page">
    <div class="tmp">
          <my-bar
          v-bind:groups="this.groups"
          @go="changegroup"
          @send="reglog"
          ></my-bar>
    </div>

    <div class="menu" >
          <all-tasks
          v-bind:tasks="group.tasks"
          @open="open"
          ></all-tasks>
    </div>
  </div>
    <full-task v-if="op"
      v-bind:task="opened"
      @close="changeop"
    ></full-task>
  <my-btn
  @click="getTasks"
  >send</my-btn>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  components: {},
  data() {
    return {
      user:{
        email:'',
        name:'',
        password: ''
      },
      opened:{
          type:Object
      },
      op: false,


      group:{
        id: 0,
        name: 'some',
        tasks : [{id: 0, title: 'название', body: 'Описание', status: 'никто не выполняет'}],
        users : [{id: 0, username: "user" , Email: "@mail.com"}]
      },
      groups: []
 }
  },
  methods:{
    open(task){
      this.opened = task
      this.op = true
    },
    changeop(){
      if(this.op)
        this.op = false
    },
    async getTasks(){
          try{
              const response = await axios.get('http://127.0.0.1:8888/Groups');
              this.groups = response.data.groups;
              console.log(response)
          }catch (e){
                alert('error')
          }
    },
    mounted(){
      this.getTasks();
    },
    changegroup(group){
      this.group = group;
    },
    reglog(Username,Password,Email){
      this.user.name=Username;
      this.user.password=Password;
      if(Email.length>0)
        this.user.email=Email;

    }

  }
}
</script>

<style>
.tmp{
    width: 10%;
    background: white;
}
.menu{
    margin: 3%;
}
.page{
  display: flex;
  height: 100vh;
  background: green;
}
</style>
