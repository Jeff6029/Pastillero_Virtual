<template>
  <h1>Bienvenido</h1>
  <div class="login">
    <form action class="form">
      <label class="form-label" for="#email">Usuario:</label>
      <input
        class="form-input"
        type="email"
        id="email"
        required
        placeholder="Introduce usuario"
        v-model="user"
      />
      <label class="form-label" for="#password">Clave:</label>
      <input
        class="form-input"
        type="password"
        id="password"
        placeholder="Introduce contraseña..."
        v-model="password"
      />
      <button class="form-submit" @click="onButtonClicked">Login</button>
    </form>
  </div>
</template>

<script>
import { login } from "@/services/auth.js";
import { useStorage } from "@vueuse/core";

export default {
  name: "Home",
  data() {
    return {
      user: "",
      password: "",
      auth: useStorage("auth", {}),
    };
  },
  methods: {
    async onButtonClicked() {
      const response = await login(this.user, this.password);
      const loginStatus = response.status;

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        const auth = await response.json();

        this.auth = auth;
        this.$router.push("/medicines");
      }
    },
  },
};
</script>

<style scoped>
h1 {
  font-style: italic;
}
.login {
  padding: 2rem;
}
.title {
  text-align: center;
}
.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 20%;
  min-width: 350px;
  max-width: 100%;
  background: rgba(70, 134, 183, 0.648);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: white;
  margin-bottom: 0.5rem;
}
.form-label:first-of-type {
  margin-top: 0rem;
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: white;
}
.form-input:focus {
  outline: 0;
  border-color: #1ab188;
}
.form-submit {
  background: #1ab188;
  border: none;
  color: white;
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
}
.form-submit:hover {
  background: #0b9185;
}
</style>
