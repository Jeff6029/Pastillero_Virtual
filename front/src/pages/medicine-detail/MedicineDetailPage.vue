<template>
  <section class="medicines-list">
    <article class="medicine-box" >
      <header>
        <h2>{{ medicine.name_medicine }}</h2>
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
  name: "MedicineDetail",
  data() {
    return {
		medicine : {},
		idOfMedicine: this.$route.params.id,
	}
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch(`${config.API_PATH}/medicines/${this.idOfMedicine}`);
      this.medicine = await response.json();
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
.medicines-list{
	margin: 10vh auto ;
	width: 60vw;
	height: 50vh;
	border: 1px solid #42b983;
	border-radius: 12px;
	display: grid;
	place-items: center;
	overflow: auto;
}

.medicine-box > ul > li {
  list-style: none;
  text-align: center;
  margin: 0 3em;
  margin-bottom: 0.4em;
}

</style>
