<template>
  <div class="card shadow-sm border-0">

    <div class="card-body">

      <div class="d-flex justify-content-between align-items-center mb-3">

        <h4 class="mb-0">
          All Treks
        </h4>

        <small class="text-muted">
          {{ treks.length }} Trek(s)
        </small>

      </div>

      <div class="table-responsive">

        <table class="table table-hover align-middle">

          <thead>

            <tr>
              <th>Name</th>
              <th>Location</th>
              <th>Difficulty</th>
              <th>Duration</th>
              <th>Slots</th>
              <th>Status</th>
              <th>Assigned Staff</th>
              <th class="text-center">Actions</th>
            </tr>

          </thead>

          <tbody>

            <tr
              v-for="trek in treks"
              :key="trek.id"
            >

              <td>{{ trek.name }}</td>

              <td>{{ trek.location }}</td>

              <td>{{ trek.difficulty }}</td>

              <td>{{ trek.duration }}</td>

              <td>{{ trek.slots }}</td>

              <td>

                <span
                  class="badge"
                  :class="badgeClass(trek.status)"
                >

                  {{ trek.status }}

                </span>

              </td>

              <td>

                  {{ trek.assigned_staff_name || "Not Assigned" }}

              </td>

              <td class="text-center">

                <button
                    class="btn btn-sm btn-outline-primary me-2"
                    @click="emit('edit', trek)">
                    Edit
                </button>

                <button
                    class="btn btn-sm btn-outline-secondary me-2"
                    @click="emit('assign', trek)"
                >
                    Assign Staff
                </button>

                <button
                    class="btn btn-sm btn-outline-danger"
                    @click="emit('delete', trek)"
                >
                    Delete
                </button>

              </td>

            </tr>

            <tr v-if="treks.length === 0">

              <td
                colspan="7"
                class="text-center text-muted"
              >
                No treks match the current search or filters.
              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>
</template>

<script setup>

import { badgeClass } from "@/utils/badgeUtils"

defineProps({
    treks: {
        type: Array,
        default: () => []
    }
})

// UPDATED: Table now supports Edit and Delete actions
const emit = defineEmits([
    "edit",
    "delete",
    "assign"
])

</script>