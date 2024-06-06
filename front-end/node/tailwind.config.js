/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    // "../pages/**/*.py",
    "../*.py",
    "../views/*.py",
    "../**/*.py"
  ],
  theme: {
    extend: {
      flexGrow: {
        1: 1,
      }
    },
  },
  plugins: [],
};

