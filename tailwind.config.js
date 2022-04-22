module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-color-stops))'
      }
    }
  },
  variants: {
    extend: {
      display: ["group-hover"]
    }
  },
  plugins: [],
}
