<template>
  <div class="top-predictions" v-if="predictions.length">
    <h2>Top 3 des Prédictions</h2>
    <ul>
      <li v-for="(item, index) in predictions" :key="index">
        {{ index + 1 }}. {{ item.label }} — {{ (item.confidence * 100).toFixed(1) }}%
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    predictions: {
      type: Array,
      required: true,
      default: () => []
    }
  }
};
</script>
