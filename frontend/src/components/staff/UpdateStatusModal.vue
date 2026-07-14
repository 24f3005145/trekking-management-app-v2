<template>
  <div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
  >
    <div class="modal-dialog">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h5 class="modal-title">
            Update Trek Status
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <label class="form-label">
            Status
          </label>

          <select
            v-model="status"
            class="form-select"
          >
            <option>Pending</option>
            <option>Open</option>
            <option>Upcoming</option>
            <option>Completed</option>
          </select>

        </div>

        <!-- Modal Footer -->
        <div class="modal-footer">

          <button
            class="btn btn-secondary"
            @click="$emit('close')"
          >
            Cancel
          </button>

          <button
            class="btn btn-success"
            :disabled="loading"
            @click="$emit('save', status)"
          >
            {{ loading ? "Updating..." : "Update" }}
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
  currentStatus: String
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "save",
  "close"
])

// =========================================================
// Reactive State
// =========================================================

const status = ref("Pending")

// =========================================================
// Watchers
// =========================================================

// Initialize the selected status with the current trek status.
watch(
  () => props.currentStatus,
  (value) => {
    status.value = value || "Pending"
  },
  {
    immediate: true
  }
)
</script>

