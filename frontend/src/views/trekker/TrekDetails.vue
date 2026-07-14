<template>

<div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2>Trek Details</h2>

        <RouterLink
            to="/dashboard/trekker"
            class="btn btn-secondary">

            Back

        </RouterLink>

    </div>

    <div
        v-if="loading"
        class="text-center">

        Loading...

    </div>

    <div
        v-else
        class="card">

        <img
            src="@/assets/images/hero-banner.jpg"
            class="trek-banner"
        >

        <div class="card-body">

            <h3 class="fw-bold mb-3">

                {{ trek.name }}

            </h3>

            <!-- Trek Description -->

            <p class="text-muted">

                {{ trek.description }}

            </p>

            <table class="table">

                <tbody>

                    <tr>
                        <th width="220">Location</th>
                        <td>{{ trek.location }}</td>
                    </tr>

                    <tr>
                        <th>Difficulty</th>
                        <td>{{ trek.difficulty }}</td>
                    </tr>

                    <tr>
                        <th>Duration</th>
                        <td>{{ trek.duration }} Days</td>
                    </tr>

                    <tr>
                        <th>Start Date</th>
                        <td>{{ trek.start_date }}</td>
                    </tr>

                    <tr>
                        <th>End Date</th>
                        <td>{{ trek.end_date }}</td>
                    </tr>

                    <tr>
                        <th>Available Slots</th>
                        <td>{{ trek.available_slots }}</td>
                    </tr>

                    <tr>
                        <th>Guide</th>
                        <td>{{ trek.assigned_staff || "Not Assigned" }}</td>
                    </tr>

                </tbody>

            </table>

            <!-- Book Trek -->

            <button
                class="btn btn-success btn-lg"
                @click="bookTrek">

                Book This Trek

            </button>

        </div>

    </div>

</div>

</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRoute, RouterLink } from "vue-router"

import trekkerService from "@/services/trekkerService"

import { useToastStore } from "@/stores/toast"                 // Toast

const route = useRoute()

const trek = ref({})

const loading = ref(true)

const toast = useToastStore()                   // Toast

// ---------------------------------------------------------
// Load trek details.
// ---------------------------------------------------------

async function loadTrek() {

    try {

        trek.value = await trekkerService.getTrekDetails(route.params.id)

    }

    finally {

        loading.value = false

    }

}

// ---------------------------------------------------------
// Book trek.
// ---------------------------------------------------------

async function bookTrek() {

    try {

        await trekkerService.bookTrek(route.params.id)

        toast.trigger(
            "Trek booked successfully.",
            "success"
        )

        await loadTrek()

    }

    catch (error) {

        toast.trigger(
            error.response?.data?.message ||
            "Unable to book trek.",
            "error"
        )

    }

}

onMounted(loadTrek)

</script>

<style scoped>

.trek-banner{

    width:100%;
    height:350px;
    object-fit:cover;

}

</style>