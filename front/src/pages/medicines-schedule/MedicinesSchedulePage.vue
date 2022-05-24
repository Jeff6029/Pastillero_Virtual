<template>
  <h1>Aqui va el horario</h1>
  <table>
    <tr>
      <th>Horas</th>
      <th>Medicinas</th>
    </tr>
    <tr v-for="number in hours" :key="number">
      <td class="hour">{{ `${number - 1}` }}:00 hrs.</td>
      <td>{{ filterPerHour(number) }}</td>
      <!-- <td><MedicineList medicines="filterPerHour(number)" /></td> -->
    </tr>
  </table>
  {{ this.namesFiltered }}
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicinesSchedule",
  data() {
    return {
      listMedicines: [],
      hours: 24,
      namesFiltered: [],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {
    filteredMedicines() {
      const filterMedicine = this.listMedicines.filter((medicine) => medicine);
      return filterMedicine;
    },
  },
  methods: {
    showNames() {
      let names = this.namesFiltered;
      for (let name in names) {
        return name;
      }
    },
    filterPerHour(number) {
      const hours_dosage = this.filteredMedicines.filter((medicine) => {
        if (medicine.dosage.hour_dosage.split(":")[0] === `${number}`) {
          return medicine;
        }
      });
      const names_medicines = hours_dosage.map(
        (medicine) => medicine.name_medicine
      );
      this.namesFiltered = names_medicines;
      return names_medicines;
    },
    async loadData() {
      let date = new Date();
      let today = date.toISOString().split("T")[0];
      const response = await fetch(
        `${config.API_PATH}/medicines/by-date/${today}`
      );
      const allResponse = await response.json();
      this.listMedicines = allResponse;
    },
  },
};
</script>

<style scoped>
table {
  width: 80vw;
  margin: 0 10vw;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
}

th {
  text-align: left;
}
.hour {
  width: 10vw;
}
</style>