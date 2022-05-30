<template>
  <h1>Aqui va el horario</h1>
  <table>
    <tr>
      <th>Horas</th>
      <th>Medicinas</th>
    </tr>
    <tr v-for="number in hours" :key="number">
      <td class="hour">{{ `${number - 1}` }}:00 hrs.</td>
      <td>{{ medicineFilterPerHour(number) }}</td>
      <!-- <td><MedicineList medicines="filterPerHour(number)" /></td> -->
    </tr>
  </table>
  {{ this.medicinesNamesFiltered }}
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicinesSchedule",
  data() {
    return {
      listMedicines: [],
      hours: 24,
      medicinesNamesFiltered: [],
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
    medicineFilterPerHour(number) {
      const listMedicinesPerHour = (medicine) => {
        let medicineDosageHour = medicine.dosage.hour_dosage.split(":")[0];
        if (medicineDosageHour === `${number}`) {
          return medicine;
        }
      };
      const hoursDosage = this.filteredMedicines.filter(listMedicinesPerHour);
      const namesMedicines = hoursDosage.map(
        (medicine) => medicine.name_medicine
      );
      this.medicinesNamesFiltered = namesMedicines;
      return namesMedicines;
    },
    async loadData() {
      let date = new Date();
      let today = date.toISOString().split("T")[0];
      let endpoint = `${config.API_PATH}/medicines/by-date/${today}`;

      const response = await fetch(endpoint);
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