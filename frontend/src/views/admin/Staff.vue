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
        @toggle-status="toggleStatus"
        @view-treks="viewTreks"
    />

    <StaffFormModal

        :show="showModal"

        :loading="loading"

        @close="showModal = false"

        @save="handleCreateStaff"

    />

    <StaffTreksModal

        :show="showTreksModal"

        :treks="staffTreks"

        @close="showTreksModal = false"

    />

</div>

</template>

<script setup>

import { ref, onMounted, watch } from "vue"

import StaffTable from "@/components/admin/StaffTable.vue"

import { useToastStore } from "@/stores/toast"                       // Toast

import { useRoute } from "vue-router"
const route = useRoute()

// UPDATED
import {

    getStaff,

    createStaff,

    updateStaffStatus,

    getStaffTreks

} from "@/services/adminService"

import StaffTreksModal from "@/components/admin/StaffTreksModal.vue"
import StaffFormModal from "@/components/admin/StaffFormModal.vue"

const staff = ref([])

const toast = useToastStore()                   // Toast

const showModal = ref(false)
const loading = ref(false)

const selectedStaff = ref(null)
const staffTreks = ref([])
const showTreksModal = ref(false)

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

        toast.trigger(
            "Staff member created successfully.",
            "success"
        )

    }

    catch(error) {

        console.error(error)

        toast.trigger(
            error.response?.data?.message ||
            "Unable to create staff.",
            "error"
        )

    }

    finally {

        loading.value = false

    }

}

async function toggleStatus(member) {

    try {

        await updateStaffStatus(

            member.id,

            !member.is_active

        )

        await loadStaff()

        const activating = !member.is_active

        await updateStaffStatus(member.id, activating)
        await loadStaff()

        toast.trigger(
            activating
                ? "Staff activated successfully."
                : "Staff deactivated successfully.",
            "success"
        )

    }

    catch (error) {

        console.error(error)

        toast.trigger(

            "Unable to update staff status.",

            "error"

        )

    }

}

async function viewTreks(member) {

    try {

        selectedStaff.value = member

        staffTreks.value = await getStaffTreks(member.id)

        showTreksModal.value = true

    }

    catch (error) {

        console.error(error)

        toast.trigger(

            "Unable to load assigned treks.",

            "error"

        )

    }

}


// for quick actions buttons 

watch(
    () => route.query.add,
    (value) => {

        if (value === "true") {

            showModal.value = true

        }

    },
    { immediate: true }
)

onMounted(loadStaff)

</script>