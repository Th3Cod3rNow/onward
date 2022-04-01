<template>
  <div class="dialog">
      <div class="reg">
          <my-inp class="in" placeholder="Email"></my-inp>
          <my-inp class="in" placeholder="Username"></my-inp>
          <my-inp class="in" placeholder="Password"></my-inp>
          <my-btn
            @click="SendUser"
          >Sing In</my-btn>
          <my-btn
              @click="$emit('swap')"
          >swap</my-btn>
      </div>

  </div>
</template>

<script>
export default {
  name: "my-register",
  components: {},
  props:{
      Email:[String],
      Username:[String],
      Password:[String]
  },
  methods:{
    SendUser(){
      this.$emit('send',this.Username,this.Password,this.Email,)
    }
  }
}
</script>

<style scoped>
.dialog{
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  margin: auto ;
  max-width: 20%;
  max-height: 12%;
  -webkit-user-select: none;
}
.reg{
  position: center;
  background: black;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
}

.in{
  margin-bottom: 10px;
}
.btn{
  margin: auto;
  flex-direction: row;
}
</style>