<template>
  <div class="container-fluid">

    <!-- Heading -->
    <div class="mb-4">
      <h2 class="fw-bold">
        Admin Dashboard
      </h2>

      <p class="text-muted">
        Welcome back! Here's an overview of your trekking management system.
      </p>
    </div>

    <!-- Statistics -->
    <div class="row g-4 mb-4">

      <div class="col-lg-3 col-md-6">
        <StatCard
          title="Total Treks"
          :value="summary.total_treks"
          icon="🥾"
        />
      </div>

      <div class="col-lg-3 col-md-6">
        <StatCard
          title="Users"
          :value="summary.total_users"
          icon="👤"
        />
      </div>

      <div class="col-lg-3 col-md-6">
        <StatCard
          title="Staff"
          :value="summary.total_staff"
          icon="🧭"
        />
      </div>

      <div class="col-lg-3 col-md-6">
        <StatCard
          title="Bookings"
          :value="summary.total_bookings"
          icon="📋"
        />
      </div>

    </div>

    <!-- Quick Actions -->
    <div class="mb-4">
      <QuickActions />
    </div>

    <!-- Tables -->
    <div class="row g-4">

      <div class="col-lg-6">
        <RecentTreksTable />
      </div>

      <div class="col-lg-6">
        <RecentBookingsTable />
      </div>

    </div>

  </div>
</template>

<script setup>
import StatCard from '@/components/admin/StatCard.vue'
import QuickActions from '@/components/admin/QuickActions.vue'
import RecentTreksTable from '@/components/admin/RecentTreksTable.vue'
import RecentBookingsTable from '@/components/admin/RecentBookingsTable.vue'

import { ref, onMounted } from "vue";
import { getDashboardSummary } from "@/services/adminService";

const summary = ref({
    total_treks: 0,
    total_users: 0,
    total_staff: 0,
    total_bookings: 0
});

onMounted(async () => {
    try {
        summary.value = await getDashboardSummary();
    } catch (error) {
        console.error("Failed to load dashboard summary:", error);
    }
});
</script>