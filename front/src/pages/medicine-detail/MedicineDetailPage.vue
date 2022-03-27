<template>
  <fieldset class="medicines-box">
    <legend>+ Información:</legend>
    <h2 class="medicine-name">{{ medicine.name_medicine }}</h2>
    <ul>
      <li>Tipo: {{ medicine.type_medicine }}</li>
      <li>Descripción: "Beber con agüa fria"</li>
      <li>Dosis: {{ medicine.dosage }}</li>
      <li>Hora: 8:00</li>
      <button class="name-of-day" v-for="day of nameOfDays" :key="day.id">
        {{ day }}
      </button>
      <li>Fecha Inicio: 2022-01-01</li>
      <li>Fecha Fin: {{ medicine.end_date }}</li>
    </ul>
    <section class="area-btns">
      <router-link to="/medicines">
        <input type="checkbox" id="input-delete" />
        <label class="label-input-delete" for="input-delete">Eliminar</label>
      </router-link>
      <router-link to="/medicines">
        <input type="checkbox" id="input-back" />
        <label class="label-input-back" for="input-back">Volver</label>
      </router-link>
    </section>
  </fieldset>
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicineDetail",
  data() {
    return {
      medicine: {},
      idOfMedicine: this.$route.params.id,
      nameOfDays: ["L", "M", "M", "J", "V", "S", "D"],
      daysOfMedicine: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch(
        `${config.API_PATH}/medicines/${this.idOfMedicine}`
      );
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
.medicines-box {
  margin: 10vh auto;
  width: 60vw;
  height: 65vh;
  border: 1px solid #42b983;
  border-radius: 12px;
  display: grid;
  place-items: center;
  overflow: auto;
}
.medicine-name {
  margin: 0.3em;
}

ul > li {
  list-style: none;
  text-align: center;
  margin: 0 3em;
  margin-bottom: 0.4em;
}
button {
  background-color: transparent;
  border: none;
  margin: 2px;
  padding: 2px;
}

.area-btns {
  margin-bottom: 0.5em;
}

.label-input-back,
.label-input-delete {
  cursor: pointer;
  width: fit-content;
  height: fit-content;
  border: 1px solid;
  padding: 0.3em;
  margin: 1em;
  background: #e5e9e8;
  border-radius: 5px;
}
/* .label-input-back:hover{
  background:#42b983;
}
.label-input-delete:hover{
  background:#42b983;
} */
#input-back,
#input-delete {
  display: none;
}
</style>
