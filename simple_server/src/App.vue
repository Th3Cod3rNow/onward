<template>
    <div class="app">

  <div class="tmp">
        <my-bar></my-bar>
      <div class="menu" >
        <all-tasks
        v-bind:tasks="tasks"
        @open="open"
        ></all-tasks>
      </div>
    <full-task v-if="op"
      v-bind:task="opened"
      @close="changeop"
    ></full-task>
  </div>
    </div>
</template>

<script>
import FullTask from "@/templates/task/full_task";
export default {
  name: 'App',
  components: {FullTask},
  data() {
    return {
      tasks: [
        {id: 0, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 1, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 2, title: 'r', body: 'Описание', status: 'никто не выполняет'},
        {id: 3, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 4, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 5, title: 'название', body: 'Описание', status: 'никто не выполняет'},

      ],
      user:{
        email:'timafaer@gamil.com',
        name:'timafaer',
        password: 'qwerty'
      },
      opened:{
          type:Object
      },
      op: false
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
    }
  }
}
</script>

<style>
.tmp{
  display: flex;

}
.menu{
}
</style>
