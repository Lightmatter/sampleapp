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
        main: resolve(__dirname, './frontend/js/main.ts'),
      }
    },
    outDir:  '../sampleapp/static', // puts the manifest.json in PROJECT_ROOT/static/
  },
  plugins: [
    // {
    //   name: 'watch-external', // https://stackoverflow.com/questions/63373804/rollup-watch-include-directory/63548394#63548394
    //   async buildStart(){
    //     const files = await fg(['sampleapp/templates/**/*']);
    //     for(let file of files){
    //       this.addWatchFile(file);
    //     }
    //   }
    // },
    // {
    //   name: 'reloadHtml',
    //   handleHotUpdate({ file, server }) {
    //     if (file.endsWith('.html')) {
    //       server.ws.send({
    //         type: 'full-reload',
    //         path: '*',
    //       });
    //     }
    //   },
    // }
  ],
});
