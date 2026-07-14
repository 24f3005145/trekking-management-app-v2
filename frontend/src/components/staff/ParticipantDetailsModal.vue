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
            Trekker Details
          </h5>

          <button
            class="btn-close"
            @click="$emit('close')"
          ></button>
        </div>

        <!-- Modal Body -->
        <div class="modal-body">

          <!-- Participant Details -->
          <table class="table table-borderless mb-0">
            <tr>
              <th>Name</th>
              <td>{{ participant?.user_name }}</td>
            </tr>

            <tr>
              <th>Email</th>
              <td>{{ participant?.email }}</td>
            </tr>

            <tr>
              <th>Phone</th>
              <td>{{ participant?.phone || "-" }}</td>
            </tr>

            <tr>
              <th>Booking Date</th>
              <td>{{ participant?.booking_date }}</td>
            </tr>

            <tr>
              <th>Booking Status</th>
              <td>{{ participant?.booking_status }}</td>
            </tr>

            <tr>
              <th>Payment Status</th>
              <td>{{ participant?.payment_status }}</td>
            </tr>
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
  participant: Object
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "close"
])
</script>