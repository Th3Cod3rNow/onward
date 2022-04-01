<template>
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <prev-task  v-for="task in tasks"
        v-bind:task="task"
        @open="$emit('open',task)"
        v-bind:key="task.id"
       >
      </prev-task>
    </div>
  </div>
</template>

<script>
export default {
  name: "all-tasks",
  components: {},

  props:{
    tasks:{
      type:Array,
      required: true
    }
  }
}
</script>

<style scoped>
.ul{

}
</style>