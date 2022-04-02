<template>
  <div>
    <div class="full">
      <button type="button" class="btn-close " aria-label="Close"
              @click="$emit('close')"
      ></button>

      <my-inp @input="mane" placeholder="название"></my-inp>
      <hr>
      <my-inp @input="descr" placeholder="Описание"></my-inp>
      <hr>
      <my-btn @click="addTask">add_task</my-btn>
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
      const res =await axios.get('http://127.0.0.1:8888/addTask/'+'Username='+this.Username+'&Taskname='+ this.task.name + '&Body=' + this.task.body + '&idGroup='+ this.idG);
      if(res.data.status ==='success'){
          return this.$emit('success',res.data.groups,res.data.group);
      }
    },
    mane(event){
      this.task.name = event.target.value;
    },
    descr(event){
      this.task.body = event.target.value;
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
  background: #8888AA;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}
</style>