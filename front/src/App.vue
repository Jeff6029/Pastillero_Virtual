<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/medicines">Mis Medicinas</router-link>
  </div>
  <router-view />
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Raleway:wght@400;500&display=swap");
* {
  font-family: "Playfair Display", serif;
}
</style>