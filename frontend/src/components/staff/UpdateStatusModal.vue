<template>
  <div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
  >
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title">
            Update Trek Status
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <div class="modal-body">

          <label class="form-label">Status</label>

          <select
            v-model="status"
            class="form-select"
          >
            <option>Pending</option>
            <option>Upcoming</option>
            <option>Completed</option>
          </select>

        </div>

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
import { ref, watch } from "vue"

const props = defineProps({
  show: Boolean,
  loading: Boolean,
  currentStatus: String
})

defineEmits(["save", "close"])

const status = ref("Pending")

watch(
  () => props.currentStatus,
  (value) => {
    status.value = value || "Pending"
  },
  { immediate: true }
)
</script>