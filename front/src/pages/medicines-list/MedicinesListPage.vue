<template>
  <h1>Mis Medicamentos</h1>
  <nav class="area-btns">
    <button>Añadir Medicamento</button>
    <button>Calendario</button>
  </nav>
  <section class="medicines-list">
    <article class="medicine-box">
      <header>
        <h3>Paracetamol</h3>
        <button>+ info</button>
      </header>
      <p>Tipo: Pastillas</p>
      <p>Dosis: 2 veces por semana</p>
      <p>Fecha Fin: 30/06/2022</p>
    </article>
    <article class="medicine-box">
      <header>
        <h3>Bephantol</h3>
        <button>+ info</button>
      </header>
      <p>Tipo: Crema</p>
      <p>Dosis: 3 veces por semana</p>
      <p>Fecha Fin: 30/05/2022</p>
    </article>
  </section>
</template>
<script>
export default {
  name: "MedicinesList",
  data() {
    return {
      info: {},
    };
  },
  // mounted() {
  //   this.loadData();
  // },
  // methods: {
  //   async loadData() {
  //     const response = await fetch('http://localhost:5000/api/info')
  //     this.info = await response.json()
  //   }
  // }
};
</script>
<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
body {
  width: 100vw;
}
.area-btns {
  /* border: 2px solid #42b983; */
  padding: 0 3em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}
.medicine-box {
  border: 2px solid #42b983;
}
.medicine-box > header {
  padding: 0 2em;
  margin: 1em 0;
  display: flex;
  justify-content: space-between;
}
</style>
