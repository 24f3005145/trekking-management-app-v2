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
            {{ title }}
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">
          <p class="mb-0">
            {{ message }}
          </p>

          <small class="text-danger">
            This action cannot be undone.
          </small>
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
            class="btn btn-danger"
            :disabled="loading"
            @click="$emit('confirm')"
          >
            {{ loading ? "Please wait..." : confirmText }}
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
// =========================================================
// Component Props
// =========================================================

defineProps({
  show: Boolean,

  loading: Boolean,

  title: {
    type: String,
    default: "Confirm Action"
  },

  message: {
    type: String,
    default: ""
  },

  confirmText: {
    type: String,
    default: "Confirm"
  }
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "close",
  "confirm"
])
</script>