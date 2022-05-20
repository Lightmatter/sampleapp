const plugin = require('tailwindcss/plugin');

module.exports = {
  content: [
    './frontend/**/*.html',
    './frontend/**/*.js',
    './frontend/**/*.css',
    './sampleapp/templates/**/*.html',
    './sampleapp/templates/**/*.jinja',
  ],
  theme: {
    extend: {
      colors: {
        primary: { 
          '50': '#ebecfa',
          '100':'#c3c6ef',
          '200':'#9aa0e4',
          '300':'#727ad9',
          '400':'#4a54cf',
          '500':'#303ab5',
          '600':'#262d8d',
          '700':'#1b2065',
          '800':'#10133c',
          '900':'#050614',
         },
        'secondary': '#D1D5DB',
        'accent': '#111827',
        base: {
          '100': '#FFFFFF',
        },
        gray: {
          '100': '#F3F6FA',
          '200': '#E5E7EB',
          '300': '#D1D5DB',
          '400': '#9CA3AF',
          '500': '#6B7280',
          '600': '#4B5563',
          '700': '#374151',
          '800': '#1F2937',
          '900': '#111827',
        },
        blue: {
          '50': '#eff6ff',
          400: '#60a5fa',
          800: '#1e40af',
        },
        green: {
          50: '#f0fdf4',
          400: '#4ade80',
          800: '#166534',
        },
        yellow: {
          50: '#fefce8',
          400: '#FACC15',
          800: '#854DOE',
        },
        red: {
          50: '#FEF2F2',
          400: '#F87171',
          800: '#991b1b',
        }
      }
    },
  },
  plugins: [
    plugin(function ({ addVariant }) {
      addVariant('htmx-settling', ['&.htmx-settling', '.htmx-settling &']);
      addVariant('htmx-request', ['&.htmx-request', '.htmx-request &']);
      addVariant('htmx-swapping', ['&.htmx-swapping', '.htmx-swapping &']);
      addVariant('htmx-added', ['&.htmx-added', '.htmx-added &']);
    }),
    require('@tailwindcss/forms'),
  ],
}
