/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,vue}'],
  theme: {
    colors: {
      green: {
        100: '#C4FF61',
        200: '#B3CB80',
      },
      background: '#232323',
      foreground: {
        DEFAULT: '#494949',
        'white': '#fff',
        200: '#BFBFBF',
        300: '#DEDEDE'
      }

    },
    extend: {},
  },
  plugins: [],
}
