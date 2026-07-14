<template>
  <div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h5 class="modal-title">
            Update Booking Status
          </h5>

          <button
            class="btn-close"
            :disabled="loading"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <p>
            Trekker:
            <strong>
              {{ participant?.user_name }}
            </strong>
          </p>

          <label class="form-label">
            Booking Status
          </label>

          <select
            v-model="selectedStatus"
            class="form-select"
            :disabled="loading"
          >
            <option>Booked</option>
            <option>Checked In</option>
            <option>Completed</option>
            <option>Cancelled</option>
          </select>

        </div>

        <!-- Modal Footer -->
        <div class="modal-footer">
          <button
            class="btn btn-secondary"
            :disabled="loading"
            @click="$emit('close')"
          >
            Cancel
          </button>

          <button
            class="btn btn-primary"
            :disabled="loading"
            @click="save"
          >
            <span
              v-if="loading"
              class="spinner-border spinner-border-sm me-2"
            ></span>

            {{ loading ? "Saving..." : "Save Changes" }}
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
// =========================================================
// Imports
// =========================================================

import { ref, watch } from "vue"

// =========================================================
// Component Props
// =========================================================

const props = defineProps({
  show: Boolean,
  loading: Boolean,
  participant: Object
})

// =========================================================
// Component Emits
// =========================================================

const emit = defineEmits([
  "close",
  "save"
])

// =========================================================
// Reactive State
// =========================================================

const selectedStatus = ref("Booked")

// =========================================================
// Watchers
// =========================================================

// Pre-select the participant's current booking status.
watch(
  () => props.participant,
  (participant) => {
    if (participant) {
      selectedStatus.value = participant.booking_status
    }
  },
  {
    immediate: true
  }
)

// =========================================================
// Methods
// =========================================================

function save() {
  emit(
    "save",
    selectedStatus.value
  )
}
</script>