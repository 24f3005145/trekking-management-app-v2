<template>
  <div class="container mt-4">

    <h2 class="mb-4">
      Staff Dashboard
    </h2>

    <div v-if="loading" class="text-center">
      Loading...
    </div>

    <div v-else>

      <h4 class="mb-4">
        Welcome, {{ dashboard.staff }}
      </h4>

      <div class="row">

        <div class="col-md-3 mb-3">
            <StatCard
            title="Assigned Treks"
            :value="dashboard.assigned_treks"
            icon="🥾"
            />
        </div>

        <div class="col-md-3 mb-3">
            <StatCard
            title="Upcoming"
            :value="dashboard.upcoming"
            icon="📅"
            />
        </div>

        <div class="col-md-3 mb-3">
            <StatCard
            title="Completed"
            :value="dashboard.completed"
            icon="✅"
            />
        </div>

        <div class="col-md-3 mb-3">
            <StatCard
            title="Pending"
            :value="dashboard.pending"
            icon="⏳"
            />
        </div>

        </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import staffService from "@/services/staffService";
import StatCard from "@/components/admin/StatCard.vue";

const loading = ref(true);

const dashboard = ref({
  staff: "",
  assigned_treks: 0,
  upcoming: 0,
  completed: 0,
  pending: 0,
});

const loadDashboard = async () => {
  try {
    const response = await staffService.getDashboard();
    dashboard.value = response.data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

onMounted(loadDashboard);
</script>