<template>
  <h1>Aqui va el horario</h1>
  <table>
    <tr>
      <th>Horas</th>
      <th>Medicinas</th>
    </tr>
    <tr v-for="number in hours" :key="number">
      <td class="hour">{{ number - 1 }} hrs.</td>
      <!-- <td v-if="filterPerHour(number)"></td> -->
    </tr>
  </table>
  {{ this.filterPerHour(number) }}
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicinesSchedule",
  data() {
    return {
      listMedicines: [],
      hours: 24,
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
    filterPerHour(number) {
      let listOfMedicines = this.filteredMedicines();
      for (let medicine in listOfMedicines) {
        let hour = medicine.dosage.hour_dosage.split(":")[0];
        console.log(hour);
        if (number == hour) {
          return hour;
        }
      }
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