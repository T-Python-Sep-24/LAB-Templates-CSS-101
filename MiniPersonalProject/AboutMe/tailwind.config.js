/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Scans all HTML files in the templates folder
    './src/**/*.js',        // If you have JavaScript files in the src folder
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
