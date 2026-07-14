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

import { ref, onMounted, computed, watch } from "vue"

import { useRoute } from "vue-router"
const route = useRoute()

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

import { useToastStore } from "@/stores/toast"              // Toast

// =====================================================
// Data
// =====================================================

const treks = ref([])
const staff = ref([])

const toast = useToastStore()                     // Toast

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

        toast.trigger(

            isEdit.value
                ? "Trek updated successfully."
                : "Trek created successfully.",

            "success"

        )

    }

    catch (error) {

        console.error(error)

        toast.trigger(

            "Something went wrong.",

            "error"

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

        toast.trigger(

            "Trek deleted successfully.",

            "success"

        )

    }

    catch (error) {

        console.error(error)

        toast.trigger(

            "Failed to delete trek.",

            "error"

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

        toast.trigger(

            "Staff assigned successfully.",

            "success"

        )

    }

    catch (error) {

        console.error(error)

        toast.trigger(

            "Unable to assign staff.",

            "error"

        )

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

// for quick actions buttons 
watch(
    () => route.query.add,
    (value) => {

        if (value === "true") {

            isEdit.value = false

            selectedTrek.value = null

            showModal.value = true

        }

    },
    { immediate: true }
)

onMounted(loadTreks)

</script>