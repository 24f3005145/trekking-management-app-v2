<template>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2 class="mb-0">

            Staff Management

        </h2>

        <!-- NEW -->
        <button
            class="btn btn-success"
            @click="showModal = true"
        >

            + Add Staff

        </button>

    </div>

    <StaffTable
        :staff="staff"
    />

    <StaffFormModal

        :show="showModal"

        :loading="loading"

        @close="showModal = false"

        @save="handleCreateStaff"

    />

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"

import StaffTable from "@/components/admin/StaffTable.vue"

// UPDATED
import {

    getStaff,

    createStaff

} from "@/services/adminService"

import StaffFormModal from "@/components/admin/StaffFormModal.vue"

const staff = ref([])

const showModal = ref(false)
const loading = ref(false)

// NEW: Load all staff
async function loadStaff() {

    try {

        staff.value = await getStaff()

    }

    catch(error) {

        console.error(error)

    }

}

// NEW
async function handleCreateStaff(data) {

    try {

        loading.value = true

        await createStaff(data)

        showModal.value = false

        await loadStaff()

    }

    catch(error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

onMounted(loadStaff)

</script>