
<template>
  <nav class="navbar navbar-expand-lg bg-white shadow-sm px-4">
    <div class="container-fluid">

      <!-- Application Title -->
      <h4 class="mb-0 fw-bold">
        Trekking Management System
      </h4>

      <!-- User Menu -->
      <div class="dropdown">

        <button
          class="btn btn-outline-success dropdown-toggle"
          data-bs-toggle="dropdown"
        >
          Welcome, {{ userName }}
        </button>

        <ul class="dropdown-menu dropdown-menu-end">

          <li>
            <button
              class="dropdown-item"
              @click="goToProfile"
            >
              Profile
            </button>
          </li>

          <li>
            <hr class="dropdown-divider">
          </li>

          <li>
            <button
              class="dropdown-item text-danger"
              @click="handleLogout"
            >
              Logout
            </button>
          </li>

        </ul>

      </div>

    </div>
  </nav>
</template>

<script setup>

// =========================================================
// Imports
// =========================================================

import { computed } from "vue"
import { useRouter } from "vue-router"

import { useAuthStore } from "@/stores/auth"

// =========================================================
// Router & Store
// =========================================================

const router = useRouter()

const authStore = useAuthStore()

// =========================================================
// Computed Properties
// =========================================================

// Display the logged-in user's name.
const userName = computed(() => {

    return authStore.user?.name || "User"

})

// =========================================================
// Methods
// =========================================================

// Navigate to the user's profile page.
function goToProfile() {

    const role = authStore.user?.role

    if (role === "Trek Staff") {

        router.push("/dashboard/staff/profile")

    }

    else if (role === "Trekker") {

        router.push("/dashboard/trekker/profile")

    }

}

// Log out the current user.
function handleLogout() {

    authStore.logout()

    router.push("/login")

}

</script>
