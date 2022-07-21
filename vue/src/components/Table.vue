<template>
  <div class="center" >
    <span style="display: grid; grid-template-columns: 15% 45% 20% 10% 10%;  justify-content: center;
  align-items: center;margin:  -1.5rem 1.5rem 0.5rem 1.5rem">
            <strong>    Current market cap</strong>
            <span></span>
      <strong>Data from <a href="https://cryptoapis.io/">https://cryptoapis.io/</a></strong>
      <strong>Show rows</strong>
        <vs-select
        color="rgb(59,222,100)"
        placeholder="Select"
        v-model="max"
        :vs-theme="cls"
      >
      <vs-option label="5" value="5">
        5
      </vs-option>
      <vs-option label="10" value="10">
        10
      </vs-option>
      <vs-option label="20" value="20">
        20
      </vs-option>
      <vs-option label="30" value="30">
        30
      </vs-option>
    </vs-select>
    </span>
    <vs-table success :sort="true" :vs-theme="cls">
      <template  #thead>
        <vs-tr success style="color:green">
          <vs-th>Name</vs-th>
          <vs-th>usd</vs-th>
          <vs-th>usd_market_cap</vs-th>
          <vs-th>usd_24h_vol</vs-th>
          <vs-th>usd_24h_change</vs-th>
          <vs-th>eur</vs-th>
          <vs-th>eur_market_cap</vs-th>
          <vs-th>eur_24h_vol</vs-th>
          <vs-th>eur_24h_change</vs-th>
          <vs-th>last_updated_at</vs-th>
        </vs-tr>
      </template>
      <template #tbody>

        <vs-dialog blur not-close auto-width not-padding v-model="alert">
          <div class="con-image" style="padding: 1rem">
            <strong>{{ txt1 }}</strong><span style="color:green">{{ txt2 }} $</span>
          </div>
        </vs-dialog>

        <vs-tr @click="alert = true; txt1 = tr.name + '\n' ; txt2 = tr.usd_market_cap.toString()" v-for="(tr, i) in $vs.getPage(dat, page, max)" :key="i" :data="tr">
          <vs-td><h4>{{ tr.name }}</h4></vs-td>
          <vs-td>{{ tr.usd }}</vs-td>
          <vs-td>{{ tr.usd_market_cap }}</vs-td>
          <vs-td>{{ tr.usd_24h_vol }}</vs-td>
          <vs-td>{{ tr.usd_24h_change }}</vs-td>
          <vs-td>{{ tr.eur }}</vs-td>
          <vs-td>{{ tr.eur_market_cap }}</vs-td>
          <vs-td>{{ tr.eur_24h_vol }}</vs-td>
          <vs-td>{{ tr.eur_24h_change }}</vs-td>
          <vs-td>{{ tr.last_updated_at }}</vs-td>
        </vs-tr>

      </template>
      <template #footer>
          <vs-pagination width="80%" color="rgb(59,222,100)" v-model="page" :length="$vs.getLength(dat, max)" />
      </template>
    </vs-table>
  </div>
</template>


<script>
export default {
  name: "Table",
  props: {
    dat: Array,
    cls: String,
  },
  data: () => ({
  page: 1,
  max: 10,
    txt1: "",
    txt2: "",
    alert: false,
  })
}
</script>


<style scoped>

</style>
