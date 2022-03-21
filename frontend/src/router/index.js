import { createRouter, createWebHashHistory } from "vue-router";
import TheHome from "../views/TheHome.vue";
import ThePlaymate from "../views/ThePlaymate.vue";
import TheSignup from "../views/TheSignup.vue";
import TheLogin from "../views/TheLogin.vue";
import TheAccount from "../views/TheAccount.vue";
import store from "@/store/index";

const routes = [
  {
    path: "/",
    name: "home",
    component: TheHome,
  },
  {
    path: "/archives",
    name: "archives",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TheArchives.vue"),
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/playmate/:id",
    name: "playmate",
    component: ThePlaymate,
    meta: {
      requireLogin: true,
    },
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
    meta: {
      requireLogin: true,
    },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next({ name: "TheLogin", query: { to: to.path } });
  } else {
    next();
  }
});
export default router;
