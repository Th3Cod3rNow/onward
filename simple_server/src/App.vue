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
          ></all-tasks>
    </div>
  </div>
    <full-task v-if="op"
      v-bind:task="opened"
      @close="changeop"
    ></full-task>
  <window-task-add
      v-if="adding"
      @close="changeop"
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
      adding:false,

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
      if(this.op)
        this.op = false
    },
    sing_up(groups,Username){
      this.groups=groups;
      this.user.name=Username;
    },
    sing_in(Username){
      this.user.name=Username;
    },
    changegroup(group){
      this.group = group;
    },

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
