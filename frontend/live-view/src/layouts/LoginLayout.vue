<template>
  <div class="container-fluid" id="loginBody">
    <div class="sidebar shadow">
      <div class="d-flex justify-content-around org-name">
        <h2 class="mt-5">Система "Обелиск"</h2>
      </div>
      <div class="form-layout">
        <router-view />
      </div>
      <div class="footer">
        <div class="d-flex justify-content-around text-muted">
          АО "Кавминкурортресурсы"
        </div>
        <div class="d-flex justify-content-around text-muted">
          Все права защищены 2021 г.
        </div>
        <div class="d-flex justify-content-around text-muted">
          Разработчик: Туршиев Николай Манолисович
        </div>
        <div class="d-flex justify-content-around text-muted">
          email: it@kavminkr.ru
        </div>
        <div class="d-flex justify-content-around text-muted">
          Адрес: 357600 г. Ессентуки, Пятигорская 133.
        </div>
      </div>
    </div>
  </div>
</template>

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
