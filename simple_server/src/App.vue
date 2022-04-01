<template>
    <div class="app">

  <div class="tmp">
        <my-bar></my-bar>
      <div class="menu">
        <all-tasks
        v-bind:tasks="tasks"
        ></all-tasks>
      </div>
  </div>
    </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data() {
    return {
      tasks: [
        {id: 0, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 1, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 2, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 3, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 4, title: 'название', body: 'Описание', status: 'никто не выполняет'},
        {id: 5, title: 'название', body: 'Описание', status: 'никто не выполняет'},

      ],
      user:{
        email:'timafaer@gamil.com',
        name:'timafaer',
        password: 'qwerty'
      }
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
