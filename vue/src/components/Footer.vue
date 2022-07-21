<template>
    <footer>
      <section class="links" :style="theme">
        <p></p>
        <ul>
          <h3>Company</h3>
          <li><a href="#">Blockchain Explorer</a></li>
          <li><a href="#">Crypto API</a> </li>
          <li><a href="#">Crypto Indices</a> </li>
          <li><a href="#">Jobs Board</a> </li>
          <li><a href="#">About us</a> </li>
          <li><a href="#">Terms of use</a> </li>
          <li><a href="#">Privacy Policy</a> </li>
          <li><a href="#">Community Rules</a> </li>
        </ul>
        <ul>
          <h3>Support</h3>
          <li><a href="#">Email</a> </li>
          <li><a href="#">Contact Support</a> </li>
          <li><a href="#">FAQ</a> </li>
          <li><a href="#">Disclaimer</a> </li>
          <li><a href="#">Methodology</a> </li>
        </ul>
        <ul>
          <h3>Socials</h3>
          <li><a href="#">Facebook</a> </li>
          <li><a href="#">Twitter</a> </li>
          <li><a href="#">Telegram</a> </li>
          <li><a href="#">Instagram</a> </li>
        </ul>
        <p></p>
      </section>
      <section>
        <p><Bitcoin/> 2022 Cryptonomy. All rights reserved</p>
      </section>
    </footer>
</template>

<script>
import Bitcoin from 'vue-material-design-icons/Bitcoin.vue';
export default {
  name: "Footer",
  props: {
    theme: String
  },
  components: {
    Bitcoin
  }
}
// video:
</script>

<style scoped>

a{
  color: green
}
section {
  padding: 0;
}
footer > section.links {
  display: grid;
  grid-template-columns: 47% 16% 16% 16% 5%;
  height: 22rem;
}
ul {
  list-style-type: none;
  font-size: 1.2rem;
}
ul > li {
  font-size: 1.0rem;
}
p {
  text-align: left;
  padding: 2rem;
  margin: 0
}
a:hover{
  color: cyan;
}
</style>
