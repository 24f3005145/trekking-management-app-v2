<template>
  <div class="card shadow-sm">

    <div class="card-body">

      <table class="table table-hover align-middle">

        <thead>

          <tr>
            <th>Name</th>
            <th>Location</th>
            <th>Status</th>
            <th>Available Slots</th>
            <th width="120">Action</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="trek in treks"
            :key="trek.id"
          >

            <td>{{ trek.name }}</td>

            <td>{{ trek.location }}</td>

            <td>{{ trek.status }}</td>

            <td>{{ trek.available_slots }}</td>

            <td>

              <button
                class="btn btn-primary btn-sm"
                @click="$emit('view', trek)"
              >
                View
              </button>

            </td>

          </tr>

          <tr v-if="treks.length === 0">

            <td colspan="5" class="text-center">
              No assigned treks found.
            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script setup>
defineProps({
  treks: {
    type: Array,
    default: () => []
  }
})

defineEmits(["view"])
</script>