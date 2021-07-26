<template>
  <div>
    <form class="p-5" @submit.prevent="submitHandler">
      <label for="email" class="form-label">Логин:</label>
      <div v-if="$v.user.login.$invalid" class="invalid-feedback-text">
        Введите ваш Логин.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="login-addon"
          ><i class="bi bi-person-circle"></i
        ></span>
        <input
          v-model.trim="$v.user.login.$model"
          class="form-control"
          v-bind:class="[
            { valid: !$v.user.login.$invalid, invalid: $v.user.login.$invalid },
          ]"
          id="login"
          aria-describedby="login-addon"
        />
      </div>
      <label for="surname" class="form-label">Фамилия:</label>
      <div v-if="$v.user.surname.$invalid" class="invalid-feedback-text">
        Введите ваш Фамилию.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="surname-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.user.surname.$model"
          class="form-control"
          v-bind:class="[
            {
              valid: !$v.user.surname.$invalid,
              invalid: $v.user.surname.$invalid,
            },
          ]"
          id="surname"
          aria-describedby="surname-addon"
        />
      </div>
      <label for="name" class="form-label">Имя:</label>
      <div v-if="$v.user.name.$invalid" class="invalid-feedback-text">
        Введите ваш Имя.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="name-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.user.name.$model"
          class="form-control"
          v-bind:class="[
            { valid: !$v.user.name.$invalid, invalid: $v.user.name.$invalid },
          ]"
          id="name"
          aria-describedby="name-addon"
        />
      </div>
      <label for="patronymic" class="form-label">Отчество:</label>
      <div v-if="$v.user.patronymic.$invalid" class="invalid-feedback-text">
        Введите ваше Отчество.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="patronymic-addon"
          ><i class="bi bi-person-fill"></i
        ></span>
        <input
          v-model.trim="$v.user.patronymic.$model"
          class="form-control"
          id="patronymic"
          v-bind:class="[
            {
              valid: !$v.user.patronymic.$invalid,
              invalid: $v.user.patronymic.$invalid,
            },
          ]"
          aria-describedby="patronymic-addon"
        />
      </div>
      <label for="password" class="form-label">Пароль:</label>
      <div v-if="!$v.user.password.required" class="invalid-feedback-text">
        Введите ваш Пароль.
      </div>
      <div v-if="!$v.user.password.minLength" class="invalid-feedback-text">
        Пароль должен быть длинной не менее
        {{ $v.user.password.$params.minLength.min }} символов.
      </div>
      <div class="input-group mb-1">
        <span class="input-group-text" id="password-addon"
          ><i class="bi bi-shield-lock-fill"></i
        ></span>
        <input
          v-model.lazy.trim="$v.user.password.$model"
          type="password"
          class="form-control"
          id="password"
          v-bind:class="[
            {
              valid: !$v.user.password.$invalid,
              invalid: $v.user.password.$invalid,
            },
          ]"
          aria-describedby="password-addon"
        />
      </div>
      <label for="password_check" class="form-label">Повторите пароль:</label>
      <div v-if="$v.user.password_check.$invalid" class="invalid-feedback-text">
        Пароли не совападают.
      </div>
      <div class="input-group mb-3">
        <span class="input-group-text" id="password_check-addon"
          ><i class="bi bi-shield-lock-fill"></i
        ></span>
        <input
          v-model.trim="$v.user.password_check.$model"
          type="password"
          class="form-control"
          id="password_check"
          v-bind:class="[
            {
              valid:
                !$v.user.password_check.$invalid &&
                $v.user.password_check.sameAsPassword,
              invalid:
                $v.user.password_check.$invalid &&
                !$v.user.password_check.sameAsPassword,
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
import { required, minLength, sameAs } from "vuelidate/lib/validators";

export default {
  name: "Register",
  data: function () {
    return {
      user: {
        login: "",
        name: "",
        surname: "",
        patronymic: "",
        password: "",
        password_check: "",
      },
    };
  },
  validations: {
    user: {
      login: { required },
      name: { required },
      surname: { required },
      patronymic: { required },
      password: { required, minLength: minLength(8) },
      password_check: { sameAsPassword: sameAs("password") },
    },
  },
  methods: {
    async submitHandler() {
      if (this.$v.$invalid) {
        this.$v.$touch();
        return;
      }

      console.log(JSON.stringify(this.user));

      let response = await fetch(
        `http://${this.$store.getters.appApiAdress}/register`,
        {
          method: "POST",
          body: JSON.stringify(this.user),
        }
      );

      let result = await response.json();
      if (result.status_code === 201) {
        this.$router.push("/");
      }
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
