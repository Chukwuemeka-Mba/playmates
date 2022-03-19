import { createRouter, createWebHashHistory } from "vue-router";
import TheHome from "../views/TheHome.vue";
import ThePlaymate from "../views/ThePlaymate.vue";
import TheSignup from "../views/TheSignup.vue";
import TheLogin from "../views/TheLogin.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: TheHome,
  },
  {
    path: "/playmate/:id",
    name: "playmate",
    component: ThePlaymate,
  },
  {
    path: "/signup",
    name: "signup",
    component: TheSignup,
  },
  {
    path: "/login",
    name: "login",
    component: TheLogin,
  },
  {
    path: "/archives",
    name: "archives",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TheArchives.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
