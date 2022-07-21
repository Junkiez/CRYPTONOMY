<template>
  <div id="app" :style="theme.app">
    <span style="font-family: Monospace; letter-spacing: 0px;font-size: 12px; padding: 1em" v-html="jdat.status">
    </span>
    <header id="page" :style="theme.menu">
      <img/>
      <vs-button-group success>
        <vs-button
            success
            transparent
            :active="active == 1"
            @click="active = 1"
        >
          About
        </vs-button>
        <vs-select
            success
            :vs-theme="theme.table"
            :color="green"
            placeholder="Select"
            v-model="select"
        >
          <vs-option success v-for="(el,i) in jdat.table" :key="i" :data="el" :label="el.name" :value="el.name">
            {{  el.name }}
          </vs-option>
        </vs-select>
        <vs-button success transparent @click="runChart();sleep(150).then(() => { runChart() });">
          <i class='bx bx-home-alt' ></i> Chart
        </vs-button>
        <vs-button success transparent @click="scrollToBottom()">
          <i class='bx bxs-phone-call' ></i> Contact
        </vs-button>

        <vs-button success transparent>
          NFT
        </vs-button>
        <vs-button @click="arsen_posts_run()" success transparent>
        Posts
        </vs-button>
        <vs-button success transparent>
        CrypTown
        </vs-button>
        <vs-button success transparent>
        Portfolio
        </vs-button>
        <vs-button success transparent>
        Watchlist
        </vs-button>

      </vs-button-group>
      <span></span>


      <vs-select
          filter
          placeholder="Search"
          success
          :vs-theme="theme.table"
          v-model="search"
      >
        <vs-option  success v-for="(el,i) in jdat.table" :key="i" :data="el" :label="el.name" :value="el">
          {{  el.name }}
        </vs-option>
      </vs-select>


      <span></span>

      <vs-button
          @click="searched=true"
          color="rgb(59,222,100)"
          gradient
      >
        Show
      </vs-button>

      <vs-dialog blur not-close auto-width not-padding v-model="searched">
        <p class="con-image" style="padding: 1rem" v-html="frmt(search)">
        </p>
      </vs-dialog>



      <vs-button
          color="rgb(59,222,200)"
          gradient
          @click="loginActive = true"
      >
          {{ login_button }}
      </vs-button>

      <vs-switch dark v-model="th" style="width:60px;margin: 0.5rem">
        <template >
          <Sun v-if="!th" ></Sun>
          <Moon v-else style="background-color:transparent;color:white"></Moon>
        </template>
      </vs-switch>
    </header>

    <!-- style="width:500px; height:300px;"-->

    <section v-if="chartActive" style="
    width:100%;
    display: grid;
    grid-template-columns: 70% 5% 20% 5%;
    ">
      <div style="width:100%; height:auto">
        <canvas id="myChart"></canvas>
      </div>
      <span></span>
      <section style="padding-top: 3rem">
        <h2>Market cap</h2>
        <h3>Display chart for seven days cap</h3>
        <vs-button success block @click="dchart();select=''">
          Close
        </vs-button>
        <Bitcoin style="height: 3rem"/>
      </section>
      <span></span>
    </section>

<p>

</p>

    <vs-dialog scroll overflow-hidden not-close auto-width v-model="arsen_posts">
      <template #header>
        <h3>
          Arsen posts
        </h3>
      </template>
      <div class="con-content" v-if="arsen_posts">
        <vs-card :vs-theme="theme.table" v-for="(card,i) in jdat.arsen_posts_data" :key="i" @click="url(card.link)">
          <template #title>
            <h3 style="
            text-overflow: ellipsis;">{{ card.title }}</h3>
          </template>
          <template #img>
            <img :src="card.image_url" alt="" style="aspect-ratio: 16 / 9">
          </template>
          <template #text>
            <p style="
            text-overflow: ellipsis;">
              {{ card.description }}
            </p>
          </template>
        </vs-card>
      </div>
    </vs-dialog>



    <vs-dialog :vs-theme="theme.table" prevent-close v-model="loginActive">
      <template #header>
        <h4 class="not-margin">
          Welcome to <b>Cryptonomy</b>
        </h4>
      </template>

      <div class="con-form">
        <vs-input v-model="login_login" placeholder="Email">
          <template #icon>
            @
          </template>
        </vs-input>
        <vs-input type="password" v-model="login_password" placeholder="Password">
          <template #icon>
            <i class='bx bxs-lock'></i>
          </template>
        </vs-input>
      </div>

      <template #footer>
        <div class="footer-dialog">
          <vs-button @click="postON(login_login,login_password, 'get_user_data')" block>
            Sign In
          </vs-button>

          <div class="new">
            New Here? <a href="#" @click="logupActive = true">Create New Account</a>
          </div>
        </div>
      </template>
    </vs-dialog>

    <vs-dialog prevent-close v-model="logupActive">
      <template #header>
        <h4 class="not-margin">
          Welcome to <b>Cryptonomy</b>
        </h4>
      </template>


      <div class="con-form">
        <vs-input v-model="dl" placeholder="Email">
          <template #icon>
            @
          </template>
        </vs-input>
        <vs-input type="password" v-model="dl" placeholder="Password">
          <template #icon>
            <i class='bx bxs-lock'></i>
          </template>
        </vs-input>
      </div>

      <template #footer>
        <div class="footer-dialog">
          <vs-button block>
            Sign In
          </vs-button>

          <div class="new">
            New Here? <a href="#">Create New Account</a>
          </div>
        </div>
      </template>
    </vs-dialog>


    <!--<vs-card-group :v-if="dl">-->
    <div style="
      margin: 1rem;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 1rem;
      max-width: 100%;
      overflow-y: auto;
    " :v-if="dl">
      <vs-card :vs-theme="theme.table" v-for="(card,i) in jdat.news.filter(checkImage)" :key="i" @click="url(card.link)">
        <template #title>
          <h3 style="
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;">{{ card.title }}</h3>
        </template>
        <template #img>
          <img :src="card.image_url" alt="" style="aspect-ratio: 16 / 9">
        </template>
        <template #text>
          <p style="
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;">
            {{ card.description }}
          </p>
        </template>
      </vs-card>
    </div>


    <Table :dat="jdat.table" :cls="theme.table"></Table>
    <Subscribe :theme="theme.sub"></Subscribe>
    <Footer id="scr" :theme="theme.footer"></Footer>
  </div>
</template>

<script>
import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import Moon from 'vue-material-design-icons/WeatherNight.vue';
import Sun from 'vue-material-design-icons/WhiteBalanceSunny.vue'
import Table from "./components/Table";
import Subscribe from "./components/Subscribe";
import Footer from "./components/Footer";
import Bitcoin from 'vue-material-design-icons/Bitcoin.vue';

const Chart = require('chart.js/dist/chart.js');

Vue.use(Vuesax, {
  colors: {
    primary:'#5b3cc4',
    success:'rgb(23, 201, 100)',
    danger:'rgb(242, 19, 93)',
    warning:'rgb(255, 130, 0)',
    dark:'rgb(36, 33, 69)'
  }
})

export default {
  name: 'App',
  components: {
    Table,
    Subscribe,
    Footer,
    Moon,
    Sun,
    Bitcoin
  },
  created: function(){
    this.fetchURL("news", "GET", 'news')
    let stat = '    Cryptos:  <strong style="color:#3c3">18 255</strong>'
    this.fetchURL("current_cap/bitcoin", "GET", 'status', true)
    stat += `   bitcoin USD Marketcap: ` + '<strong style="color:#3c3">' + this.jdat.status + '</strong>'
    this.fetchURL("current_cap/ethereum", "GET", 'status', true)
    stat += "  ethereum USD Marketcap: " + '<strong style="color:#3c3">' + this.jdat.status + '</strong>'

    this.jdat.status = stat

    this.fetchURL("caps_chart/bitcoin", "GET", 'chart')

    this.fetchURL("table", "GET", 'table')
    this.dl = true
    this.openNotification('top-right', 'success')

    this.sleep(550).then(() => { this.th = true });
    this.sleep(650).then(() => { this.th = false });
  },
  methods: {
    scrollToBottom: function () {
      let pageBottom = document.querySelector("#scr")
      pageBottom.scrollIntoView()
    },
    url: function (link) {
      window.open(link)
    },
    frmt: function (obj) {
      let res = ``
      for(let i in obj){
        res += `
        ${i} : ${obj[i]}<br>
        `
      }
      return res
    },
    arsen_posts_run: function () {
      this.fetchURL('arsen_posts', 'GET', 'arsen_posts_data')
      this.arsen_posts = true
    },
    postON: function (login, password, url, code="") {
      let xmlHttpReq = new XMLHttpRequest();
      xmlHttpReq.open("POST", 'http://warder.herokuapp.com/' +url, false);
      let data = new FormData()
      data.append('email', login)
      data.append('pass', password)
      data.append('code', code)
      xmlHttpReq.send(data);
      let position ='top-right'
      let color = 'warn'
      alert(xmlHttpReq.responseText)
      try{
        this.user_data = JSON.parse(JSON.stringify(xmlHttpReq.responseText))
        this.login_button = this.user_data.name
      } catch(exception){
        this.$vs.notification({
          progress: 'auto',
          color,
          position,
          title: 'Message',
          text: xmlHttpReq.responseText
        })
      }
    },
    openNotification(position = null, color) {
      this.$vs.notification({
        progress: 'auto',
        color,
        position,
        title: 'Welcome to Cryptonomy',
        text: `These a tool to discover crypto marketcap,
            checkout all things it provides here 👉 Cryptonomy`
      })
    },
    dchart: function () {
      if(this.chart!=null){
        this.chart.destroy();
      }
      this.chartActive = false
    },
    runChart: function () {
      this.fetchURL("caps_chart/" + this.select, "GET", 'chart')
      this.chartActive = true
      if(this.chart!=null){
        this.chart.destroy();
      }
      this.chart = new Chart("myChart", {
        type: "line",
        data: {
          labels: this.jdat.chart.xValues,
          datasets: [{
            label: "marketcap",
            fill: false,
            lineTension: 1,
            backgroundColor: "#0f0a",
            borderColor: "rgba(0,255,255,0.3)",
            data: this.jdat.chart.yValues
          }]
        },
        options: {
          legend: {display: false},
          scales: {
            yAxes: [{ticks: {min: 1000 , max: 1000}}], //this.jdat.chart.Min
          }
        }
      });
    },
    sleep: function (ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    checkImage: function (card) {
      let url = card.image_url
      const img = new Image();
      img.src = url;

      if (img.complete) {
        return true
      } else {
        img.onload = () => {
          return true
        };
        img.onerror = () => {
          return false
        };
      }
    },
    // video:
    fetchURL: function (url, method='GET', val, str=false) {
      let xmlHttpReq = new XMLHttpRequest();
      xmlHttpReq.open(method, 'http://warder.herokuapp.com/'+url, false);
      xmlHttpReq.send(null);
      if(str){
        this.jdat[val] = xmlHttpReq.responseText;
        return true
      }
      this.jdat[val] = JSON.parse(xmlHttpReq.responseText);
      return true
    },
  },
  data: () => ({
    login_button: "Login",
    arsen_posts: false,
    select: "",
    search: "",
    txt1: "",
    txt2: "",
    searched: false,
    theme: {
      footer: "",
      app: "",
      sub: null,
      status: null,
      menu: null,
      table: null,
      card: null,
    },
    th: false,
    jdat: {
      status: null,
      news: null,
      table: null,
      chart: null,
      arsen_posts_data: null
    },
    loginActive: false,
    logupActive: false,
    chartActive: false,
    dl: false,
    login_password: "",
    login_login: "",
    logup_password: "",
    logup_login: "",
    sub_code: "",
    user_data: null,
    chart: null,
  }),
  watch: {
    th(val) {
      if (val) {
        this.theme.footer = `background-color: #282444; color: #ddd`
        this.theme.app = `background-color: #141222; color: #aaa`
        this.theme.sub = `background-color: #141222;`
        this.theme.status = `background-color: #141222; color: #dd0`
        this.theme.menu = `background-color: #282444`
        this.theme.table = `dark`
      } else {
        this.theme.footer = ``
        this.theme.app = ``
        this.theme.sub = ``
        this.theme.status = ``
        this.theme.menu = ``
        this.theme.table = ``
      }
    },
    searched(val) {
      if(!val){
        this.search = ''
      }
    }
  },
}
</script>

<style>
@font-face {
  font-family: "BebasNeue";
  src: url("assets/BebasNeueRegular.ttf");
  src: url("assets/BebasNeueRegular.otf");
}
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  scroll-behavior: smooth;
}
h2{
  margin-left : 2rem
}
#app {
  margin: 0;
  padding: 0;
  width: 100%;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: BebasNeue, monospace;
  font-size: 1rem;
  color: #444;
  letter-spacing: 0.1em;
}
::-webkit-scrollbar {
  width: 0;
}
header#page{
  margin: 0;
  padding: 0.5rem;
  background-color: #ded;
  display: grid;
  grid-template-columns: 5% 65% 1% 12% 1% 6% 5% 5%;
}
span#status {
  color: #777;
  display: block;
  width: 100%;
  text-align: left;
}
</style>
<style lang="stylus">
getColor(vsColor, alpha = 1)
unquote("rgba(var(--vs-"+vsColor+"), "+alpha+")")
getVar(var)
unquote("var(--vs-"+var+")")
.not-margin
  margin 0px
  font-weight normal
  padding 10px
.con-form
  width 100%
  .flex
    display flex
    align-items center
    justify-content space-between
    a
      font-size .8rem
      opacity .7
      &:hover
        opacity 1
  .vs-checkbox-label
    font-size .8rem
  .vs-input-content
    margin 10px 0px
    width calc(100%)
    .vs-input
      width 100%
.footer-dialog
  display flex
  align-items center
  justify-content center
  flex-direction column
  width calc(100%)
  .new
    margin 0px
    margin-top 20px
    padding: 0px
    font-size .7rem
    a
      color getColor('primary') !important
      margin-left 6px
      &:hover
        text-decoration underline
  .vs-button
    margin 0px
</style>
