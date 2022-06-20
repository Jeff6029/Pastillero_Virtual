<template>
  <header class="areTitle">
    <h1>Horario:</h1>
    <button class="btn-back" @click="onClickToReturnListMedicines">
      <i class="fa-solid fa-arrow-rotate-left"></i>
    </button>
  </header>
  <sectionn class="content-table">
    <table>
      <tr>
        <th>Horas</th>
        <th>Medicinas</th>
      </tr>
      <tr
        v-for="medicine in filteredMedicines"
        :key="medicine.id"
        class="data-medicine"
      >
        <td>
          {{ medicine.dosage.hour_dosage }}
          hrs.
        </td>
        <td>
          <span @click="onClickGetMedicineById(medicine.id_medicine)">{{
            medicine.name_medicine
          }}</span>
        </td>
      </tr>
    </table>
  </sectionn>
</template>

<script>
import { getListMedicinesByDate } from "@/services/api.js";
export default {
  name: "MedicinesSchedule",
  data() {
    return {
      listMedicines: [],
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
    async loadData() {
      const allResponse = await getListMedicinesByDate();
      this.listMedicines = allResponse;
    },
    onClickGetMedicineById(id_medicine) {
      this.$router.push(`/medicines/${id_medicine}`);
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

.content-table {
  margin: 0 auto;
  max-width: 1200px;
  display: grid;
  place-content: center;
}

.content-table > table {
  width: 300px;
  font-size: 12px;
  border-collapse: collapse;
}

table,
th,
td {
  border-bottom: 1px solid black;
}

th,
td {
  padding: 10px;
}

.data-medicine:hover {
  background: #78d4cb;
  color: white;
}
span {
  cursor: pointer;
}

th {
  text-align: center;
}
.hour {
  width: 10vw;
}

@media screen and (min-width: 700px) {
  .content-table > table {
    width: 450px;
    font-size: 14px;
  }
}
@media screen and (min-width: 1050px) {
  .content-table > table {
    width: 700px;
    font-size: 15px;
  }
}
@media screen and (min-width: 1320px) {
  .content-table > table {
    width: 800px;
    font-size: 16px;
  }
}
@media screen and (min-width: 1700px) {
  .content-table > table {
    width: 1100px;
    font-size: 18px;
  }
}
</style>