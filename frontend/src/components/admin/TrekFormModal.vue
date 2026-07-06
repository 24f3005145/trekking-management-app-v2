<template>
    <div
        v-if="show"
        class="modal fade show d-block"
        tabindex="-1"
        style="background: rgba(0,0,0,.5)"
    >
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title">
                        {{ isEdit ? "Edit Trek" : "Add Trek" }}
                    </h5>

                    <button
                        class="btn-close"
                        @click="$emit('close')"
                    ></button>
                </div>

                <div class="modal-body">

                    <div class="mb-3">
                        <label class="form-label">Trek Name</label>

                        <input
                            v-model="form.name"
                            class="form-control"
                        >
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Location</label>

                        <input
                            v-model="form.location"
                            class="form-control"
                        >
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Difficulty</label>

                        <select
                            v-model="form.difficulty"
                            class="form-select"
                        >
                            <option>Easy</option>
                            <option>Moderate</option>
                            <option>Hard</option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Duration (Days)</label>

                        <input
                            v-model.number="form.duration"
                            type="number"
                            min="1"
                            class="form-control"
                        >
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Available Slots</label>

                        <input
                            v-model.number="form.available_slots"
                            type="number"
                            min="0"
                            class="form-control"
                        >
                    </div>

                </div>

                <div class="modal-footer">

                    <button
                        class="btn btn-secondary"
                        @click="$emit('close')"
                    >
                        Cancel
                    </button>

                    <button
                        class="btn btn-success"
                        @click="save"
                        :disabled="loading"
                    >
                        {{ loading? (isEdit ? "Updating..." : "Creating...") : (isEdit ? "Update Trek" : "Create Trek")}}
                    </button>

                </div>

            </div>
        </div>
    </div>
</template>

<script setup>

import { reactive, watch } from "vue"

const emit = defineEmits([
    "save",
    "close"
])


const props = defineProps({
    show: Boolean,
    loading: Boolean,
    isEdit: Boolean,

    trek: {
        type: Object,
        default: () => ({})
    }
})

const form = reactive({
    name: "",
    location: "",
    difficulty: "Easy",
    duration: 1,
    available_slots: 0
})


watch(

    () => props.trek,

    (trek) => {

        if (!trek) return

        form.name = trek.name
        form.location = trek.location
        form.difficulty = trek.difficulty
        form.duration = trek.duration
        form.available_slots = trek.slots

    },

    {
        immediate: true
    }

)

function save() {

    emit("save", {
        ...form
    })

    form.name = ""
    form.location = ""
    form.difficulty = "Easy"
    form.duration = 1
    form.available_slots = 0

}

</script>