<template>
<div>
  <div class="col">
    <div class="task" >
      <div class="card" style="width: 18rem; border: none">
        <div class="card-body" style="background: #313131">
          <h5 class="card-title-text" style="color:white">Добавить новое задание</h5>
        <a class="btn btn-success" style="background: #353535; border: none">Add</a>
          </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "add-task",
  components: {}
}
</script>

<style scoped>
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
</style>