<template>
<div>
  <div class="col">
    <div class="task" >
      <div class="card">
        <my-btn>add</my-btn>
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