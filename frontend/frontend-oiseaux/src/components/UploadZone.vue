<template>
    <div
      class="upload-zone"
      @dragover.prevent
      @drop.prevent="handleDrop"
      @click="$refs.fileInput.click()"
    >
      <p v-if="!fileName">Cliquez ou déposez un fichier .ogg ici</p>
      <p v-else>Fichier sélectionné : {{ fileName }}</p>
      <input
        type="file"
        accept=".ogg"
        ref="fileInput"
        class="hidden"
        @change="handleFileChange"
      />
    </div>
  </template>
  
  <script>
  export default {
    name: "UploadZone",
    data() {
      return {
        fileName: ""
      };
    },
    methods: {
      handleFileChange(event) {
        const file = event.target.files[0];
        this.processFile(file);
      },
      handleDrop(event) {
        const file = event.dataTransfer.files[0];
        this.processFile(file);
      },
      processFile(file) {
        if (file && file.name.endsWith(".ogg")) {
          this.fileName = file.name;
          this.$emit("file-selected", file);
        } else {
          alert("Veuillez sélectionner un fichier au format .ogg");
        }
      }
    }
  };
  </script>
  