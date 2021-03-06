<template>
  <li class="list-group-item">
    <div class="row">
      <div class="col-lg-3 img-wrap">
        <img class="card-img-top" :src="large_photo">
      </div>
      <div class="col-lg-9">
        <h2>{{ name }}</h2>
        <div class="methods m-3">
          <p class="text-left ml-lg-3">Методы:</p>
          <div class="row">
            <div class="col-lg-3 p-4 p-lg-2" v-for="method  in methods" :key="method">
            <span class="px-lg-2 py-lg-1 alert" :class="alerts[methods.indexOf(method) % 6]">
              {{ method }}
            </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  props: ['psychotherapist'],
  data() {
    return {
      large_photo: this.psychotherapist['fields']['Фотография'][0]['thumbnails']['large']['url'],
      name: this.psychotherapist['fields']['Имя'],
      methods: this.psychotherapist['fields']['Методы'],
      alerts: ['alert-primary', 'alert-success', 'alert-danger', 'alert-warning', 'alert-info', 'alert-dark', 'alert-secondary']
    }
  }
}
</script>

<style>
.card {
  flex-direction: row;
}

.img-wrap {
  height: 340px;
}

.img-wrap img {
  height: 100%;
  object-fit: cover;
}
</style>
