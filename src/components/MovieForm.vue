<script setup>
import { onMounted, ref } from "vue";

const csrf_token = ref("");
const message = ref("");
const errors = ref([]);

function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.log(error);
    });
}

function saveMovie() {
  const movieForm = document.getElementById("movieForm");
  const form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        errors.value = data.errors;
        message.value = "";
      } else {
        message.value = data.message;
        errors.value = [];
        movieForm.reset();
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

onMounted(() => {
  getCsrfToken();
});
</script>

<template>
  <section class="page-shell">
    <div class="glass-panel form-panel">
      <div class="form-heading">
        <p class="form-kicker">Upload</p>
        <h1 class="section-title">Add Movie</h1>
        <p class="section-copy">Save a title, a short description, and a poster image.</p>
      </div>

      <div v-if="message" class="feedback feedback-success">
        {{ message }}
      </div>

      <div v-if="errors.length > 0" class="feedback feedback-error">
        <ul class="feedback-list">
          <li v-for="(error, index) in errors" :key="index">
            {{ error }}
          </li>
        </ul>
      </div>

      <form id="movieForm" class="movie-form" @submit.prevent="saveMovie" enctype="multipart/form-data">
        <div class="field-group">
          <label for="title" class="field-label">Movie Title</label>
          <input type="text" name="title" id="title" class="field-input" />
        </div>

        <div class="field-group">
          <label for="description" class="field-label">Description</label>
          <textarea
            name="description"
            id="description"
            class="field-input field-textarea"
            rows="4"
          ></textarea>
        </div>

        <div class="field-group">
          <label for="poster" class="field-label">Movie Poster</label>
          <input type="file" name="poster" id="poster" class="field-input field-file" />
        </div>

        <button type="submit" class="submit-button">Save Movie</button>
      </form>
    </div>
  </section>
</template>

<style scoped>
.form-panel {
  width: min(100%, 760px);
  margin: 0 auto;
  padding: 2rem;
}

.form-heading {
  margin-bottom: 1.5rem;
}

.form-kicker {
  margin-bottom: 0.75rem;
  color: var(--app-highlight);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.feedback {
  margin-bottom: 1rem;
  padding: 0.95rem 1rem;
  border-radius: 16px;
  font-weight: 600;
}

.feedback-success {
  background: rgba(32, 172, 109, 0.22);
  border: 1px solid rgba(32, 172, 109, 0.45);
  color: #ffffff;
}

.feedback-error {
  background: rgba(209, 77, 92, 0.2);
  border: 1px solid rgba(209, 77, 92, 0.4);
  color: #ffffff;
}

.feedback-list {
  margin: 0;
  padding-left: 1.2rem;
}

.movie-form {
  display: grid;
  gap: 1.1rem;
}

.field-group {
  display: grid;
  gap: 0.55rem;
}

.field-label {
  color: var(--app-text);
  font-weight: 600;
}

.field-input {
  width: 100%;
  padding: 0.95rem 1rem;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  background: rgba(4, 16, 38, 0.8);
  color: var(--app-text);
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.field-input::placeholder {
  color: rgba(237, 244, 255, 0.58);
}

.field-input:focus {
  border-color: rgba(79, 148, 255, 0.7);
  box-shadow: 0 0 0 0.2rem rgba(79, 148, 255, 0.16);
}

.field-textarea {
  resize: vertical;
  min-height: 7rem;
}

.field-file {
  padding: 0.8rem 1rem;
  color: #ffffff;
}

.field-file::file-selector-button {
  margin-right: 0.9rem;
  padding: 0.65rem 1rem;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(135deg, #4f94ff, #2d63d6);
  color: #ffffff;
  font-weight: 700;
}

.submit-button {
  width: fit-content;
  margin-top: 0.25rem;
  padding: 0.95rem 1.55rem;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(135deg, #ffb11f, #ff7d12);
  color: #071632;
  font-weight: 800;
  box-shadow: 0 14px 24px rgba(255, 145, 17, 0.24);
}

.submit-button:hover {
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .form-panel {
    padding: 1.35rem;
  }

  .submit-button {
    width: 100%;
  }
}
</style>
