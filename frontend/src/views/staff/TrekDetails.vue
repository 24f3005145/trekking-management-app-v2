<template>
  <div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

      <h2>Trek Details</h2>

      <RouterLink
        to="/dashboard/staff/treks"
        class="btn btn-secondary"
      >
        Back
      </RouterLink>

    </div>

    <div
      v-if="loading"
      class="text-center"
    >
      Loading...
    </div>

    <div
      v-else
      class="card shadow-sm"
    >

      <div class="card-body">

        <table class="table">

          <tbody>

            <tr>
              <th width="220">Name</th>
              <td>{{ trek.name }}</td>
            </tr>

            <tr>
              <th>Location</th>
              <td>{{ trek.location }}</td>
            </tr>

            <tr>
              <th>Difficulty</th>
              <td>{{ trek.difficulty }}</td>
            </tr>

            <tr>
              <th>Duration</th>
              <td>{{ trek.duration }} Days</td>
            </tr>

            <tr>
              <th>Start Date</th>
              <td>{{ trek.start_date }}</td>
            </tr>

            <tr>
              <th>End Date</th>
              <td>{{ trek.end_date }}</td>
            </tr>

            <tr>
              <th>Status</th>
              <td>{{ trek.status }}</td>
            </tr>

            <tr>
              <th>Available Slots</th>
              <td>{{ trek.available_slots }}</td>
            </tr>

          </tbody>

        </table>

        <div class="d-flex gap-2 mt-4 flex-wrap">

          <RouterLink
            :to="`/dashboard/staff/treks/${route.params.id}/participants`"
            class="btn btn-primary"
          >
            View Participants
          </RouterLink>

          <button
            class="btn btn-warning"
            @click="showStatusModal = true"
          >
            Update Status
          </button>

          <button
            class="btn btn-success"
            @click="showSlotsModal = true"
          >
            Update Slots
          </button>

        </div>

      </div>

    </div>

    <UpdateStatusModal
      :show="showStatusModal"
      :loading="statusLoading"
      :currentStatus="trek.status"
      @close="showStatusModal = false"
      @save="updateStatus"
    />

    <UpdateSlotsModal
      :show="showSlotsModal"
      :loading="slotsLoading"
      :currentSlots="trek.available_slots"
      @close="showSlotsModal = false"
      @save="updateSlots"
    />

  </div>
</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRoute, RouterLink } from "vue-router"

import staffService from "@/services/staffService"

import UpdateStatusModal from "@/components/staff/UpdateStatusModal.vue"
import UpdateSlotsModal from "@/components/staff/UpdateSlotsModal.vue"

const route = useRoute()

const trek = ref({})
const loading = ref(true)

const showStatusModal = ref(false)
const showSlotsModal = ref(false)

const statusLoading = ref(false)
const slotsLoading = ref(false)

async function loadTrek() {

  try {

    trek.value = await staffService.getTrekDetails(route.params.id)

  }

  catch (error) {

    console.error(error)

  }

  finally {

    loading.value = false

  }

}

async function updateStatus(status) {

  try {

    statusLoading.value = true

    await staffService.updateStatus(route.params.id, {
      status
    })

    showStatusModal.value = false

    await loadTrek()

  }

  catch (error) {

    console.error(error)

  }

  finally {

    statusLoading.value = false

  }

}

async function updateSlots(slots) {

  try {

    slotsLoading.value = true

    await staffService.updateSlots(route.params.id, {
      available_slots: slots
    })

    showSlotsModal.value = false

    await loadTrek()

  }

  catch (error) {

    console.error(error)

  }

  finally {

    slotsLoading.value = false

  }

}

onMounted(loadTrek)

</script>