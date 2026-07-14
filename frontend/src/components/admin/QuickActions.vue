<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">

      <!-- Card Heading -->
      <h4 class="mb-4">
        Quick Actions
      </h4>

      <!-- Quick Action Buttons -->
      <div class="d-flex gap-3 flex-wrap">

        <RouterLink
          to="/dashboard/admin/treks?add=true"
          class="btn btn-success"
        >
          Add Trek
        </RouterLink>

        <RouterLink
          to="/dashboard/admin/staff?add=true"
          class="btn btn-primary"
        >
          Add Staff
        </RouterLink>

        <RouterLink
          to="/dashboard/admin/reports"
          class="btn btn-warning"
        >
          View Reports
        </RouterLink>

      </div>

    </div>
  </div>
</template>

<script setup>
// =========================================================
// Imports
// =========================================================

import { RouterLink } from "vue-router"
</script>