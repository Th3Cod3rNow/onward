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
            @not="message"
            @close="close">
        </my-singup></div>
        <div v-else><my-register
            @success="sing_in"
            @swap="swap"
            @not="message"
            @close="close">

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
    sing_up(groups,Username,Password){
      return this.$emit('sing_up',groups,Username,Password);
    },
    sing_in(Username,Password){

      return this.$emit('sing_in',Username,Password);
    },
    message(mess){
      this.show_message=true;
      this.err_mess=mess;
    },
    close(){
      return this.$emit('close');
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
  flex-direction: row;
}
</style>