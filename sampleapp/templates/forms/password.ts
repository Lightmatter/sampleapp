import AlpineInstance, { AlpineComponent } from "alpinejs";


interface Password {
  //callback requires indexing to string and symbol
  [key: string]: unknown;
  [key: symbol]: unknown;
  //real types
  eventName: string;
  value: unknown;
  type: unknown;
  active: boolean;
  updateFlag(): void;
}



const password = (...args: unknown[]): AlpineComponent<Password> => {
  const [eventName, value, type] = args as [string, unknown, unknown];
  return {
    eventName,
    value,
    type,
    active: false,
    updateFlag() {
      const childInput:HTMLInputElement|null = this.$refs.input.querySelector("input, textarea");
      if (!childInput) {
        return;
      }
      if (!childInput.value) {
        this.active = !this.active;
      }
    },
    init() {
      if (this.value === "None") {
        this.value = "";
      }
      if (this.eventName !== "") {
        this.$watch("value", () => {
          this.$dispatch(
            this.eventName,
            { value: this.value },
          );
        });
      }
    },
  }
};

AlpineInstance.data("password", password);
