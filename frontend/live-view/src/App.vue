<template>
  <div id="app">
    <header
      class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow"
    >
      <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#"
        >Кавминкурортресурсы</a
      >
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="#">Выход</a>
        </li>
      </ul>
    </header>
    <nav class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Live-режим</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>
