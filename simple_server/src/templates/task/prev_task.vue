<template>
  <div class="col">
    <div class="task" >
      <div class="card">
        <h3 class="card-text">{{ task.title }}</h3>
        <hr>
        <h5 class="card-text" >{{task.body}}</h5>
      <my-btn
      @click="$emit('open',task)"
      >open</my-btn>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "prev-task",
  components: {},
  props:{
    task:{
      type:Object,
      required:true
    }
  },
}
</script>

<style scoped>
.pre{
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  -webkit-user-select: none;
}
.task{
  -webkit-user-select: none;
  display: block;
  position: static;
  margin: 2vh 5vw;
  width: 20vw;
  height: 20vh;
}
.card{

  width: 20vw;
  height: 20vh;

  position: absolute;
}
.card-text{
  margin: 1vh 1vw;
  max-height: 20vh;
}
</style>