<template>
  <nav class="navbar navbar-expand-lg bg-white shadow-sm px-4">
    <div class="container-fluid">

      <h4 class="mb-0 fw-bold">
        Trekking Management System
      </h4>

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

// =====================================================
// NEW
// =====================================================

import { computed } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth"

const router = useRouter()

const authStore = useAuthStore()

// =====================================================
// NEW
// Display logged-in user's name
// =====================================================

const userName = computed(() => {

    return authStore.user?.name || "User"

})

// =====================================================
// NEW
// Placeholder Profile navigation
// =====================================================

function goToProfile() {

    alert("Profile page will be added in a later sprint.")

}

// =====================================================
// NEW
// Logout
// =====================================================

function handleLogout() {

    authStore.logout()

    router.push("/login")

}

</script>