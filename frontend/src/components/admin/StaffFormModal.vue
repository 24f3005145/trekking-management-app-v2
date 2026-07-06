<template>

<div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background:rgba(0,0,0,.5)"
>

    <div class="modal-dialog">

        <div class="modal-content">

            <div class="modal-header">

                <h5 class="modal-title">

                    Add Staff

                </h5>

                <button
                    class="btn-close"
                    @click="$emit('close')"
                ></button>

            </div>

            <div class="modal-body">

                <div class="mb-3">

                    <label class="form-label">
                        Name
                    </label>

                    <input
                        v-model="form.name"
                        class="form-control"
                    >

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Email
                    </label>

                    <input
                        v-model="form.email"
                        type="email"
                        class="form-control"
                    >

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Phone
                    </label>

                    <input
                        v-model="form.phone"
                        class="form-control"
                    >

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Password
                    </label>

                    <input
                        v-model="form.password"
                        type="password"
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

                    {{ loading ? "Creating..." : "Create Staff" }}

                </button>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

import { reactive } from "vue"

// NEW
defineProps({

    show: Boolean,

    loading: Boolean

})

const emit = defineEmits([
    "save",
    "close"
])

const form = reactive({

    name: "",

    email: "",

    phone: "",

    password: ""

})

// NEW
function resetForm() {

    form.name = ""
    form.email = ""
    form.phone = ""
    form.password = ""

}

function save() {

    emit(
        "save",
        {
            ...form
        }
    )

    resetForm()

}

</script>