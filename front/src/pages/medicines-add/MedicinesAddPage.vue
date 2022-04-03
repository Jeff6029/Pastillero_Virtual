<template>
  <fieldset class="medicines-box">
    <legend>Añadir Medicina:</legend>
    <dl class="form-add-medicine">
      <dd>
        <span>Nombre: </span> <input type="text" v-model="this.inputName" />
      </dd>
      <dd>
        <span>Tipo: </span>
        <select name="types" v-model="this.inputType">
          <option hidden value="Select">Elige un tipo</option>
          <option value="Pills">Pastillas</option>
          <option value="Cream">Crema</option>
          <option value="eye_drops">Gotas de ojo</option>
        </select>
      </dd>
      <dd>
        <p><span>Descripción:</span></p>
        <textarea cols="28" rows="5" v-model="this.inputDescription"></textarea>
      </dd>
      <dd>
        <span>Dosis:</span>
        <input
          class="input-number"
          v-model="this.inputDosage"
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
        <span>Hora:</span> <input type="time" v-model="this.inputHour" /> hrs.
      </dd>
      <dd>
        <span>Fecha Inicio:</span>
        <input type="date" v-model="this.inputInitialDate" />
      </dd>
      <dd>
        <span>Fecha Fin:</span>
        <input type="date" v-model="this.inputEndDate" />
      </dd>
    </dl>
    <section class="area-btns">
      <button class="btn-back-save" @click="onClickToReturnListMedicines">
        Volver
      </button>
      <button class="btn-back-save" @click="onSaveClickedMedicine">
        Guardar
      </button>
    </section>
  </fieldset>
</template>


<script>
import config from "@/config";
import { v4 as uuidv4 } from "uuid";
export default {
  name: "MedicinesAdd",
  data() {
    return {
      inputName: "",
      inputType: "",
      inputDescription: "",
      inputDosage: "",
      inputHour: "",
      inputInitialDate: "",
      inputEndDate: "",
      listDays: [],
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
  mounted() {},
  computed: {},
  methods: {
    isValidInputsMedicine() {
      if (
        this.inputName === "" ||
        this.inputType === "" ||
        this.inputDescription === "" ||
        this.inputDosage === "" ||
        this.inputHour === "" ||
        this.inputInitialDate === "" ||
        this.inputEndDate === ""
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
            day.value = true;
            this.listDays.push(day.name);
            return true;
          } else {
            day.value = false;
            return false;
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
      const addMedicine = {
        id_medicine: uuidv4(),
        name_medicine: this.inputName,
        type_medicine: this.inputType,
        description: this.inputDescription,
        dosage: {
          dosages_times: `${this.inputDosage} veces por semana`,
          hour_dosage: this.inputHour,
          days_dosage: this.listDays,
        },
        start_date: this.inputInitialDate,
        end_date: this.inputEndDate,
      };
      const settings = {
        method: "POST",
        body: JSON.stringify(addMedicine),
        headers: {
          "Content-Type": "application/json",
        },
      };
      await fetch(`${config.API_PATH}/medicines`, settings);
      alert("Tu medicación se ha guardado correctamente");
      this.$router.push("/medicines");
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
.btn-back-save {
  cursor: pointer;
  padding: 0.3em;
  margin: 1em;
  border-radius: 5px;
}
/* .label-input-back:hover{
  background:#42b983;
}
.label-input-delete:hover{
  background:#42b983;
} */
</style>