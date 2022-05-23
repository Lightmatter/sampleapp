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
          '100': '#c3c6ef',
          '200': '#9aa0e4',
          '300': '#727ad9',
          '400': '#4a54cf',
          '500': '#303ab5',
          '600': '#262d8d',
          '700': '#1b2065',
          '800': '#10133c',
          '900': '#050614',
        },
        secondary: {
          '50': '#f1f2f4',
          '100': '#d4d8dd',
          '200': '#b7bec7',
          '300': '#9ba4b1',
          '400': '#7e899a',
          '500': '#657081',
          '600': '#4e5764',
          '700': '#383e48',
          '800': '#22252b',
          '900': '#0b0c0e',
        },
        accent: {
          '50': '#edf0f7',
          '100': '#cad3e8',
          '200': '#a6b6d8',
          '300': '#8399c9',
          '400': '#5f7cb9',
          '500': '#4662a0',
          '600': '#364d7c',
          '700': '#273759',
          '800': '#172135',
          '900': '#080b12',
        },
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
