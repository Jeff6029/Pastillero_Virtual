<template>
  <header class="areTitle">
    <h1>Horario</h1>
    <button class="btn-back" @click="onClickToReturnListMedicines">
      <i class="fa-solid fa-arrow-rotate-left"></i>
    </button>
  </header>
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
</template>

<script>
import { getListMedicinesByDate } from "@/services/api.js";
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
    onClickToReturnListMedicines() {
      this.$router.push("/medicines");
    },
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
      const allResponse = await getListMedicinesByDate();
      this.listMedicines = allResponse;
    },
  },
};
</script>

<style scoped>
.areTitle {
  width: 350px;
  padding: 0 2.8em;
  margin: 0.8em auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.btn-back {
  cursor: pointer;
  padding: 8px;
  margin: 1em;
  background: #e5e9e8;
  color: black;
  border-radius: 5px;
  border: none;
}
.btn-back:hover {
  background: #6dc39c;
  color: white;
  transition: 0.2s all ease-out;
}

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