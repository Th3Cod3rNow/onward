<template>
  <div class="col">
    <div class="card shadow-sm" style="width: 350px; height: 300px">
      <div class="card-body">
        <h3 class="card-text">{{ task.title }}</h3>
        <hr>
        <h5 >{{task.body}}</h5>
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
  max-width: 15%;
  max-height: 20%;
  -webkit-user-select: none;
}

</style>