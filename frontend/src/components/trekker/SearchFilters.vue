<template>

<div class="card mb-4">

    <div class="card-body">

        <div class="row g-3">

            <div class="col-md-4">

                <input
                    v-model="filters.search"
                    class="form-control"
                    placeholder="Search Trek">

            </div>

            <div class="col-md-3">

                <select
                    v-model="filters.difficulty"
                    class="form-select">

                    <option value="">All Difficulty</option>
                    <option>Easy</option>
                    <option>Moderate</option>
                    <option>Hard</option>

                </select>

            </div>

            <div class="col-md-3">

                <input
                    v-model="filters.location"
                    class="form-control"
                    placeholder="Location">

            </div>

            <div class="col-md-2">

                <button
                    class="btn btn-success w-100"
                    @click="$emit('search', filters)">

                    Search

                </button>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

import { reactive } from "vue"

// ---------------------------------------------------------
// Search filters.
// ---------------------------------------------------------

const filters = reactive({

    search:"",
    difficulty:"",
    location:"",
    duration:""

})

defineEmits([
    "search"
])

</script>