<template>
  <fieldset class="medicines-box">
    <legend><h1>* Editar Medicina:</h1></legend>
    <MedicineForm
      :medicine="medicine"
      :nameOfDays="nameOfDays"
      @changedMedicine="medicineChanged"
      @changedDays="nameOfDaysChanged"
    />

    <section class="area-btns">
      <button class="btn-back" @click="onClickToReturnListMedicines">
        <i class="fa-solid fa-arrow-rotate-left"></i>
      </button>
      <button class="btn-save" @click.prevent="onSaveClickedMedicine">
        <i class="fa-solid fa-bookmark"></i>
      </button>
    </section>
  </fieldset>
</template>


<script>
import { getMedicineById, updateMedicine } from "@/services/api.js";
import MedicineForm from "@/components/MedicineForm.vue";

export default {
  name: "MedicinesUpdate",
  components: {
    MedicineForm,
  },
  data() {
    return {
      idOfMedicine: this.$route.params.id,
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
      nameOfDays: [
        { name: "Lun", value: false },
        { name: "Mar", value: false },
        { name: "Miér", value: false },
        { name: "Juev", value: false },
        { name: "Vier", value: false },
        { name: "Sáb", value: false },
        { name: "Dom", value: false },
      ],
      dosageTimes: "",
    };
  },
  mounted() {
    this.loadData();
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
    onClickToReturnListMedicines() {
      this.$router.push("/medicines");
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
    medicineChanged(newValue) {
      this.medicine = newValue;
    },
    nameOfDaysChanged(newValue) {
      this.nameOfDays = newValue;
    },

    isValidInputsMedicine() {
      if (
        this.medicine.name_medicine === "" ||
        this.medicine.type_medicine === "" ||
        this.medicine.description === "" ||
        this.medicine.dosage.dosages_times ||
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
    async loadData() {
      let responseMedicine = await getMedicineById(this.idOfMedicine);
      this.medicine = responseMedicine;
      this.dosageTimes = responseMedicine.dosage.dosages_times;
      let daysReceived = responseMedicine.dosage.days_dosage;
      this.paintDaysSelected(daysReceived);
    },

    async onSaveClickedMedicine() {
      this.medicine.dosage.days_dosage = this.filterDaysTrue;

      await updateMedicine(this.medicine);
      alert("Tu medicación se ha actualizado");
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
.btn-back,
.btn-save {
  padding: 0.5em;
  cursor: pointer;
  margin: 1em;
  background: #e5e9e8e0;
  color: black;
  border-radius: 5px;
  border: none;
}
.btn-save:hover {
  color: white;
  background: #42b983;
}
.btn-back:hover {
  color: white;
  background: #fa79018e;
}
</style>