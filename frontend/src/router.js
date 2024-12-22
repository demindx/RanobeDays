import { createMemoryHistory, createRouter } from 'vue-router';
import App from './App.vue';
import CatalogVeiw from './CatalogView.vue';
import HomeView from './HomeView.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/catalog', component: CatalogVeiw },

]

const router = createRouter({
  history: createMemoryHistory(),
  routes
})

export default router
