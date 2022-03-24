<template>
  <h1>Mis Medicamentos ( {{ this.filteredMedicines.length }} )</h1>
  <nav class="area-btns">
    <button>Añadir +</button>
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
  },
  methods: {
    async loadData() {
      const response = await fetch(`${config.API_PATH}/medicines`);
      this.allMedicines = await response.json();
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
}
.medicine-box {
  width: 300px;
  border: 2px solid #42b983;
  margin: 3px 0;
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
