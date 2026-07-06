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
    />

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRoute, RouterLink } from "vue-router"

import staffService from "@/services/staffService"
import ParticipantsTable from "@/components/staff/ParticipantsTable.vue"

const route = useRoute()

const loading = ref(true)

const participants = ref([])

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

onMounted(loadParticipants)

</script>