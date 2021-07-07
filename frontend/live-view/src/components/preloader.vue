<template>
  <div class="preloader d-flex">
    <div class="logo">
      <div class="kmkr-logo-circles">
        <img class="kmkr-logo-circle" src="@/assets/img/circle-1.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-2.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-3.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-4.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-5.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-6.svg" />
        <img class="kmkr-logo-circle" src="@/assets/img/circle-7.svg" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "preloader",
};
</script>

<style scoped>
.preloader {
  width: 100%;
  height: 100%;
  justify-content: center;
  padding-top: 150px;
}

.logo {
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-position: center;
  background-size: 200px, 1px;
  height: 363px;
  width: 344px;
}

.kmkr-logo-circles {
  width: 357px;
  height: 1px;
  margin: auto;
  position: relative;
  float: right;
}

.kmkr-logo-circle {
  position: absolute;
  animation: kmkr-logo-circle 1s linear infinite;
  will-change: transform;
}

.kmkr-logo-circle:nth-child(1) {
  animation-duration: 30s;
}

.kmkr-logo-circle:nth-child(2) {
  animation-duration: 40s;
}

.kmkr-logo-circle:nth-child(3) {
  animation-duration: 60s;
}

.kmkr-logo-circle:nth-child(4) {
  animation-duration: 70s;
}

.kmkr-logo-circle:nth-child(5) {
  animation-duration: 80s;
}

.kmkr-logo-circle:nth-child(6) {
  animation-duration: 90s;
}

.kmkr-logo-circle:nth-child(7) {
  animation-duration: 100s;
}

@keyframes kmkr-logo-circle {
  100% {
    transform: rotate(1turn);
  }
}
</style>
