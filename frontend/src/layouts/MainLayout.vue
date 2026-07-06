<template>

<div class="d-flex">

    <Sidebar />

    <div class="flex-grow-1">

        <DashboardNavbar />

        <main class="p-4">

            <router-view />

        </main>

    </div>

</div>

</template>

<script setup>

import DashboardNavbar from '@/components/DashboardNavbar.vue'
import Sidebar from '@/components/Sidebar.vue'

</script>