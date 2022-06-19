<template>
  <fieldset class="medicines-box">
    <legend class="title_fielset"><h1>+ Información:</h1></legend>
    <h2 class="medicine-name">{{ medicine.name_medicine }}</h2>
    <ul>
      <li><span>Tipo:</span> {{ medicine.type_medicine }}</li>
      <li><span>Descripción:</span> {{ medicine.description }}</li>
      <li><span>Dosis:</span> {{ dosage.dosages_times }} dosis por semana</li>
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
      <button class="btn-delete" @click="onDeleteClickMedicine">
        <i class="fa-solid fa-trash-can"></i>
      </button>

      <button class="btn-back" @click="onClickToReturnListMedicines">
        <i class="fa-solid fa-arrow-rotate-left"></i>
      </button>

      <button class="btn-update" @click="onClickToUpdateMedicine">
        <i class="fa-solid fa-pen"></i>
      </button>
    </section>
  </fieldset>
</template>

<script>
import { getMedicineById, deleteMedicine } from "@/services/api.js";
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
  methods: {
    async loadData() {
      let responseMedicine = await getMedicineById(this.idOfMedicine);

      this.medicine = responseMedicine;
      this.dosage = responseMedicine.dosage;
      let daysReceived = responseMedicine.dosage.days_dosage;
      this.paintDaysSelected(daysReceived);
    },
    async onDeleteClickMedicine() {
      if (confirm("¿Deseas eliminar este evento?")) {
        this.onClickToReturnListMedicines();
        await deleteMedicine(this.idOfMedicine);
      } else {
        return "";
      }
    },
    onClickToReturnListMedicines() {
      this.$router.push("/medicines");
    },
    onClickToUpdateMedicine() {
      this.$router.push(`/medicines/${this.idOfMedicine}/update`);
    },

    paintDaysSelected(array) {
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
.title_fielset {
  text-align: left;
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
ul > button {
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

.btn-update,
.btn-delete,
.btn-back {
  cursor: pointer;
  padding: 8px;
  margin: 1em;
  background: #e5e9e8;
  color: black;
  border-radius: 5px;
  border: none;
}
.btn-update:hover {
  background: #fa79018e;
  color: white;
  border: 1px solid white;
  transition: 0.2s all ease-out;
}
.btn-back:hover {
  background: #6dc39c;
  color: white;
  border: 1px solid white;
  transition: 0.2s all ease-out;
}
.btn-delete:hover {
  background: #df4f4fea;
  color: white;
  border: 1px solid white;
  transition: 0.2s all ease-out;
}
</style>
