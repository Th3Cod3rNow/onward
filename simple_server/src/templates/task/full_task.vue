<template>
<div>
      <div class="full">
        <button type="button" class="btn-close " aria-label="Close"
        @click="$emit('close')"
        ></button>

        <h3 style="color: white">{{task[1]}}</h3>
        <hr style="background: chocolate; height: 0.25rem">
        <h4 style="color: lightgray">{{task[2]}}</h4>
        <hr style="background: dimgray; height: 0.25rem">
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
  background: #363636;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;

}
</style>