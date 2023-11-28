/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx,tsx}"],
  theme: {
    extend: {
      backgroundColor: {
        primary: "#435334",
        secondary: "#9EB384",
        backgroundGray: "DBDBDB",
      },
      textColor: {
        primary: "#435334",
        secondary: "#9EB384",
        black: "#111111",
      },
    },
  },
  plugins: [],
};
