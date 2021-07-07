<template>
  <div>
    <header class="navbar sticky-top flex-md-nowrap p-0 shadow">
      <div class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">
        Кавминкурортресурсы
      </div>
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="#">Выход</a>
        </li>
      </ul>
    </header>
    <nav class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse shadow">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="nav-item">
            <router-link class="nav-link" to="/live">Live-режим</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/charts">Графики</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/meteo">Метеоданные</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/reports">Отчёты</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/tambukan">Тамбукан</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div class="app-body">
      <router-view />
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@300&display=swap");

.app-body {
  color: #dad6d1;
  background: #939fae;
  font-family: "Source Code Pro", monospace;
  height: 100%;
  width: 100%;
  position: fixed;
  z-index: 1;
  top: 0;
}

header {
  background-color: #49525c;
}

.navbar-brand {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  font-size: 1rem;
  background-color: rgba(0, 0, 0, 0.25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.25);
  color: aqua;
}

.navbar-nav .nav-link {
  color: #c6c1ae;
}

.navbar .form-control {
  padding: 0.75rem 1rem;
  border-width: 0;
  border-radius: 0;
}

.form-control-dark {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.1);
}

.form-control-dark:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.25);
}

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  padding: 48px 0 0;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.1);
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: 0.5rem;
  overflow-x: hidden;
  overflow-y: auto;
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #727272;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: 0.75rem;
  text-transform: uppercase;
}
</style>
