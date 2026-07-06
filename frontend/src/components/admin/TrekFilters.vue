<template>
    <div class="card shadow-sm border-0 mb-4">

        <div class="card-body">

            <div class="row g-3">

                <div class="col-md-6">

                    <label class="form-label">
                        Search
                    </label>

                    <input
                        :value="search"
                        @input="updateSearch"
                        type="text"
                        class="form-control"
                        placeholder="Search by trek name or location..."
                    >

                </div>

                <div class="col-md-3">

                    <label class="form-label">
                        Difficulty
                    </label>

                    <select
                        :value="difficulty"
                        @change="updateDifficulty"
                        class="form-select"
                    >

                        <option value="">All</option>
                        <option value="Easy">Easy</option>
                        <option value="Moderate">Moderate</option>
                        <option value="Hard">Hard</option>

                    </select>

                </div>

                <div class="col-md-3">

                    <label class="form-label">
                        Status
                    </label>

                    <select
                        :value="status"
                        @change="updateStatus"
                        class="form-select"
                    >

                        <option value="">All</option>
                        <option value="Open">Open</option>
                        <option value="Closed">Closed</option>
                        <option value="Completed">Completed</option>
                        <option value="Pending">Pending</option>

                    </select>

                </div>

            </div>

        </div>

    </div>
</template>

<script setup>

defineProps({

    search: String,
    difficulty: String,
    status: String

})

const emit = defineEmits([
    "update:search",
    "update:difficulty",
    "update:status"
])

function updateSearch(event) {
    emit("update:search", event.target.value)
}

function updateDifficulty(event) {
    emit("update:difficulty", event.target.value)
}

function updateStatus(event) {
    emit("update:status", event.target.value)
}

</script>