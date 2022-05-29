<template>
  <article class="medicine-box">
    <header>
      <h3>{{ medicine.name_medicine }}</h3>
      <router-link :to="`/medicines/${medicine.id_medicine}`">
        <button class="btn-info">+ Info</button>
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
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.medicine-box {
  width: 300px;
  border: 2px solid #42b983;
  margin: 3px 0;
}
.medicine-box > header {
  padding: 0 2em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}
.btn-info {
  cursor: pointer;
  padding: 2px;
}

.medicine-box > ul > li {
  list-style: none;
  text-align: left;
  margin: 0 3em;
  margin-bottom: 0.4em;
}
</style>
