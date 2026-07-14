<template>
    <!-- =====================================================
         Trek Card Component
         Displays a single trek in the Featured Treks section.
    ====================================================== -->

    <div class="card h-100 shadow-sm">

        <!-- Trek Image -->
        <img
            src="@/assets/images/hero-banner.jpg"
            class="card-img-top trek-image"
            alt="Trek Image"
        >

        <div class="card-body d-flex flex-column">

            <!-- Trek Name -->
            <h5 class="card-title fw-bold">
                {{ trek.name }}
            </h5>

            <!-- Trek Location -->
            <p class="text-muted mb-2">
                <i class="bi bi-geo-alt-fill"></i>
                {{ trek.location }}
            </p>

            <!-- Trek Details -->
            <div class="mb-3">

                <span class="badge bg-success me-2">
                    {{ trek.difficulty }}
                </span>

                <span class="badge bg-primary">
                    {{ trek.duration }} Days
                </span>

            </div>

            <p class="mb-3">
                <strong>Available Slots:</strong>
                {{ trek.available_slots }}
            </p>

            <!-- Push button to bottom -->
            <div class="mt-auto">

                <button
                    class="btn btn-success w-100"
                    @click="$emit('view-details', trek.id)"
                >
                    View Details
                </button>

            </div>

        </div>

    </div>
</template>

<script setup>

// =====================================================
// Trek Card Props
// =====================================================

defineProps({

    trek: {
        type: Object,
        required: true
    }

})

// =====================================================
// Component Events
// =====================================================

defineEmits([
    "view-details"
])

</script>

<style scoped>

.trek-image{

    height:220px;
    object-fit:cover;

}

.card{

    transition:all .3s ease;

}

.card:hover{

    transform:translateY(-6px);

}

</style>