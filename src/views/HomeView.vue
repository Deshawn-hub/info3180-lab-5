<script setup>
import { RouterLink } from "vue-router";
import backdropImage from "@/assets/background.webp";

const heroBackground = {
  backgroundImage: `linear-gradient(115deg, rgba(2, 17, 49, 0.92) 0%, rgba(7, 48, 122, 0.76) 52%, rgba(6, 19, 45, 0.9) 100%), url(${backdropImage})`
};
</script>

<template>
  <section class="home-hero" :style="heroBackground">
    <div class="hero-panel">
      <p class="hero-kicker">Streamline Your Watchlist</p>
      <h1 class="hero-title">MovieTask</h1>
      <p class="hero-copy">
        Keep your movie collection, posters, and new uploads in one clean place with a
        cinematic home screen.
      </p>

      <div class="hero-actions">
        <RouterLink to="/movies" class="hero-button hero-button-primary">Browse Movies</RouterLink>
        <RouterLink to="/movies/create" class="hero-button hero-button-secondary">Add Movie</RouterLink>
      </div>
    </div>

    <div class="hero-search-shell">
      <div class="hero-search-bar">
        <span class="search-placeholder">Enter keywords...</span>
        <RouterLink to="/movies" class="search-cta">Explore</RouterLink>
      </div>
    </div>
  </section>
</template>

<style scoped>
.home-hero {
  min-height: calc(100vh - 75px);
  padding: clamp(2rem, 4vw, 3.5rem);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2.5rem;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.hero-panel {
  width: min(100%, 760px);
  padding: clamp(1.75rem, 4vw, 3rem);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 28px;
  background: linear-gradient(180deg, rgba(8, 26, 61, 0.7), rgba(7, 19, 42, 0.5));
  backdrop-filter: blur(10px);
  color: #ffffff;
  box-shadow: 0 28px 60px rgba(0, 0, 0, 0.24);
}

.hero-kicker {
  margin-bottom: 0.75rem;
  color: #ffbf47;
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.hero-title {
  margin: 0;
  font-size: clamp(3rem, 9vw, 5.8rem);
  font-weight: 800;
  line-height: 0.95;
}

.hero-copy {
  width: min(100%, 42rem);
  margin: 1rem 0 0;
  color: rgba(255, 255, 255, 0.84);
  font-size: clamp(1rem, 2.4vw, 1.2rem);
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2rem;
}

.hero-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 10rem;
  padding: 0.9rem 1.4rem;
  border-radius: 999px;
  font-weight: 700;
  text-decoration: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

.hero-button:hover {
  transform: translateY(-2px);
}

.hero-button-primary {
  color: #071632;
  background: linear-gradient(135deg, #ffb11f, #ff7d12);
  box-shadow: 0 14px 24px rgba(255, 145, 17, 0.28);
}

.hero-button-secondary {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.hero-search-shell {
  width: min(100%, 1120px);
}

.hero-search-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1rem 1rem 1.5rem;
  border-radius: 24px;
  background: rgba(250, 252, 255, 0.92);
  box-shadow: 0 22px 50px rgba(2, 11, 31, 0.28);
}

.search-placeholder {
  color: #59708f;
  font-size: clamp(1rem, 2vw, 1.2rem);
}

.search-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.95rem 1.6rem;
  border-radius: 18px;
  background: linear-gradient(135deg, #4f94ff, #2d63d6);
  color: #ffffff;
  font-weight: 700;
  text-decoration: none;
}

@media (max-width: 768px) {
  .home-hero {
    min-height: calc(100vh - 75px);
    padding: 1.25rem;
  }

  .hero-panel {
    border-radius: 22px;
  }

  .hero-search-bar {
    flex-direction: column;
    align-items: stretch;
    padding: 1rem;
  }

  .search-cta {
    width: 100%;
  }
}
</style>
