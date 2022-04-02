<template>
<div class="dialog">
  <div class="reg">
          <div v-if="show_message">
            <h4>{{err_mess}}
              <button type="button" class="btn-close " aria-label="Close"
                      @click="$emit('close')" ></button>
            </h4>

          </div>
        <div v-if="sing"><my-singup
            @success="sing_up"
            @swap="swap"
            @not="message">
        </my-singup></div>
        <div v-else><my-register
            @success="sing_in"
            @swap="swap"
            @not="message">
        </my-register></div>
  </div>
</div>
</template>

<script>
export default {
  name: "my-entry",
  components: {},
 data(){
    return{
      sing:false,
      show_message:false,
      err_mess:''
    }
 },
  methods:{
    swap(){
      this.sing = !this.sing;
    },
    send(Username,Password,Email){
      this.$emit('send',Username,Password,Email);
    },
    sing_up(groups,Username){
      return this.$emit('sing_up',groups,Username);
    },
    sing_in(Username){

      return this.$emit('sing_in',Username);
    },
    message(mess){
      this.show_message=true;
      this.err_mess=mess;
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
  background: blueviolet;
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