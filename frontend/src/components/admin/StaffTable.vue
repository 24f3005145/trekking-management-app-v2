<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">

      <!-- Card Header -->
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h4 class="mb-0">
          All Staff
        </h4>

        <small class="text-muted">
          {{ staff.length }} Staff Member(s)
        </small>
      </div>

      <!-- Staff Table -->
      <div class="table-responsive">
        <table class="table table-hover align-middle">

          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Status</th>
              <th width="220">Actions</th>
            </tr>
          </thead>

          <tbody>

            <tr
              v-for="member in staff"
              :key="member.id"
            >
              <td>{{ member.name }}</td>

              <td>{{ member.email }}</td>

              <td>{{ member.phone }}</td>

              <td>
                <span
                  class="badge"
                  :class="
                    member.is_active
                      ? 'bg-success'
                      : 'bg-danger'
                  "
                >
                  {{ member.is_active ? "Active" : "Inactive" }}
                </span>
              </td>

              <td>

                <button
                  class="btn btn-sm btn-outline-primary me-2"
                  @click="$emit('view-treks', member)"
                >
                  View Treks
                </button>

                <button
                  class="btn btn-sm"
                  :class="
                    member.is_active
                      ? 'btn-outline-danger'
                      : 'btn-outline-success'
                  "
                  @click="$emit('toggle-status', member)"
                >
                  {{ member.is_active ? "Deactivate" : "Activate" }}
                </button>

              </td>
            </tr>

            <!-- Empty State -->
            <tr v-if="staff.length === 0">
              <td
                colspan="5"
                class="text-center text-muted"
              >
                No staff found.
              </td>
            </tr>

          </tbody>

        </table>
      </div>

    </div>
  </div>
</template>

<script setup>
// =========================================================
// Component Props
// =========================================================

defineProps({
  staff: {
    type: Array,
    default: () => []
  }
})

// =========================================================
// Component Emits
// =========================================================

defineEmits([
  "toggle-status",
  "view-treks"
])
</script>