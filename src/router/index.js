import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue'
import Movie from '../views/Movie.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      alias: '/about',
      name: 'movies',
      // route level code-splitting
      // this generates a separate chunk (Movies.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Movie
    },
    {
      path: '/movies/create',
      name: 'add-movie',
      component: AddMovieFormView
    }
  ]
})

export default router
