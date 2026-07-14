<template>
  <div
    v-if="toast.show"
    class="app-toast shadow-lg"
    :class="toastClass"
  >
    <div class="d-flex">

      <!-- Toast Icon -->
      <div class="me-3 fs-4">
        {{ icon }}
      </div>

      <!-- Toast Content -->
      <div class="flex-grow-1">

        <div class="fw-bold mb-1">
          {{ title }}
        </div>

        <div>
          {{ toast.message }}
        </div>

      </div>

      <!-- Close Button -->
      <button
        class="btn-close btn-close-white ms-3"
        @click="toast.show = false"
      ></button>

    </div>
  </div>
</template>

<script setup>
// =========================================================
// Imports
// =========================================================

import { computed } from "vue"

import { useToastStore } from "@/stores/toast"

// =========================================================
// Store
// =========================================================

const toast = useToastStore()

// =========================================================
// Computed Properties
// =========================================================

// Toast background color.
const toastClass = computed(() => {
  switch (toast.type) {
    case "success":
      return "bg-success text-white"

    case "error":
      return "bg-danger text-white"

    case "warning":
      return "bg-warning text-dark"

    case "info":
      return "bg-primary text-white"

    default:
      return "bg-success text-white"
  }
})

// Toast title.
const title = computed(() => {
  switch (toast.type) {
    case "success":
      return "Success"

    case "error":
      return "Error"

    case "warning":
      return "Warning"

    case "info":
      return "Information"

    default:
      return "Notification"
  }
})

// Toast icon.
const icon = computed(() => {
  switch (toast.type) {
    case "success":
      return "✅"

    case "error":
      return "❌"

    case "warning":
      return "⚠️"

    case "info":
      return "ℹ️"

    default:
      return "🔔"
  }
})
</script>

<style scoped>
.app-toast {
  position: fixed;
  top: 24px;
  right: 24px;
  min-width: 340px;
  max-width: 420px;
  padding: 16px 18px;
  border-radius: 14px;
  z-index: 9999;
  animation: slideIn 0.35s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(40px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>