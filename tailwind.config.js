/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,js,css}"],
  theme: {

    colors:{
      'nemo': '#7D8AF6',
      'nemo-main': '#808DF6',
      'for-buttons': '#FF5A05',
      'register-bg': '#7B68EE'
    },

    extend: {
      backgroundImage:{
        'mainpage-gradient': 'radial-gradient(circle, rgba(155,180,255,1) 29%, rgba(84,129,255,1) 96%)',
        'register-gradient': 'radial-gradient(circle, rgba(46, 67, 240, 0.61) 61%, rgba(63, 83, 244, 0.73) 73%, rgba(102, 119, 255, 1.0) 100%)'
      }
    },
  },
  plugins: [],
}
