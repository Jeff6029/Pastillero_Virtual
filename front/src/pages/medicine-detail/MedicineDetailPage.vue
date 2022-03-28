<template>
  <fieldset class="medicines-box">
    <legend>+ Información:</legend>
    <h2 class="medicine-name">{{ medicine.name_medicine }}</h2>
    <ul>
      <li>Tipo: {{ medicine.type_medicine }}</li>
      <li>Descripción: {{ medicine.description }}</li>
      <li>Dosis: {{ dosage.dosages_times }}</li>
      <li>Hora: {{ dosage.hour_dosage }}</li>
      <button
        v-for="day of nameOfDays"
        :class="{ 'name-of-day': day.value }"
        :key="day.id"
      >
        {{ day.name }}
      </button>
      <li>Fecha Inicio: {{ medicine.start_date }}</li>
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
  {{ $data.dosage }}
</template>

<script>
import config from "@/config.js";
export default {
  name: "MedicineDetail",
  data() {
    return {
      idOfMedicine: this.$route.params.id,
      medicine: {},
      dosage: {},
      nameOfDays: [
        { name: "Lun", value: false },
        { name: "Mar", value: false },
        { name: "Mier", value: false },
        { name: "Juev", value: false },
        { name: "Vier", value: false },
        { name: "Sab", value: false },
        { name: "Dom", value: false },
      ],
      daysOfMedicine: ["Mar", "Juev", "Sab"],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {},
  methods: {
    async loadData() {
      const response = await fetch(
        `${config.API_PATH}/medicines/${this.idOfMedicine}`
      );
      let responseMedicine = await response.json();
      this.medicine = responseMedicine;
      this.dosage = responseMedicine.dosage;
    },
    printDays() {
      let array1 = this.nameOfDays;
      let array2 = this.daysOfMedicine;
      for (let day of array2) {
        for (let compare of array1) {
          if (day === compare.name) {
            compare.value = true;
          }
        }
      }
      console.table(array1);
      return array1;
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
  width: 70vw;
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

.name-of-day {
  background-color: #42b983;
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
