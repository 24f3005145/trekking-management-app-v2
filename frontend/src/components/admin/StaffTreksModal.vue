<template>
  <div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h5 class="modal-title">
            Assigned Treks
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <!-- Assigned Treks Table -->
          <table class="table table-hover">

            <thead>
              <tr>
                <th>Name</th>
                <th>Location</th>
                <th>Start</th>
                <th>End</th>
                <th>Status</th>
              </tr>
            </thead>

            <tbody>

              <tr
                v-for="trek in treks"
                :key="trek.id"
              >
                <td>{{ trek.name }}</td>
                <td>{{ trek.location }}</td>
                <td>{{ trek.start_date }}</td>
                <td>{{ trek.end_date }}</td>
                <td>{{ trek.status }}</td>
              </tr>

              <!-- Empty State -->
              <tr v-if="treks.length === 0">
                <td
                  colspan="5"
                  class="text-center text-muted"
                >
                  No treks assigned.
                </td>
              </tr>

            </tbody>

          </table>

        </div>

        <!-- Modal Footer -->
        <div class="modal-footer">
          <button
            class="btn btn-secondary"
            @click="$emit('close')"
          >
            Close
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

  treks: {
    type: Array,
    default: () => []
  }
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "close"
])
</script>