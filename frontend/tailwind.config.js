/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        overlord: {
          primary: '#6D28D9',
          secondary: '#DB2777',
        }
      }
    },
  },
  plugins: [],
}