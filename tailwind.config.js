/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#F5F3FF",
          100: "#EDE9FE",
          200: "#DDD6FE",
          300: "#C4B5FD",
          400: "#A78BFA",
          500: "#8B5CF6",
          600: "#5B35D5", // Exact primary accent from design brief
          700: "#4826B5",
          800: "#361B8C",
          900: "#24135C", // Deep primary indigo from design brief
          950: "#140A36",
          lavender: "#F2EEFF", // Background lavender
          electric: "#38BDF8",
        },
        navy: {
          950: "#090D1A",
          900: "#0D1424",
          850: "#111A30",
          800: "#18233C",
          700: "#243254",
        },
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      boxShadow: {
        'card-soft': '0 4px 20px -2px rgba(91, 53, 213, 0.08), 0 2px 6px -1px rgba(0, 0, 0, 0.04)',
        'card-hover': '0 12px 28px -4px rgba(91, 53, 213, 0.15), 0 4px 10px -2px rgba(0, 0, 0, 0.06)',
        'glow-purple': '0 0 25px -4px rgba(91, 53, 213, 0.35)',
      },
      keyframes: {
        wave: {
          '0%, 100%': { transform: 'scaleY(0.3)' },
          '50%': { transform: 'scaleY(1.0)' },
        },
      },
      animation: {
        'wave-bar': 'wave 1.2s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};
