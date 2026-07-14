<template>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2>Participants</h2>

        <RouterLink
            :to="`/dashboard/staff/treks/${route.params.id}`"
            class="btn btn-secondary"
        >
            Back
        </RouterLink>

    </div>

    <div
        v-if="loading"
        class="text-center"
    >

        Loading...

    </div>

    <ParticipantsTable

        v-else

        :participants="participants"

        @view-participant="openViewModal"

        @edit-status="openStatusModal"

        @remove-participant="openRemoveModal"

    />

    <BookingStatusModal

        :show="showStatusModal"

        :loading="saving"

        :participant="selectedParticipant"

        @close="showStatusModal = false"

        @save="saveStatus"

    />

    <ParticipantDetailsModal

        :show="showViewModal"

        :participant="selectedParticipant"

        @close="showViewModal = false"

    />

    <DeleteConfirmationModal

        :show="showRemoveModal"

        :loading="removing"

        title="Remove Participant"

        :message="`Are you sure you want to remove ${selectedParticipant?.user_name} from this trek?`"

        confirm-text="Remove Participant"

        @close="showRemoveModal = false"

        @confirm="confirmRemove"

    />

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRoute, RouterLink } from "vue-router"

import staffService from "@/services/staffService"
import ParticipantsTable from "@/components/staff/ParticipantsTable.vue"

import { useToastStore } from "@/stores/toast"

import BookingStatusModal from "@/components/staff/BookingStatusModal.vue"
import DeleteConfirmationModal from "@/components/admin/DeleteConfirmationModal.vue"
import ParticipantDetailsModal from "@/components/staff/ParticipantDetailsModal.vue"

const route = useRoute()

const loading = ref(true)

const participants = ref([])
const selectedParticipant = ref(null)

const showStatusModal = ref(false)
const showRemoveModal = ref(false)
const showViewModal = ref(false)

const saving = ref(false)

const removing = ref(false)

const toast = useToastStore()

async function loadParticipants() {

    try {

        participants.value =
            await staffService.getParticipants(route.params.id)

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

function openStatusModal(participant) {

    selectedParticipant.value = participant

    showStatusModal.value = true

}

function openRemoveModal(participant) {

    selectedParticipant.value = participant

    showRemoveModal.value = true

}

async function saveStatus(status) {

    saving.value = true

    try {

        await staffService.updateBookingStatus(

            selectedParticipant.value.booking_id,

            status

        )

        toast.trigger(
            "Booking status updated.",
            "success"
        )

        showStatusModal.value = false

        await loadParticipants()

    }

    catch {

        toast.trigger(
            "Unable to update booking status.",
            "danger"
        )

    }

    finally {

        saving.value = false

    }

}

async function confirmRemove() {

    removing.value = true

    try {

        await staffService.removeParticipant(

            selectedParticipant.value.booking_id

        )

        toast.trigger(
            "Participant removed.",
            "success"
        )

        showRemoveModal.value = false

        await loadParticipants()

    }

    catch {

        toast.trigger(
            "Unable to remove participant.",
            "danger"
        )

    }

    finally {

        removing.value = false

    }

}

function openViewModal(participant) {

    selectedParticipant.value = participant

    showViewModal.value = true

}

onMounted(loadParticipants)

</script>