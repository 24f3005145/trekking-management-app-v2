<template>

<div
    v-if="show"
    class="modal fade show d-block"
    tabindex="-1"
    style="background: rgba(0,0,0,.5)"
>

    <div class="modal-dialog modal-dialog-centered">

        <div class="modal-content">

            <div class="modal-header">

                <h5 class="modal-title">

                    Confirm Delete

                </h5>

                <button
                    class="btn-close"
                    @click="$emit('close')"
                ></button>

            </div>

            <div class="modal-body">

                <p class="mb-0">

                    Are you sure you want to delete

                    <strong>"{{ trekName }}"</strong>?

                </p>

                <small class="text-danger">

                    This action cannot be undone.

                </small>

            </div>

            <div class="modal-footer">

                <button
                    class="btn btn-secondary"
                    @click="$emit('close')"
                    :disabled="loading"
                >

                    Cancel

                </button>

                <button
                    class="btn btn-danger"
                    @click="$emit('confirm')"
                    :disabled="loading"
                >

                    {{ loading ? "Deleting..." : "Delete Trek" }}

                </button>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

// NEW
defineProps({

    show: Boolean,

    loading: Boolean,

    trekName: {

        type: String,

        default: ""

    }

})

defineEmits([

    "close",

    "confirm"

])

</script>