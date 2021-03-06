<template>
  <div class="container">
    <ul class="list-group">
      <Card
          v-for="psychotherapist of psychotherapists" :key="psychotherapist.id"
          v-bind:psychotherapist="psychotherapist"
      />
      <hr>
    </ul>
  </div>
</template>

<script>
import Card from "@/components/Card"

export default {
  props: ['psychotherapists'],
  components: {
    Card
  }
}
</script>