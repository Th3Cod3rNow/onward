<template>
  <div class="col">
    <div class="card shadow-sm" style="width: 350px; height: 300px">
      <div class="card-body">
        <h3 class="card-text">{{ title }}</h3>
        <hr>
        <h5 >{{body}}</h5>
      <my-btn>open</my-btn>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "prev-task",
  components: {},
  props:{
    title:[String],
    body: [String]
  }
}
</script>

<style scoped>
.pre{
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  max-width: 15%;
  max-height: 20%;
  -webkit-user-select: none;
}

</style>