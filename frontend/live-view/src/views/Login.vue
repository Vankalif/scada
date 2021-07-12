<template>
  <div>
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
      <div class="d-flex justify-content-between pt-2">
        <router-link
          to="/live"
          class="btn bg-login-btn login-btn-group"
          tabindex="-1"
          role="button"
          >Войти</router-link
        >
        <router-link
          to="/register"
          class="btn bg-reg-btn login-btn-group"
          tabindex="-1"
          role="button"
          >Зарегистрироваться</router-link
        >
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
};
</script>

<style scoped>
.bg-reg-btn {
  background-color: #3b8787;
}
.bg-login-btn {
  background-color: #3e568d;
}
.login-btn-group {
  color: azure;
}
</style>
