<template>
  <body class='bg-slate-900 h-screen pt-5 overflow-auto w-full'>
    <div class="grid grid-cols-3">
      <div class="ml-2 p-5 col-span-2">
        <img 
          src="@/assets/esure_No_R_Blue.png"
          alt="esure-logo"
          width="100"
          height="auto"
          class=""
        >
      </div>
      <div class="col-span-1 bg-radial-gradient from-slate-700 via-slate-900 to-slate-900 rounded-full mr-6 flex justify-center items-center">
        <nav class="text-white font-bold">
          <router-link to="/">Home</router-link> |
          <router-link to="/about">About</router-link>
        </nav>
      </div>
    </div>
    <router-view />
  </body>
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
</style>
