<template>
  <div class="container-fluid">

    <div class="d-flex justify-content-between align-items-center mb-4">

      <h2 class="mb-0">
        My Assigned Treks
      </h2>

    </div>

    <div
      v-if="loading"
      class="text-center"
    >
      Loading...
    </div>

    <AssignedTreksTable
      v-else
      :treks="treks"
      @view="viewTrek"
    />

  </div>
</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import AssignedTreksTable from "@/components/staff/AssignedTreksTable.vue"
import staffService from "@/services/staffService"

const treks = ref([])
const loading = ref(true)

const router = useRouter()

async function loadTreks() {

  try {

    treks.value = await staffService.getAssignedTreks()

  }

  catch (error) {

    console.error(error)

  }

  finally {

    loading.value = false

  }

}

function viewTrek(trek) {

  router.push(`/dashboard/staff/treks/${trek.id}`)

}

onMounted(loadTreks)

</script>