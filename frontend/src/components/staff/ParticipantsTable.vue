<template>
  <div class="card shadow-sm">
    <div class="card-body">

      <!-- Participants Table -->
      <table class="table table-hover">

        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Booking Date</th>
            <th>Booking Status</th>
            <th>Payment</th>
            <th width="250">Actions</th>
          </tr>
        </thead>

        <tbody>

          <tr
            v-for="participant in participants"
            :key="participant.booking_id"
          >
            <td>{{ participant.user_name }}</td>

            <td>{{ participant.email }}</td>

            <td>{{ participant.phone || "-" }}</td>

            <td>{{ participant.booking_date }}</td>

            <td>
              <span class="badge bg-secondary">
                {{ participant.booking_status }}
              </span>
            </td>

            <td>
              <span class="badge bg-primary">
                {{ participant.payment_status }}
              </span>
            </td>

            <td>

              <button
                class="btn btn-sm btn-outline-info me-2"
                @click="$emit('view-participant', participant)"
              >
                👁️
              </button>

              <button
                class="btn btn-sm btn-primary me-2"
                @click="$emit('edit-status', participant)"
              >
                ✏️
              </button>

              <button
                class="btn btn-sm btn-outline-danger"
                @click="$emit('remove-participant', participant)"
              >
                🗑️
              </button>

            </td>
          </tr>

          <!-- Empty State -->
          <tr v-if="participants.length === 0">
            <td
              colspan="7"
              class="text-center"
            >
              No participants found.
            </td>
          </tr>

        </tbody>

      </table>

    </div>
  </div>
</template>

<script setup>
// =========================================================
// Component Props
// =========================================================

defineProps({
  participants: {
    type: Array,
    default: () => []
  }
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "view-participant",
  "edit-status",
  "remove-participant"
])
</script>