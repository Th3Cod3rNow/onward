<template>
<div class="app">
  <div class="page">
    <div class="tmp">
          <my-bar
          v-bind:groups="this.groups"
          @go="changegroup"
          @sing_up="sing_up"
          @sing_in="sing_in"
          ></my-bar>
    </div>

    <div class="menu" >
          <all-tasks
          v-bind:tasks="group.tasks"
          @open="open"
          @add_task="this.add=true"
          ></all-tasks>
    </div>
  </div>
    <full-task v-if="op"
      v-bind:task="opened"
      @close="changeop"
    ></full-task>
  <window-task-add
      v-if="add"
      @close="changeop"
      @add="add_task"
      :idG="group.id"
      :Username="user.name"
  ></window-task-add>
</div>
</template>

<script>



export default {
  name: 'App',
  components: {},
  data() {
    return {
      user:{
        email:'',
        name:'Nikita',
        password: '123456'
      },
      opened:{
          type:Object
      },
      op: false,
      add:false,

      group:{},
      groups: []
 }
  },
  methods:{
    open(task){
      this.opened = task
      this.op = true
    },
    changeop(){
      if(this.add)
        this.add = false
      if(this.op)
        this.op = false
    },
    sing_up(groups,Username,Password){
      this.groups=groups;
      this.user.name=Username;
      this.user.password=Password;
    },
    sing_in(Username,Password){
      this.user.name=Username;
      this.user.password=Password;
    },
    changegroup(group){
      this.group = group;
    },
    add_task(groups,group){
      this.groups = groups;
      this.group = group;
    }
  }
}
</script>

<style>
.tmp{
    width: 10%;
    background: #1e1e1e;
}
.menu{
    margin: 3%;
}
.page{
  display: flex;
  height: 100vh;
  background: #1a1a1a;
}
</style>
