<template>
  <h1>Aqui va el horario</h1>
  <table>
    <tr>
      <th>Horas</th>
      <th>Medicinas</th>
    </tr>
    <tr v-for="number in hours" :key="number">
      <td class="hour">{{ number - 1 }}</td>
      <td>medicina</td>
    </tr>
  </table>
  {{ this.listMedicines }}
</template>

<script>
import config from "@/config.js";
export default {
  data() {
    return {
      listMedicines: [],
      hours: 24,
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch(
        `${config.API_PATH}/medicines/by-date/2022-05-11`
      );
      const allResponse = await response.json();
      this.listMedicines = allResponse;
      console.log(allResponse);
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