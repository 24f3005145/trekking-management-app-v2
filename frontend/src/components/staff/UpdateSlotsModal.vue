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
            Update Available Slots
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <label class="form-label">
            Available Slots
          </label>

          <input
            v-model.number="slots"
            type="number"
            min="0"
            class="form-control"
          >

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
            @click="$emit('save', slots)"
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
  currentSlots: Number
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

const slots = ref(0)

// =========================================================
// Watchers
// =========================================================

// Initialize the input with the current number of available slots.
watch(
  () => props.currentSlots,
  (value) => {
    slots.value = value ?? 0
  },
  {
    immediate: true
  }
)
</script>
