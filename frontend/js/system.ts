import "htmx.org";
// @ts-expect-error // todo: make a types file for x-widget
import Alpine from "alpinejs";

declare global {
  interface Window {
    Alpine?: any;
  }
}

// @ts-expect-error // todo: make a types file for x-widget
// const { htmx } = window;
window.Alpine = Alpine;
Alpine.start();

// if (import.meta.hot) {
//   import.meta.hot.on("special-update", (data) => {});
// }
