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
                    Assign Staff
                </h5>

                <button
                    class="btn-close"
                    @click="$emit('close')"
                ></button>

            </div>

            <div class="modal-body">

                <label class="form-label">
                    Select Staff Member
                </label>

                <select
                    v-model="selectedStaff"
                    class="form-select"
                >

                    <option disabled value="">
                        Choose Staff
                    </option>

                    <option
                        v-for="member in staff"
                        :key="member.id"
                        :value="member.id"
                    >

                        {{ member.name }}

                    </option>

                </select>

            </div>

            <div class="modal-footer">

                <button
                    class="btn btn-secondary"
                    @click="$emit('close')"
                >
                    Cancel
                </button>

                <button
                    class="btn btn-primary"
                    @click="save"
                >
                    Assign
                </button>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

import { ref, watch } from "vue"

// NEW
const props = defineProps({

    show: Boolean,

    staff: {
        type: Array,
        default: () => []
    },

    assignedStaffId: Number

})

const emit = defineEmits([
    "save",
    "close"
])

const selectedStaff = ref("")

// NEW: Pre-select current assignment
watch(

    () => props.assignedStaffId,

    (value) => {

        selectedStaff.value = value ?? ""

    },

    {
        immediate: true
    }

)

function save() {

    emit(
        "save",
        selectedStaff.value
    )

}

</script>