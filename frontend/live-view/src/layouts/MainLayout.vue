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
    <router-view />
  </div>
</template>
