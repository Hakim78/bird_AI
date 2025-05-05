<template>
    <div>
      <h3>Suggestions alternatives</h3>
      <ul>
        <li v-for="(item, index) in alternatives" :key="index">{{ item }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "FallbackSuggestions",
    props: {
      alternatives: Array
    }
  }
  </script>
  