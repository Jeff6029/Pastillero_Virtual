<template>
  <fieldset class="medicines-box">
    <legend>+ Información:</legend>
    <h2 class="medicine-name">{{ medicine.name_medicine }}</h2>
    <ul>
      <li><span>Tipo:</span> {{ medicine.type_medicine }}</li>
      <li><span>Descripción:</span> {{ medicine.description }}</li>
      <li><span>Dosis:</span> {{ dosage.dosages_times }}</li>
      <button
        v-for="day of nameOfDays"
        :class="{ 'name-of-day': day.value }"
        :key="day.id"
      >
        {{ day.name }}
      </button>
      <li><span>Hora:</span> {{ dosage.hour_dosage }} hrs.</li>
      <li><span>Fecha Inicio:</span> {{ medicine.start_date }}</li>
      <li><span>Fecha Fin:</span> {{ medicine.end_date }}</li>
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
      idOfMedicine: this.$route.params.id,
      medicine: {},
      dosage: {},
      nameOfDays: [
        { name: "Lun", value: false },
        { name: "Mar", value: false },
        { name: "Miér", value: false },
        { name: "Juev", value: false },
        { name: "Vier", value: false },
        { name: "Sáb", value: false },
        { name: "Dom", value: false },
      ],
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
      let daysReceived = responseMedicine.dosage.days_dosage;
      this.printDays(daysReceived);
    },
    printDays(array) {
      let array1 = this.nameOfDays;
      for (let day of array) {
        for (let compare of array1) {
          if (day === compare.name) {
            compare.value = true;
          }
        }
      }
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
span {
  font-weight: bolder;
}

ul > li {
  list-style: none;
  text-align: center;
  margin: 0 3em;
  margin-bottom: 0.3em;
}
button {
  color: #9ea1a0ea;
  background-color: transparent;
  border: none;
  margin: 0.25em;
  padding: 0.25em;
}

.name-of-day {
  margin-bottom: 0.5em;
  color: white;
  font-weight: bold;
  background-color: #42b983;
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
