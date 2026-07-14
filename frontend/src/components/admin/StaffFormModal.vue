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
            Add Staff
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <div class="mb-3">
            <label class="form-label">
              Name
            </label>

            <input
              v-model="form.name"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">
              Email
            </label>

            <input
              v-model="form.email"
              type="email"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">
              Phone
            </label>

            <input
              v-model="form.phone"
              class="form-control"
            >
          </div>

          <div class="mb-3">
            <label class="form-label">
              Password
            </label>

            <input
              v-model="form.password"
              type="password"
              class="form-control"
            >
          </div>

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
            @click="save"
          >
            {{ loading ? "Creating..." : "Create Staff" }}
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

import { reactive } from "vue"

// =========================================================
// Component Props
// =========================================================

defineProps({
  show: Boolean,
  loading: Boolean
})

// =========================================================
// Component Emits
// =========================================================

const emit = defineEmits([
  "save",
  "close"
])

// =========================================================
// Reactive State
// =========================================================

const form = reactive({
  name: "",
  email: "",
  phone: "",
  password: ""
})

// =========================================================
// Helper Functions
// =========================================================

// Reset the form after a successful save.
function resetForm() {
  form.name = ""
  form.email = ""
  form.phone = ""
  form.password = ""
}

// =========================================================
// Methods
// =========================================================

function save() {
  emit("save", {
    ...form
  })

  resetForm()
}
</script>