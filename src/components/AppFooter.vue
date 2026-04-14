<template>
  <footer class="app-footer">
    <div class="page-shell footer-shell">
      <p class="footer-copy">Copyright &copy; {{ year }} MovieTask. Built with Flask and Vue.</p>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.app-footer {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(2, 10, 23, 0.78);
  backdrop-filter: blur(10px);
}

.footer-shell {
  padding-top: 1.4rem;
  padding-bottom: 1.4rem;
}

.footer-copy {
  margin: 0;
  color: rgba(237, 244, 255, 0.62);
  text-align: center;
}
</style>
