<template>
  <div class="col">
    <div class="task" >
      <div class="card" style="width: 18rem; border: none">
        <div class="card-body" style="background: #313131">
        <h5 class="card-title-text" style="color:white">{{ task[1] }}</h5>
<!--        <hr>-->
        <p class="card-text" style="color: whitesmoke">{{task[2]}}</p>
      <a class="btn btn-success" style="background: #353535; border: none"
      @click="$emit('open',task)"
      >open</a>
        </div>
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