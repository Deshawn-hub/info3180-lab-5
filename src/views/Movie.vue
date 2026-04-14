<script setup>
import { onMounted, ref } from "vue";

const movies = ref([]);
const isLoading = ref(true);
const errorMessage = ref(null);

async function fetchMovies() {
  isLoading.value = true;
  errorMessage.value = null;
  try {
    const response = await fetch("/api/v1/movies");
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    movies.value = data.movies || [];
  } catch (error) {
    console.error("Error fetching movies:", error);
    errorMessage.value = "Failed to load movies.";
  } finally {
    isLoading.value = false;
  }
}

onMounted(() => fetchMovies());
</script>

<template>
  <section class="movies-page">
    <div class="movies-header">
      <h1 class="movies-title">Movies</h1>
    </div>

    <div v-if="isLoading" class="state-message">
      <div class="spinner"></div>
      <p>Loading movies…</p>
    </div>

    <div v-else-if="errorMessage" class="state-message error">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-else-if="movies.length > 0" class="movies-grid">
      <article v-for="movie in movies" :key="movie.id" class="movie-card">
        <div class="poster-wrap">
          <img :src="movie.poster" :alt="movie.title" class="poster-img" />
        </div>
        <div class="movie-info">
          <h2 class="movie-title">{{ movie.title }}</h2>
          <p class="movie-desc">{{ movie.description }}</p>
        </div>
      </article>
    </div>

    <div v-else class="state-message">
      <p>No movies yet. Add your first one!</p>
    </div>
  </section>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

.movies-page {
  width: min(100%, 1100px);
  margin: 0 auto;
  padding: 2.5rem 1.5rem 5rem;
  font-family: 'Inter', sans-serif;
}

.movies-header { margin-bottom: 1.75rem; }

.movies-title {
  margin: 0;
  font-size: clamp(2rem, 4vw, 2.75rem);
  font-weight: 700;
  color: #ffffff;
  line-height: 1;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.movie-card {
  display: flex;
  flex-direction: row;
  align-items: flex-start;   /* children sit at top */
  background: #ffffff;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0 0 0 / 0.25);
  transition: box-shadow 0.22s ease, transform 0.22s ease;
  cursor: pointer;
}

.movie-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0 0 0 / 0.4);
}

/* ── Poster: fixed size, never stretches ─────────── */
.poster-wrap {
  flex-shrink: 0;
  width: 180px;
  height: 260px;            /* locked — text length has zero effect */
  align-self: flex-start;
}

.poster-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  display: block;
}

/* ── Text side ───────────────────────────────────── */
.movie-info {
  flex: 1;
  min-width: 0;
  padding: 1.25rem 1.4rem;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.movie-title {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.3;
}

.movie-desc {
  margin: 0;
  font-size: 0.92rem;
  color: #475569;
  line-height: 1.7;
  white-space: normal;
  overflow-wrap: break-word;
  word-break: break-word;
}

/* ── States ──────────────────────────────────────── */
.state-message {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 5rem 0;
  color: rgba(255 255 255 / 0.45);
}

.state-message.error { color: #f87171; }

.spinner {
  width: 30px;
  height: 30px;
  border: 2px solid rgba(255 255 255 / 0.15);
  border-top-color: rgba(255 255 255 / 0.7);
  border-radius: 50%;
  animation: spin 0.75s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

@media (max-width: 780px) {
  .movies-grid { grid-template-columns: 1fr; }
}

@media (max-width: 480px) {
  .poster-wrap { width: 130px; height: 200px; }
  .movie-title { font-size: 1.05rem; }
  .movie-desc  { font-size: 0.85rem; }
}
</style>