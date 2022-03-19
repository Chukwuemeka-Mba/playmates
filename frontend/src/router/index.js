import { createRouter, createWebHashHistory } from "vue-router";
import TheHome from "../views/TheHome.vue";
import ThePlaymate from "../views/ThePlaymate.vue";
import TheSignup from "../views/TheSignup.vue";
import TheLogin from "../views/TheLogin.vue";
import TheAccount from "../views/TheAccount.vue";

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
    path: "/account",
    name: "account",
    component: TheAccount,
  },
  {
    path: "/archives",
    name: "archives",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TheArchives.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
