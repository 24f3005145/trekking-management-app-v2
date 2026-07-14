<template>

<div class="container-fluid">

    <!-- =====================================================
         Profile
    ====================================================== -->

    <h2 class="fw-bold mb-4">

        My Profile

    </h2>

    <div
        v-if="loading"
        class="text-center py-5">

        <div class="spinner-border text-success"></div>

    </div>

    <div
        v-else
        class="row">

        <!-- ============================================== -->
        <!-- Profile Card -->
        <!-- ============================================== -->

        <div class="col-lg-6">

            <div class="card">
                <form
                    autocomplete="off"
                    @submit.prevent="saveProfile">

                <div class="card-body">

                    <h4 class="mb-4">

                        Personal Information

                    </h4>

                    <div class="mb-3">

                        <label class="form-label">

                            Name

                        </label>

                        <input
                            v-model="profile.name"
                            class="form-control"
                            autocomplete="name">

                    </div>

                    <div class="mb-3">

                        <label class="form-label">

                            Email

                        </label>

                        <input
                            v-model="profile.email"
                            class="form-control"
                            readonly
                            autocomplete="email">

                    </div>

                    <div class="mb-4">

                        <label class="form-label">

                            Phone

                        </label>

                        <input
                            v-model="profile.phone"
                            class="form-control"
                            autocomplete="tel">

                    </div>

                    <button
                        type="submit"
                        class="btn btn-success">

                        Save Changes

                    </button>

                </div>
                </form>

            </div>

        </div>

        <!-- ============================================== -->
        <!-- Password Card -->
        <!-- ============================================== -->

        <div class="col-lg-6">

            <div class="card">

                <form
                    autocomplete="off"
                    @submit.prevent="updatePassword">

                <div class="card-body">

                    <h4 class="mb-4">

                        Change Password

                    </h4>

                    <div class="mb-3">

                        <input
                            v-model="password.current_password"
                            type="password"
                            class="form-control"
                            placeholder="Current Password"
                            autocomplete="current-password">

                    </div>

                    <div class="mb-4">

                        <input
                            v-model="password.new_password"
                            type="password"
                            class="form-control"
                            placeholder="New Password"
                            autocomplete="new-password">

                    </div>

                    <button
                        type="submit"
                        class="btn btn-primary">

                        Change Password

                    </button>

                </div>

                </form>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

// =====================================================
// Imports
// =====================================================

import { ref, onMounted } from "vue"

import trekkerService from "@/services/trekkerService"
import { useToastStore } from "@/stores/toast"             // Global Toast store

// =====================================================
// State
// =====================================================

const loading = ref(true)

const toast = useToastStore()              // Toast


const profile = ref({})

const password = ref({

    current_password: "",
    new_password: ""

})

// =====================================================
// Load profile
// =====================================================

async function loadProfile() {

    try {

        profile.value = await trekkerService.getProfile()

    }

    catch (error) {

        console.error(error)

    }

    finally {

        loading.value = false

    }

}

// =====================================================
// Save profile
// =====================================================

async function saveProfile() {

    try {

        await trekkerService.updateProfile({

            name: profile.value.name,
            phone: profile.value.phone

        })

        toast.trigger(
            "Profile updated successfully.",
            "success"
        )

    }

    catch (error) {

        toast.trigger(
            error.response?.data?.message ||
            "Unable to update profile.",
            "error"
        )

    }

}

// =====================================================
// Change password
// =====================================================

async function updatePassword() {

    try {

        await trekkerService.changePassword(password.value)

        toast.trigger("Password changed successfully.", "success")

        password.value = {

            current_password: "",
            new_password: ""

        }

    }

    catch (error) {

        toast.trigger(error.response?.data?.message || "Unable to change password.", "error")

    }

}

onMounted(loadProfile)

</script>