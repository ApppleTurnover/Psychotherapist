<template>
  <div id="app">
    <Cards v-bind:psychotherapists="psychotherapists"/>
    <Loader v-if="loading"/>
  </div>
</template>

<script>
import axios from 'axios';
import Cards from "@/components/Cards"
import Loader from "@/components/Loader"

export default {
  name: 'App',
  data() {
    return {
      psychotherapists: '',
      loading: true
    }
  },
  methods: {
    getData() {
      axios.get('http://localhost:5000/data')
          .then(res => {
            this.psychotherapists = res.data;
            this.loading = false
          })
          .catch(error => {
            console.error(error)
          });
    }
  },
  created() {
    this.getData()
  },
  components: {
    Cards, Loader
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
