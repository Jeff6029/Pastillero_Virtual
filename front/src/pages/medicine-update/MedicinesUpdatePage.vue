<template>
  <fieldset class="medicines-box">
    <legend>Editar Medicina:</legend>
    <MedicineForm
      :medicine="medicine"
      :inputDosage="inputDosage"
      @changed="onMedicineChanged"
    />

    <section class="area-btns">
      <button class="btn-back" @click="onClickToReturnListMedicines">
        Volver
      </button>
      <button class="btn-save" @click="onSaveClickedMedicine">Guardar</button>
    </section>
  </fieldset>
  {{ medicine }}
</template>


<script>
import config from "@/config";
import { getMedicineById } from "@/services/api.js";
import MedicineForm from "@/components/MedicineForm.vue";

export default {
  name: "MedicinesUpdate",
  components: {
    MedicineForm,
  },
  data() {
    return {
      medicine: {
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
      listDays: [],
    };
  },
  mounted() {
    this.loadData();
  },
  computed: {},
  methods: {
    isValidInputsMedicine() {
      if (
        this.medicine.name_medicine === "" ||
        this.medicine.type_medicine === "" ||
        this.medicine.description === "" ||
        this.inputDosage === "" ||
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
    onMedicineChanged(newValue) {
      this.medicine = newValue;
    },

    onClickToReturnListMedicines() {
      this.$router.push("/medicines");
    },
    async loadData() {
      let medicineId = this.$route.params.id;
      this.medicine = await getMedicineById(medicineId);
    },
    async onSaveClickedMedicine() {
      if (!this.isValidInputsMedicine()) {
        alert("Rellena correctamente los campos");
        return;
      }
      const addMedicine = this.medicine;
      addMedicine.dosage.dosages_times = `${this.inputDosage} veces por semana`;
      addMedicine.dosage.days_dosage = this.filterDaysTrue;
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
.btn-back,
.btn-save {
  cursor: pointer;
  padding: 0.3em;
  margin: 1em;
  border-radius: 5px;
}
.btn-save:hover {
  color: white;
  background: #42b983;
}
.btn-back:hover {
  color: white;
  background: #b72f2fef;
}
</style>