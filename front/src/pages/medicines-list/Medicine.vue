<template>
  <article class="medicine-box">
    <header>
      <h3>{{ medicine.name_medicine }}</h3>
      <router-link :to="`/medicines/${medicine.id_medicine}`">
        <button class="btn-info">
          <i class="fa-solid fa-circle-info"></i>
        </button>
      </router-link>
    </header>
    <ul>
      <li>Tipo: {{ medicine.type_medicine }}</li>
      <li>Descripción: {{ medicine.description }}</li>
      <li>Fecha Fin: {{ medicine.end_date }}</li>
    </ul>
  </article>
</template>

<script>
export default {
  props: {
    medicine: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
header > h3 {
  color: #6fa3df;
}
.medicine-box {
  width: 300px;
  height: 190px;
  border: 2px solid #42b983;
  margin: 3px 0;
  border-radius: 10px;
}
.medicine-box > header {
  padding: 0 2em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}
.btn-info {
  cursor: pointer;
  padding: 5px;
  border: none;
}
.btn-info:hover {
  background: #fa79018e;
  color: white;
  transition: 0.2s all ease-out;
  align-self: center;
  padding-right: 1em;
}

.medicine-box > ul > li {
  list-style: none;
  text-align: left;
  margin: 0 3em;
  margin-bottom: 0.4em;
}
</style>
