<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-success shadow-sm">
    <div class="container">

      <RouterLink class="navbar-brand fw-bold fs-4" to="/">
        🥾 TrekMate
      </RouterLink>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbar">

        <span class="navbar-toggler-icon"></span>

      </button>

      <div
        class="collapse navbar-collapse"
        id="navbar">

        <ul class="navbar-nav ms-auto align-items-lg-center">

          <li class="nav-item">
            <RouterLink class="nav-link" to="/">
              Home
            </RouterLink>
          </li>

          <li class="nav-item">
            <RouterLink class="nav-link" to="/login">
              Login
            </RouterLink>
          </li>

          <li class="nav-item ms-lg-2">
            <RouterLink
              class="btn btn-light text-success fw-bold"
              to="/register">

              Register

            </RouterLink>
          </li>

        </ul>

      </div>

    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>