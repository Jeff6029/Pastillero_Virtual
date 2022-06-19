<template>
  <h1>Mis Medicamentos:</h1>
  <h1>{{ getUserId }}</h1>
  <nav class="area-btns">
    <button class="btn-medicine-add" @click="onClickMedicinesAdd">
      <i class="fa-solid fa-plus"></i>
    </button>
    <button class="btn-medicine-schedule" @click="onClickMedicinesSchedule">
      <i class="fa-solid fa-calendar-days"></i>
    </button>
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
body {
  width: 100vw;
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
  margin: 1em;
  background: #e5e9e8e0;
  color: black;
  border-radius: 5px;
  border: 1px solid #42b983;
}

.btn-medicine-add:hover,
.btn-medicine-schedule:hover {
  background: #6dc39c;
  color: white;
  transition: 0.2s all ease-out;
}

.medicines-list {
  display: grid;
  place-items: center;
}

.medicines-list > .medicine-box:hover {
  outline: 0;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.11);
}
</style>
