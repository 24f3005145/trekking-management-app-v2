<template>
    <div class="container-fluid">

        <div class="d-flex justify-content-between align-items-center mb-4">

            <h2 class="mb-0">
                Manage Treks
            </h2>

            

            <button
                class="btn btn-success"
                @click="isEdit = false; selectedTrek = null; showModal = true;"
            >
                + Add Trek
            </button>

        </div>

        <div
            v-if="alert.show"
            class="alert mt-3"
            :class="`alert-${alert.type}`"
        >

            {{ alert.message }}

        </div>

        <TrekFilters
            v-model:search="search"
            v-model:difficulty="difficulty"
            v-model:status="status"
        />

        <TrekTable
            :treks="filteredTreks"
            @edit="openEditModal"
            @delete="handleDeleteTrek"
            @assign="openAssignModal"
        />

        <TrekFormModal
            :show="showModal"
            :isEdit="isEdit"
            :loading="loading"
            :trek="selectedTrek"
            @close="closeModal"
            @save="saveTrek"
        />

        <!-- NEW -->
        <AssignStaffModal

            :show="showAssignModal"

            :staff="staff"

            :assignedStaffId="selectedTrek?.assigned_staff_id"

            @close="showAssignModal = false"

            @save="handleAssignStaff"

        />

        <!-- NEW -->
        <DeleteConfirmationModal

            :show="showDeleteModal"

            :loading="deleteLoading"

            :trekName="selectedTrek?.name"

            @close="showDeleteModal = false"

            @confirm="confirmDeleteTrek"

        />

    </div>
</template>

<script setup>

// =====================================================
// Treks.vue
// Admin page for managing treks.
// Supports CRUD operations, filtering and staff assignment.
// =====================================================

import { ref, onMounted, computed } from "vue"

// =====================================================
// Components
// =====================================================

import TrekTable from "@/components/admin/TrekTable.vue"
import TrekFilters from "@/components/admin/TrekFilters.vue"
import TrekFormModal from "@/components/admin/TrekFormModal.vue"
import AssignStaffModal from "@/components/admin/AssignStaffModal.vue"
import DeleteConfirmationModal from "@/components/admin/DeleteConfirmationModal.vue"

// =====================================================
// Services
// =====================================================

import {
    getTreks,
    createTrek,
    updateTrek,
    deleteTrek,
    getStaff,
    assignStaff
} from "@/services/adminService"

// =====================================================
// Data
// =====================================================

const treks = ref([])
const staff = ref([])

// =====================================================
// Filters
// =====================================================

const search = ref("")
const difficulty = ref("")
const status = ref("")

// =====================================================
// Selected Objects
// =====================================================

const selectedTrek = ref(null)

// =====================================================
// Modal State
// =====================================================

const showModal = ref(false)
const showAssignModal = ref(false)
const showDeleteModal = ref(false)

const isEdit = ref(false)

// =====================================================
// Loading State
// =====================================================

const loading = ref(false)
const deleteLoading = ref(false)

// =====================================================
// Alert State
// =====================================================

const alert = ref({
    show: false,
    type: "",
    message: ""
})

// =====================================================
// Data Loaders
// =====================================================

async function loadTreks() {

    try {

        treks.value = await getTreks()
        staff.value = await getStaff()

    }

    catch (error) {

        console.error(error)

    }

}

// =====================================================
// Utility Functions
// =====================================================

function showAlert(type, message) {

    alert.value = {
        show: true,
        type,
        message
    }

    setTimeout(() => {

        alert.value.show = false

    }, 3000)

}

// =====================================================
// Modal Handlers
// =====================================================

function openEditModal(trek) {

    selectedTrek.value = trek

    isEdit.value = true

    showModal.value = true

}

function closeModal() {

    showModal.value = false

    isEdit.value = false

    selectedTrek.value = null

}

function openAssignModal(trek) {

    selectedTrek.value = trek

    showAssignModal.value = true

}

function handleDeleteTrek(trek) {

    selectedTrek.value = trek

    showDeleteModal.value = true

}

// =====================================================
// Trek CRUD
// =====================================================

async function saveTrek(data) {

    try {

        loading.value = true

        if (isEdit.value) {

            await updateTrek(
                selectedTrek.value.id,
                data
            )

        }

        else {

            await createTrek(data)

        }

        closeModal()

        await loadTreks()

        showAlert(
            "success",
            isEdit.value
                ? "Trek updated successfully."
                : "Trek created successfully."
        )

    }

    catch (error) {

        console.error(error)

        showAlert(
            "danger",
            "Something went wrong."
        )

    }

    finally {

        loading.value = false

    }

}

async function confirmDeleteTrek() {

    try {

        deleteLoading.value = true

        await deleteTrek(selectedTrek.value.id)

        showDeleteModal.value = false

        await loadTreks()

        showAlert(
            "success",
            "Trek deleted successfully."
        )

    }

    catch (error) {

        console.error(error)

        showAlert(
            "danger",
            "Failed to delete trek."
        )

    }

    finally {

        deleteLoading.value = false

        selectedTrek.value = null

    }

}

// =====================================================
// Staff Assignment
// =====================================================

async function handleAssignStaff(staffId) {

    try {

        await assignStaff(
            selectedTrek.value.id,
            staffId
        )

        showAssignModal.value = false

        await loadTreks()

    }

    catch (error) {

        console.error(error)

    }

}

// =====================================================
// Computed Properties
// =====================================================

const filteredTreks = computed(() => {

    return treks.value.filter(trek => {

        const matchesSearch =
            trek.name.toLowerCase().includes(search.value.toLowerCase()) ||
            trek.location.toLowerCase().includes(search.value.toLowerCase())

        const matchesDifficulty =
            !difficulty.value ||
            trek.difficulty === difficulty.value

        const matchesStatus =
            !status.value ||
            trek.status === status.value

        return (
            matchesSearch &&
            matchesDifficulty &&
            matchesStatus
        )

    })

})

// =====================================================
// Lifecycle Hooks
// =====================================================

onMounted(loadTreks)

</script>