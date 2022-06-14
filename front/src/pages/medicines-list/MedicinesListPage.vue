<template>
  <h1>Mis Medicamentos: {{ getUserId }}</h1>
  <nav class="area-btns">
    <button @click="onClickMedicinesAdd">Añadir +</button>
    <button @click="onClickMedicinesSchedule">Horario</button>
  </nav>
  <section class="medicines-list">
    <Medicine
      v-for="medicine in filteredMedicines"
      :key="medicine.id"
      :medicine="medicine"
      class="medicine-box"
    />
  </section>
</template>

<script>
import { getMedicines } from "@/services/api.js";
import Medicine from "./Medicine.vue";
export default {
  name: "MedicinesList",
  components: {
    Medicine,
  },
  data() {
    return {
      allMedicines: [],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {
    filteredMedicines() {
      const filterMedicine = this.allMedicines.filter((medicine) => medicine);
      return filterMedicine;
    },
    getUserId() {
      const userJson = localStorage.getItem("auth");
      const user = JSON.parse(userJson);
      return user.name;
    },
  },
  methods: {
    onClickMedicinesAdd() {
      this.$router.push("/medicinesadd");
    },
    onClickMedicinesSchedule() {
      let date = new Date();
      let today = date.toISOString().split("T")[0];
      this.$router.push(`/medicines-schedule/${today}`);
    },
    async loadData() {
      const response = await getMedicines();
      this.allMedicines = response;
    },
  },
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
body {
  width: 100vw;
}
.medicines-list {
  display: grid;
  place-items: center;
}
.area-btns {
  width: 350px;
  padding: 0 2.8em;
  margin: 0.8em auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.area-btns > button {
  padding: 0.5em;
  cursor: pointer;
}
</style>
