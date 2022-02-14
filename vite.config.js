const { resolve } = require('path');
const fg = require('fast-glob');
import { defineConfig } from 'vite';



export default defineConfig({
  base: "/static/",
  root: resolve('./frontend/'),
  resolve:{
    alias:{
      '@' : resolve('./frontend')
    },
  },
  build: {
    manifest: true, // adds a manifest.json
    rollupOptions: {
      input: {
        fontawesome: resolve(__dirname, './frontend/fontawesome/fontawesome.ts'),
        main: resolve(__dirname, './frontend/js/main.ts'),
        system: resolve(__dirname, './frontend/js/system.ts'),
      }
    },
    outDir:  '../sampleapp/static', // puts the manifest.json in PROJECT_ROOT/static_source/
  },
});
