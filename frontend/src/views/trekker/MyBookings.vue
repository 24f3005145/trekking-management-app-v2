<template>

<div class="container-fluid">

    <!-- =====================================================
         Page Header
    ====================================================== -->

    <div class="d-flex justify-content-between align-items-center mb-4">

        <h2 class="fw-bold">

            My Bookings

        </h2>

        <div>

            <button
                class="btn btn-success"
                :disabled="exporting"
                @click="exportHistory">

                <span
                    v-if="exporting"
                    class="spinner-border spinner-border-sm me-2">
                </span>

                Export CSV

            </button>

        </div>

    </div>

    <!-- =====================================================
         Loading
    ====================================================== -->

    <div
        v-if="loading"
        class="text-center py-5">

        <div class="spinner-border text-success"></div>

    </div>

    <!-- =====================================================
         Empty State
    ====================================================== -->

    <div
        v-else-if="bookings.length === 0"
        class="card p-5 text-center">

        <h4>

            No Bookings Yet

        </h4>

        <p class="text-muted">

            Explore our adventures and book your first trek.

        </p>

        <RouterLink
            to="/dashboard/trekker"
            class="btn btn-success mt-3">

            Explore Treks

        </RouterLink>

    </div>

    <!-- =====================================================
         Booking History
    ====================================================== -->

    <div
        v-if="downloadUrl"
        class="alert alert-success d-flex justify-content-between align-items-center">

        <span>

            Your booking history is ready.

        </span>

        <a
            :href="downloadUrl"
            class="btn btn-success"
            download>

            Download CSV

        </a>

    </div>

    <div
        v-else
        class="card">

        <div class="card-body">

            <table class="table align-middle">

                <thead>

                    <tr>

                        <th>Trek</th>
                        <th>Location</th>
                        <th>Duration</th>
                        <th>Status</th>
                        <th>Payment</th>
                        <th>Booked On</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="booking in bookings"
                        :key="booking.booking_id">

                        <td>

                            {{ booking.trek_name }}

                        </td>

                        <td>

                            {{ booking.location }}

                        </td>

                        <td>

                            {{ booking.duration }} Days

                        </td>

                        <td>

                            <span
                                class="badge"
                                :class="statusBadge(booking.status)">

                                {{ booking.status }}

                            </span>

                        </td>

                        <td>

                            <span
                                class="badge"
                                :class="paymentBadge(booking.payment_status)">

                                {{ booking.payment_status }}

                            </span>

                        </td>

                        <td>

                            {{ formatDate(booking.booking_date) }}

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </div>

</div>

</template>

<script setup>

// =====================================================
// Imports
// =====================================================

import { ref, onMounted, onUnmounted } from "vue"
import { RouterLink } from "vue-router"

import trekkerService from "@/services/trekkerService"

// =====================================================
// State
// =====================================================

const bookings = ref([])

const loading = ref(true)

// =====================================================
// Export State
// =====================================================

const exporting = ref(false)

const downloadUrl = ref(null)

let pollTimer = null

// =====================================================
// Load User Bookings
// =====================================================

async function loadBookings() {

    try {

        bookings.value = await trekkerService.getBookings()

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

// =====================================================
// Export Booking History
// =====================================================

async function exportHistory() {

    exporting.value = true

    downloadUrl.value = null

    try {

        const response = await trekkerService.exportBookings()

        pollStatus(response.job_id)

    }

    catch (error) {

        exporting.value = false

        console.error(error)

    }

}

// =====================================================
// Poll Export Status
// =====================================================

function pollStatus(jobId) {

    pollTimer = setInterval(async () => {

        const result =
            await trekkerService.getExportStatus(jobId)

        if (result.status === "Completed") {

            clearInterval(pollTimer)

            exporting.value = false

            downloadUrl.value = result.download_url

        }

        if (result.status === "Failed") {

            clearInterval(pollTimer)

            exporting.value = false

        }

    }, 2000)

}

// =====================================================
// Status Badge
// =====================================================

function statusBadge(status) {

    switch (status) {

        case "Booked":

            return "bg-success"

        case "Completed":

            return "bg-primary"

        case "Cancelled":

            return "bg-danger"

        default:

            return "bg-secondary"

    }

}

// =====================================================
// Payment Badge
// =====================================================

function paymentBadge(status) {

    switch (status) {

        case "Paid":

            return "bg-success"

        case "Pending":

            return "bg-warning text-dark"

        default:

            return "bg-secondary"

    }

}

// =====================================================
// Date Formatting
// =====================================================

function formatDate(date) {

    return new Date(date).toLocaleDateString()

}

onMounted(loadBookings)

onUnmounted(() => {

    if (pollTimer) {

        clearInterval(pollTimer)

    }

})

</script>