<template>
  <dl class="form-add-medicine">
    <dd>
      <span>Nombre: </span>
      <input
        type="text"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.name_medicine"
      />
    </dd>
    <dd>
      <span>Tipo: </span>
      <select
        name="types"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.type_medicine"
      >
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
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.description"
      ></textarea>
    </dd>
    <dd>
      <span>Dosis:</span>
      <input
        class="input-number"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.dosage.dosages_times"
        type="number"
        min="0"
        max="7"
      />
      dosis por día
    </dd>
    <dd class="name-days">
      <button
        @click="onClickNameDay(day.name) && onNameOfDaysChanged"
        v-for="day of nameOfDaysInForm"
        :key="day.id"
        class="names-days"
        :class="{ 'name-of-day': day.value }"
      >
        {{ day.name }}
      </button>
    </dd>
    <dd>
      <span>Hora:</span>
      <input
        type="time"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.dosage.hour_dosage"
      />
      hrs.
    </dd>
    <dd>
      <span>Fecha Inicio:</span>
      <input
        type="date"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.start_date"
      />
    </dd>
    <dd>
      <span>Fecha Fin:</span>
      <input
        type="date"
        @keyup="onMedicineChanged"
        v-model="this.medicineInForm.end_date"
      />
    </dd>
  </dl>
</template>


<script>
export default {
  name: "MedicineForm",
  props: {
    medicine: {
      type: Object,
      required: true,
    },
    nameOfDays: {
      type: Object,
      required: true,
    },
  },
  emits: ["changedMedicine", "changedDays"],
  watch: {
    medicine: {
      handler(newValue) {
        const medicineAsJson = JSON.stringify(newValue);
        this.medicineInForm = JSON.parse(medicineAsJson);
      },
      inmediate: true,
    },
    nameOfDays: {
      handler(newValue) {
        const medicineAsJson = JSON.stringify(newValue);
        this.medicineInForm = JSON.parse(medicineAsJson);
      },
      inmediate: true,
    },
  },
  data() {
    return {
      medicineInForm: this.medicine,
      nameOfDaysInForm: this.nameOfDays,
    };
  },
  computed: {},
  methods: {
    onClickNameDay(someday) {
      for (let day of this.nameOfDaysInForm) {
        if (someday === day.name) {
          if (day.value === false) {
            return (day.value = true);
          } else {
            return (day.value = false);
          }
        }
      }
    },
    onMedicineChanged() {
      this.$emit("changedMedicine", this.medicineInForm);
    },
    onNameOfDaysChanged() {
      this.$emit("changedDays", this.nameOfDaysInForm);
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
</style>