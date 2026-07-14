<template>

    <!-- =====================================================
         Featured Treks Section
    ====================================================== -->

    <section>

        <div class="d-flex justify-content-between align-items-center mb-4">

            <h2 class="fw-bold">
                Featured Treks
            </h2>

        </div>

        <!-- -------------------------------------------------
             Search Filters
        -------------------------------------------------- -->

        <SearchFilters
            @search="loadTreks"
        />

        <!-- -------------------------------------------------
             Loading State
        -------------------------------------------------- -->

        <div
            v-if="loading"
            class="text-center py-5">

            <div class="spinner-border text-success"></div>

        </div>

        <!-- -------------------------------------------------
             Trek Cards
        -------------------------------------------------- -->

        <div
            v-else-if="treks.length"
            class="row g-4">

            <div
                v-for="trek in treks"
                :key="trek.id"
                class="col-md-6 col-lg-4">

                <TrekCard
                    :trek="trek"
                    @view-details="viewDetails"
                />

            </div>

        </div>

        <!-- -------------------------------------------------
             Empty State
        -------------------------------------------------- -->

        <div
            v-else
            class="text-center py-5">

            <h5>No treks found.</h5>

            <p class="text-muted">
                Try changing your search or filter criteria.
            </p>

        </div>

    </section>

</template>

<script setup>

import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

import TrekCard from "./TrekCard.vue"
import SearchFilters from "./SearchFilters.vue"

import trekkerService from "@/services/trekkerService"

const router = useRouter()

const treks = ref([])

const loading = ref(true)

// ---------------------------------------------------------
// Load available treks with optional filters.
// ---------------------------------------------------------

async function loadTreks(filters = {}) {

    loading.value = true

    try {

        treks.value = await trekkerService.getTreks(filters)

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

// ---------------------------------------------------------
// Navigate to Trek Details page.
// ---------------------------------------------------------

function viewDetails(id) {

    router.push(`/dashboard/trekker/treks/${id}`)

}

onMounted(() => {

    loadTreks()

})

</script>