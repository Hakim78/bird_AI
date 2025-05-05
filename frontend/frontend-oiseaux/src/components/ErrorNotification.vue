<template>
    <div class="error-notification" v-if="message">
      <div class="error-box">
        <svg class="icon" viewBox="0 0 24 24">
          <path
            fill="currentColor"
            d="M11.001 10h2v5h-2zm0 6h2v2h-2z"
          />
          <path
            fill="currentColor"
            d="M1 21h22L12 2 1 21zm12-3v-2h-2v2h2zm0-3V10h-2v5h2z"
          />
        </svg>
        <p>{{ message }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: {
        type: String,
        default: ''
      }
    }
  };
  </script>
  