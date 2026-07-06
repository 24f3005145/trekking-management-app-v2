<template>
  <div class="card shadow-sm border-0 h-100">
    <div class="card-body text-center">

      <div class="display-6">
        {{ icon }}
      </div>

      <h5 class="mt-3 fw-bold">
        {{ title }}
      </h5>

      <h2 class="text-success fw-bold">
        {{ value }}
      </h2>

    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  value: Number,
  icon: String
})
</script>