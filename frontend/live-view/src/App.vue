<template>
  <div id="app">
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import MainLayout from "@/layouts/MainLayout";
import LoginLayout from "@/layouts/LoginLayout";

export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || "login") + "-layout";
    },
  },
  components: {
    MainLayout,
    LoginLayout,
  },
};
</script>
