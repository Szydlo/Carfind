/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.{html,js}"],
  theme: {
    colors: {
      'mainBG' : "#2C2C2C",
      'panelBG': "#1B1B1B",
      'white' : '#FFFFFF',
      'inputBG' : '#303030',
      'dark' : "#757575",
      'primary' : "#005D92",
      'primaryHover' : "#003D5F",
      'red' : "#3b0000",
      'redHover' : "#730101"
    },
    fontFamily : {
      'serif' : ["Inria Serif"],
      'display' : ["Inter"]
    },
    extend: {},
  },
  plugins: [],
}

