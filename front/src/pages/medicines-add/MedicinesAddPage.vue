<template>
  <fieldset class="medicines-box">
    <legend><h1>+ Añadir Medicina:</h1></legend>
    <dl class="form-add-medicine">
      <dd>
        <span>Nombre: </span>
        <input type="text" v-model="this.medicine.name_medicine" />
      </dd>
      <dd>
        <span>Tipo: </span>
        <select name="types" v-model="this.medicine.type_medicine">
          <option hidden value="Select">Elige un tipo</option>
          <option value="Pills">Pastillas</option>
          <option value="Cream">Crema</option>
          <option value="eye_drops">Gotas de ojo</option>
        </select>
      </dd>
      <dd>
        <p><span>Descripción:</span></p>
        <textarea
          cols="28"
          rows="5"
          v-model="this.medicine.description"
        ></textarea>
      </dd>
      <dd>
        <span>Dosis:</span>
        <input
          class="input-number"
          v-model="this.medicine.dosage.dosages_times"
          type="number"
          min="0"
          max="7"
        />
        dosis por semana
      </dd>
      <dd class="name-days">
        <button
          @click="onClickNameDay(day.name)"
          v-for="day of nameOfDays"
          :key="day.id"
          class="names-days"
          :class="{ 'name-of-day': day.value }"
        >
          {{ day.name }}
        </button>
      </dd>
      <dd>
        <span>Hora:</span>
        <input type="time" v-model="this.medicine.dosage.hour_dosage" /> hrs.
      </dd>
      <dd>
        <span>Fecha Inicio:</span>
        <input type="date" v-model="this.medicine.start_date" />
      </dd>
      <dd>
        <span>Fecha Fin:</span>
        <input type="date" v-model="this.medicine.end_date" />
      </dd>
    </dl>
    <section class="area-btns">
      <button class="btn-back" @click="onClickToReturnListMedicines">
        <i class="fa-solid fa-arrow-rotate-left"></i>
      </button>
      <button class="btn-save" @click="onSaveClickedMedicine">
        <i class="fa-solid fa-plus"></i>
      </button>
    </section>
  </fieldset>
</template>


<script>
import { saveMedicine } from "@/services/api.js";
export default {
  name: "MedicinesAdd",
  data() {
    return {
      medicine: {
        id_medicine: "",
        name_medicine: "",
        type_medicine: "",
        description: "",
        dosage: {
          dosages_times: "",
          hour_dosage: "",
          days_dosage: [],
        },
        start_date: "",
        end_date: "",
      },
      inputDosage: "",
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
  computed: {
    filterDaysTrue() {
      let listDays = this.nameOfDays;
      const filterOfDaysTrue = listDays
        .filter((i) => {
          if (i.value === true) {
            return i.name;
          }
        })
        .map((i) => i.name);
      return filterOfDaysTrue;
    },
  },
  methods: {
    isValidInputsMedicine() {
      if (
        this.medicine.name_medicine === "" ||
        this.medicine.type_medicine === "" ||
        this.medicine.description === "" ||
        this.medicine.dosage.dosages_times === "" ||
        this.medicine.dosage.hour_dosage === "" ||
        this.medicine.dosage.days_dosage === "" ||
        this.medicine.start_date === "" ||
        this.medicine.end_date === ""
      ) {
        return false;
      } else {
        return true;
      }
    },
    onClickNameDay(someday) {
      for (let day of this.nameOfDays) {
        if (someday === day.name) {
          if (day.value === false) {
            return (day.value = true);
          } else {
            return (day.value = false);
          }
        }
      }
    },

    onClickToReturnListMedicines() {
      this.$router.push("/medicines");
    },
    async onSaveClickedMedicine() {
      if (!this.isValidInputsMedicine()) {
        alert("Rellena correctamente los campos");
        return;
      }
      let addMedicine = this.medicine;
      addMedicine.dosage.days_dosage = this.filterDaysTrue;

      await saveMedicine(addMedicine);
      alert("Tu medicación se ha guardado correctamente");
      this.$router.push("/medicines");
    },
  },
};
</script>

<style scoped>
.medicines-box {
  margin: 5vh auto;
  width: 50vw;
  height: 70vh;
  border: 1px solid #42b983;
  border-radius: 12px;
  display: grid;
  place-items: center;
  overflow: auto;
}
span {
  font-weight: bolder;
}
dl > dd {
  text-align: center;
  padding: 0.3em 0.59em;
}
.input-number {
  width: 40px;
  text-align: center;
  margin-left: 5px;
}
.names-days {
  color: #9ea1a0ea;
  background-color: transparent;
  border: 1.5px solid #9ea1a0ea;
  margin: 0.15em;
  padding: 0.15em;
  cursor: pointer;
}
.name-of-day {
  color: white;
  font-weight: bold;
  background-color: #42b983;
}

.btn-save,
.btn-back {
  cursor: pointer;
  padding: 8px;
  margin: 1em;
  background: #e5e9e8;
  color: black;
  border-radius: 5px;
  border: none;
}
.btn-save:hover {
  background: #6dc39c;
  color: white;
  border: 1px solid white;
  transition: 0.2s all ease-out;
}
.btn-back:hover {
  background: #fa79018e;
  color: white;
  border: 1px solid white;
  transition: 0.2s all ease-out;
}
</style>