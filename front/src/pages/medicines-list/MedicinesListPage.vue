<template>
  <h1>Mis Medicamentos ( {{ this.filteredMedicines.length }} )</h1>
  <nav class="area-btns">
    <button>Añadir Medicamento</button>
    <button>Calendario</button>
  </nav>
  <section class="medicines-list">
    <article
      class="medicine-box"
      v-for="medicine of this.filteredMedicines"
      :key="medicine.id"
    >
      <header>
        <h3>{{ medicine.name_medicine }}</h3>
        <router-link
          :to="{
            name: 'MedicineDetailPage',
            params: { id: `${medicine.id_medicine}` },
          }"
        >
          <button>+ info {{ medicine.id }}</button>
        </router-link>
      </header>
      <ul>
        <li>id: {{ medicine.id_medicine }} @click="openInfoMedicinePage(medicine)" </li>
        <li>Tipo: {{ medicine.type_medicine }}</li>
        <li>Dosis: {{ medicine.dosage }}</li>
        <li>Fecha Fin: {{ medicine.end_date }}</li>
      </ul>
    </article>
  </section>
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicinesList",
  data() {
    return {
      all_medicines: [],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {
    filteredMedicines() {
      const filterMedicine = this.all_medicines.filter((medicine) => medicine);
      return filterMedicine;
    },
  },
  methods: {
    async loadData() {
      const response = await fetch(`${config.API_PATH}/medicines`);
      this.all_medicines = await response.json();
    },
    // openInfoMedicinePage(medicine) {
    //   this.$router.push("/medicines/" + medicine.id_medicine);
    // },
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
.area-btns {
  padding: 0 3em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}
.medicine-box {
  border: 2px solid #42b983;
}
.medicine-box > header {
  padding: 0 2em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}

.medicine-box > ul > li {
  list-style: none;
  text-align: left;
  margin: 0 3em;
  margin-bottom: 0.4em;
}
</style>
