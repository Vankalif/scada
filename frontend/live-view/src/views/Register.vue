<template>
  <div>
    <form class="p-5" @submit.prevent="submitHandler">
      <label for="email" class="form-label">Адрес электронной почты:</label>
      <div v-if="$v.email.$invalid" class="invalid-feedback-text">
        Введите ваш Email.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="email-addon"
          ><i class="bi bi-envelope-fill"></i
        ></span>
        <input
          v-model.trim="$v.email.$model"
          class="form-control"
          v-bind:class="[
            { valid: !$v.email.$invalid, invalid: $v.email.$invalid },
          ]"
          id="email"
          aria-describedby="email-addon"
        />
      </div>
      <label for="surename" class="form-label">Фамилия:</label>
      <div v-if="$v.surename.$invalid" class="invalid-feedback-text">
        Введите ваш Фамилию.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="surename-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.surename.$model"
          class="form-control"
          v-bind:class="[
            { valid: !$v.surename.$invalid, invalid: $v.surename.$invalid },
          ]"
          id="surename"
          aria-describedby="surename-addon"
        />
      </div>
      <label for="name" class="form-label">Имя:</label>
      <div v-if="$v.name.$invalid" class="invalid-feedback-text">
        Введите ваш Имя.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="name-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.name.$model"
          class="form-control"
          v-bind:class="[
            { valid: !$v.name.$invalid, invalid: $v.name.$invalid },
          ]"
          id="name"
          aria-describedby="name-addon"
        />
      </div>
      <label for="patronymic" class="form-label">Отчество:</label>
      <div v-if="$v.patronymic.$invalid" class="invalid-feedback-text">
        Введите ваше Отчество.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="patronymic-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.patronymic.$model"
          class="form-control"
          id="patronymic"
          v-bind:class="[
            { valid: !$v.patronymic.$invalid, invalid: $v.patronymic.$invalid },
          ]"
          aria-describedby="patronymic-addon"
        />
      </div>
      <label for="password" class="form-label">Пароль:</label>
      <div v-if="!$v.password.required" class="invalid-feedback-text">
        Введите ваш Пароль.
      </div>
      <div v-if="!$v.password.minLength" class="invalid-feedback-text">
        Пароль должен быть длинной не менее
        {{ $v.password.$params.minLength.min }} символов.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="password-addon"
          ><i class="bi bi-shield-lock-fill"></i
        ></span>
        <input
          v-model.lazy.trim="$v.password.$model"
          type="password"
          class="form-control"
          id="password"
          v-bind:class="[
            { valid: !$v.password.$invalid, invalid: $v.password.$invalid },
          ]"
          aria-describedby="password-addon"
        />
      </div>
      <label for="password_check" class="form-label">Повторите пароль:</label>
      <div v-if="$v.password_check.$invalid" class="invalid-feedback-text">
        Пароли не совападают.
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="password_check-addon"
          ><i class="bi bi-shield-lock-fill"></i
        ></span>
        <input
          v-model.trim="$v.password_check.$model"
          type="password"
          class="form-control"
          id="password_check"
          v-bind:class="[
            {
              valid:
                !$v.password_check.$invalid && $v.password_check.sameAsPassword,
              invalid:
                $v.password_check.$invalid && !$v.password_check.sameAsPassword,
            },
          ]"
          aria-describedby="password_check-addon"
        />
      </div>
      <div class="d-flex justify-content-around pt-2">
        <button type="submit" class="btn bg-reg-btn login-btn-group">
          Отправить
        </button>
        <p>Уже есть аккаунт? <router-link to="/">Войти</router-link></p>
      </div>
    </form>
  </div>
</template>

<script>
import { email, required, minLength, sameAs } from "vuelidate/lib/validators";

export default {
  name: "Register",
  data: function () {
    return {
      email: "",
      name: "",
      surename: "",
      patronymic: "",
      password: "",
      password_check: "",
    };
  },
  validations: {
    email: { email, required },
    name: { required },
    surename: { required },
    patronymic: { required },
    password: { required, minLength: minLength(8) },
    password_check: { sameAsPassword: sameAs("password") },
  },
  methods: {
    submitHandler() {
      if (this.$v.$invalid) {
        this.$v.$touch();
        return;
      }
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
.invalid-feedback-text {
  width: 100%;
  font-size: 0.875em;
  color: #dc3545;
}

.valid {
  border-color: rgba(0, 90, 0, 0.5);
  border-width: 5px;
  opacity: 0.5;
}

.invalid {
  border-color: rgba(255, 0, 0, 0.5);
  border-width: 5px;
  opacity: 0.5;
}

.bg-reg-btn {
  background-color: #3b8787;
}

.login-btn-group {
  color: azure;
}

.form-label {
  margin-bottom: 0rem;
}
p {
  margin-top: 0px;
  margin-bottom: 0rem;
}
</style>
