<template>
  <div>
    <div class="full">
      <button type="button" class="btn-close " aria-label="Close"
              @click="$emit('close')"
      ></button>

      <my-inp></my-inp>
      <hr>
      <my-inp></my-inp>
      <hr>
      <my-inp></my-inp>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "window-task-add",
  components: {},
  props:{
    Username:[String],
    idG:[Number,String]
  },
  data(){
    return{
      task:{
        type:Array
      }
    }
  },
  methods:{
    async addTask(){
      axios.get('http://127.0.0.1:8888/addTask/'+'Username='+this.Username+'&Taskname='+ this.task.name + '&Body=' + this.task.body + '&idGroup'+ this.idG);
      return this.$emit('add',this.task);
    }
  }
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