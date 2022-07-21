<template>
    <div id="Subscribe" :style="theme">
      <span style="font-size:1rem; letter-spacing: 0.1em; text-align: left; margin-left: 2rem">
        <strong style="font-size: 2rem">Be the first to know about <i>crypto news every day</i></strong><br><br>
Get crypto analysis, news and updates right to your inbox!<br> Sign up here so you don't miss a single newsletter.<br><br>
      <vs-input state="success" success v-model="val" placeholder="Email" style="display: inline-block;">
        <template #icon>
          <i class='bx-user'></i>
          <EmailReceiveOutline />
        </template>
      </vs-input>
        <vs-button
            style="display: inline-block;"
            success
            :active="active === 1"
            @click="active = 1; fetchURL()"
        >Subscribe</vs-button>
    </span>
      <div></div>
      <div style="background: linear-gradient(90deg,#fff0,#38dc34)"></div>
      <vs-dialog blur not-close auto-width not-padding v-model="alert">
        <div class="con-image" style="padding: 1rem">
          <strong>Input your email, firstly 😅</strong>
        </div>
      </vs-dialog>
    </div>
</template>

<script>
import EmailReceiveOutline from 'vue-material-design-icons/EmailReceiveOutline.vue';

export default {
  name: "Subscribe",
  components: {
    EmailReceiveOutline,
  },
  props: {
    theme: String
  },
  data: () => ({
    val: "",
    alert: false
  }),
  methods: {
    fetchURL: function (method='POST') {
      if(this.val === ""){
        this.alert = true
        return
      }
      let xmlHttpReq = new XMLHttpRequest();
      xmlHttpReq.open(method, 'http://warder.herokuapp.com/subscribe', false);
      let data = new FormData()
      data.append('email', this.val)
      xmlHttpReq.send(data);
    },
  }
}
</script>

<style scoped>
div#Subscribe{
  text-align: center;
  height: 25rem;
  display: grid;
  grid-template-columns: 50% 20% 30%;
}
span{
  display: inline-block;
  margin-top: 20%;
}
</style>
