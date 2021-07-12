<template>
  <div class="container-fluid" id="loginBody">
    <div class="sidebar shadow">
      <div class="d-flex justify-content-around org-name">
        <h2 class="mt-5">Система "{{ appConfig.appName }}"</h2>
      </div>
      <div class="form-layout">
        <router-view />
      </div>
      <div class="footer">
        <div class="d-flex justify-content-around text-muted">
          {{ appConfig.orgName }}
        </div>
        <div class="d-flex justify-content-around text-muted">
          Все права защищены {{ appConfig.copyRightsYear }} г.
        </div>
        <div class="d-flex justify-content-around text-muted">
          Разработчик: {{ appConfig.developerName }}
        </div>
        <div class="d-flex justify-content-around text-muted">
          email: {{ appConfig.orgEmail }}
        </div>
        <div class="d-flex justify-content-around text-muted">
          Адрес: {{ appConfig.orgAdress }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    appConfig() {
      return this.$store.getters.appConfig;
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

#loginBody {
  font-family: "Montserrat", sans-serif;
  color: black;
  background-image: url(../assets/img/tile_background.png);
}

.sidebar {
  height: 100%;
  width: 550px;
  background-color: #b5d0d0;
  position: fixed;
  z-index: 1;
  top: 0;
}
</style>
