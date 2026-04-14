<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top app-navbar">
      <div class="container-fluid">
        <RouterLink to="/" class="navbar-brand app-brand">MovieTask</RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto d-flex gap-2" id="navbarNav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/movies" class="nav-link">Movies</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/movies/create" class="nav-link">Add Movie</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>
.app-navbar {
  padding: 0.9rem 1rem;
  background: rgba(4, 15, 36, 0.78);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(18px);
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.18);
}

.app-brand {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 0.03em;
  color: #ffffff;
}

.app-brand:hover {
  color: #ffcb61;
}

#navbarNav {
  gap: 10px;
}

#navbarNav :deep(.nav-link) {
  padding: 0.2rem 0;
  color: rgba(255, 255, 255, 0.76);
  font-weight: 700;
  letter-spacing: 0.03em;
}

#navbarNav :deep(.nav-link:hover) {
  color: #ffffff;
}

#navbarNav :deep(.router-link-active) {
  color: #ffffff;
  border-bottom: 2px solid #ffb11f;
}

.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.22);
}

.navbar-toggler:focus {
  box-shadow: 0 0 0 0.2rem rgba(79, 148, 255, 0.24);
}
</style>
