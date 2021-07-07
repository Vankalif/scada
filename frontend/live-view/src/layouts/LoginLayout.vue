<template>
  <div class="container-fluid" id="loginBody">
    <div class="sidebar shadow">
      <div class="d-flex justify-content-around org-name">
        <h2 class="mt-5">Система "Обелиск"</h2>
      </div>
      <div class="form-layout">
        <form class="p-5">
          <label for="email" class="form-label">Пользователь:</label>
          <div class="input-group mb-3">
            <span class="input-group-text" id="email-addon"
              ><i class="bi bi-person-bounding-box"></i
            ></span>
            <input
              class="form-control"
              required
              id="email"
              aria-describedby="email-addon"
            />
          </div>
          <label for="password" class="form-label">Пароль:</label>
          <div class="input-group mb-3">
            <span class="input-group-text" id="password-addon"
              ><i class="bi bi-shield-lock-fill"></i
            ></span>
            <input
              type="password"
              class="form-control"
              required
              id="password"
              aria-describedby="password-addon"
            />
          </div>
          <router-link
            to="/live"
            class="btn btn-primary"
            tabindex="-1"
            role="button"
            >Войти</router-link
          >
        </form>
      </div>
      <div class="footer">
        <div class="d-flex justify-content-around">
          <h6><p class="text-muted">АО "Кавминкурортресурсы"</p></h6>
        </div>
        <div class="d-flex justify-content-around">
          <h6 class="text-muted">Все права защищены 2021 г.</h6>
        </div>
        <div class="d-flex justify-content-around">
          <h6 class="text-muted">Разработчик: Туршиев Николай Манолисович</h6>
        </div>
        <div class="d-flex justify-content-around">
          <h6 class="text-muted">email: it@kavminkr.ru</h6>
        </div>
        <div class="d-flex justify-content-around">
          <h6 class="text-muted">
            Адрес: 357600 г. Ессентуки, Пятигорская 133.
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

#loginBody {
  font-family: "Montserrat", sans-serif;
  color: black;
  background-image: url(../assets/img/tile_background.png);
}

.org-name {
  margin-top: 15%;
}

.sidebar {
  height: 100%;
  width: 550px;
  background-color: #bec8d7;
  position: fixed;
  z-index: 1;
  top: 0;
}

.sidebar > .footer {
  margin-top: 40%;
}
</style>
