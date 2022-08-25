/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "../templates/**/*.html",
    "../project/**/*.html",
    "../account/**/*.html",
  ],
  theme: {
    screens: {
      xs: "475px",
      sm: "576px",
      md: "768px",
      lg: "976px",
      xl: "1440px",
    },
    extend: {
      colors: {
        aptechRed: "#AD1E22",
        aptechOrange: "#ddac26",
        darkBlue: "#2F2E41",
      },
    },
    fontFamily: {
      jost: ["Jost", "sans-serif"],
      mulish: ["Mulish", "sans-serif"],
    },
    fontSize: {
      xs: ".75rem",
      sm: ".875rem",
      tiny: ".875rem",
      base: "1rem",
      md: "15px",
      lg: "1.125rem",
      xl: "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem",
      "4xl": "2.25rem",
      "5xl": "3rem",
      "6xl": "4rem",
      "7xl": "5rem",
    },
  },
  plugins: [require("daisyui")],
};
