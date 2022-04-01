<template>
<div>
      <div class="full">
        <button type="button" class="btn-close " aria-label="Close"
        @click="$emit('close')"
        ></button>

        <h3>{{task.title}}</h3>
        <hr>
        <h4>{{task.body}}</h4>
        <hr>
        <h5>{{task.status}}</h5>
      </div>
</div>
</template>

<script>
export default {
  name: "full-task",
  props:{
    task: {
      id:[String],
      title: [String],
      body: [String],
      status: [String]
    }
  },

}
</script>

<style scoped>
.full{
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  margin: auto ;
  max-width: 30%;
  max-height: 80%;
  -webkit-user-select: none;
  background: blue;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}
</style>