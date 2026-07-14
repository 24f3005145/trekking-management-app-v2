<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">

      <!-- Card Header -->
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h4 class="mb-0">
          Recent Bookings
        </h4>

        <small class="text-muted">
          {{ bookings.length }} Booking(s)
        </small>
      </div>

      <!-- Bookings Table -->
      <div class="table-responsive">
        <table class="table table-hover align-middle">

          <thead>
            <tr>
              <th>User</th>
              <th>Trek</th>
              <th>Status</th>
              <th>Date</th>
            </tr>
          </thead>

          <tbody>

            <tr
              v-for="booking in bookings"
              :key="booking.id"
            >
              <td>{{ booking.user }}</td>

              <td>{{ booking.trek }}</td>

              <td>
                <span
                  class="badge"
                  :class="badgeClass(booking.status)"
                >
                  {{ booking.status }}
                </span>
              </td>

              <td>{{ booking.booking_date }}</td>
            </tr>

            <!-- Empty State -->
            <tr v-if="bookings.length === 0">
              <td
                colspan="4"
                class="text-center text-muted"
              >
                No bookings found.
              </td>
            </tr>

          </tbody>

        </table>
      </div>

    </div>
  </div>
</template>

<script setup>
// =========================================================
// Imports
// =========================================================

import { onMounted, ref } from "vue"

import { getRecentBookings } from "@/services/adminService"

// =========================================================
// Reactive State
// =========================================================

const bookings = ref([])

// =========================================================
// Helper Functions
// =========================================================

function badgeClass(status) {
  switch (status) {
    case "Booked":
      return "bg-primary"

    case "Cancelled":
      return "bg-danger"

    case "Completed":
      return "bg-success"

    default:
      return "bg-secondary"
  }
}

// =========================================================
// Lifecycle Hooks
// =========================================================

onMounted(async () => {
  try {
    bookings.value = await getRecentBookings()
  } catch (error) {
    console.error("Failed to load bookings:", error)
  }
})
</script>