<template>
  <div class="card shadow-sm">

    <div class="card-body">

      <table class="table table-hover">

        <thead>

          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="participant in participants"
            :key="participant.email"
          >
            <td>{{ participant.user_name }}</td>
            <td>{{ participant.email }}</td>
            <td>{{ participant.status }}</td>
          </tr>

          <tr v-if="participants.length === 0">

            <td colspan="3" class="text-center">

              No participants found.

            </td>

          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script setup>

defineProps({

  participants: {

    type: Array,

    default: () => []

  }

})

</script>