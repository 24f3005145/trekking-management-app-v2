<template>
  <div class="card shadow-sm border-0">
    <div class="card-body">

      <!-- Card Header -->
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h4 class="mb-0">
          Recent Treks
        </h4>

        <small class="text-muted">
          {{ treks.length }} Trek(s)
        </small>
      </div>

      <!-- Treks Table -->
      <div class="table-responsive">
        <table class="table table-hover align-middle">

          <thead>
            <tr>
              <th>Name</th>
              <th>Location</th>
              <th>Difficulty</th>
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

              <td>{{ trek.difficulty }}</td>

              <td>
                <span
                  class="badge"
                  :class="badgeClass(trek.status)"
                >
                  {{ trek.status }}
                </span>
              </td>
            </tr>

            <!-- Empty State -->
            <tr v-if="treks.length === 0">
              <td
                colspan="4"
                class="text-center text-muted"
              >
                No treks found.
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
// Imports
// =========================================================

import { onMounted, ref } from "vue"

import { getRecentTreks } from "@/services/adminService"
import { badgeClass } from "@/utils/badgeUtils"

// =========================================================
// Reactive State
// =========================================================

const treks = ref([])

// =========================================================
// Lifecycle Hooks
// =========================================================

onMounted(async () => {
  try {
    treks.value = await getRecentTreks()
  } catch (error) {
    console.error(error)
  }
})
</script>