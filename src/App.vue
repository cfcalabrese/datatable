<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Mukta:wght@200&display=swap');
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'mukta', sans-serif;
}
.container {
  max-width: 1800px;
  margin: 30px auto;
  overflow-y: scroll;
  min-height: 500px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
  align-content: center;
}
</style>
