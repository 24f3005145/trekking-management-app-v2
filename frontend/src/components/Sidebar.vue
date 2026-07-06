<template>

<div
class="bg-dark text-white vh-100 p-3"
style="width:250px;">

    <h3 class="mb-4">

        🥾 TrekMate

    </h3>

    <ul class="nav flex-column">

    <!-- ========================= -->
    <!-- Admin Menu -->
    <!-- ========================= -->

    <template v-if="role === 'Admin'">

        <li class="nav-item mb-2">
        <RouterLink
            to="/dashboard/admin"
            class="nav-link text-white">
            Dashboard
        </RouterLink>
        </li>

        <li class="nav-item mb-2">
        <RouterLink
            to="/dashboard/admin/treks"
            class="nav-link text-white">
            Treks
        </RouterLink>
        </li>

        <li class="nav-item mb-2">
        <RouterLink
            to="/dashboard/admin/staff"
            class="nav-link text-white">
            Staff
        </RouterLink>
        </li>

    </template>

    <!-- ========================= -->
    <!-- Staff Menu -->
    <!-- ========================= -->

        <template v-else-if="role === 'Trek Staff'">

            <li class="nav-item mb-2">
            <RouterLink
                to="/dashboard/staff"
                class="nav-link text-white">
                Dashboard
            </RouterLink>
            </li>

            <li class="nav-item mb-2">
            <RouterLink
                to="/dashboard/staff/treks"
                class="nav-link text-white">
                My Treks
            </RouterLink>
            </li>

        </template>

        <li class="nav-item mt-4">

            <button
            class="btn btn-danger w-100"
            @click="handleLogout">

            Logout

            </button>

        </li>

    </ul>

</div>

</template>

<script setup>

import { RouterLink, useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth"

const router = useRouter()

const authStore = useAuthStore()

const role = authStore.user?.role

// =====================================
// Logout Handler
// =====================================

function handleLogout() {

    authStore.logout()

    router.push("/login")

}

</script>