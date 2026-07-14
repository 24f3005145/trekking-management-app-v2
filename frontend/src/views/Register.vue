<template>

<div class="container-fluid vh-100">

    <div class="row h-100">

        <!-- Left Side -->

        <div
            class="col-lg-6 d-none d-lg-flex bg-success text-white align-items-center justify-content-center"
        >

            <div class="text-center px-5">

                <h1 class="display-4 fw-bold">

                    TrekMate

                </h1>

                <p class="lead">

                    Create your Trekker account and start exploring adventures.

                </p>

            </div>

        </div>

        <!-- Right Side -->

        <div
            class="col-lg-6 d-flex align-items-center justify-content-center"
        >

            <div
                class="card shadow-lg border-0"
                style="max-width:500px; width:100%;"
            >

                <div class="card-body p-4">

                    <h2 class="text-center mb-4">

                        Trekker Registration

                    </h2>

                    <form @submit.prevent="register">

                        <!-- Name -->

                        <div class="mb-3">

                            <label class="form-label">

                                Full Name

                            </label>

                            <input
                                v-model="form.name"
                                class="form-control"
                                required
                            >

                        </div>

                        <!-- Email -->

                        <div class="mb-3">

                            <label class="form-label">

                                Email

                            </label>

                            <input
                                v-model="form.email"
                                type="email"
                                class="form-control"
                                required
                            >

                        </div>

                        <!-- Phone -->

                        <div class="mb-3">

                            <label class="form-label">

                                Phone

                            </label>

                            <input
                                v-model="form.phone"
                                class="form-control"
                                required
                            >

                        </div>

                        <!-- Password -->

                        <div class="mb-3">

                            <label class="form-label">

                                Password

                            </label>

                            <div class="input-group">

                                <input
                                    :type="showPassword ? 'text' : 'password'"
                                    v-model="form.password"
                                    class="form-control"
                                    minlength="8"
                                    required
                                >

                                <button
                                    class="btn btn-outline-secondary"
                                    type="button"
                                    @click="showPassword = !showPassword"
                                >

                                    {{ showPassword ? "Hide" : "Show" }}

                                </button>

                            </div>

                        </div>

                        <!-- Confirm Password -->

                        <div class="mb-4">

                            <label class="form-label">

                                Confirm Password

                            </label>

                            <div class="input-group">

                                <input
                                    :type="showConfirmPassword ? 'text' : 'password'"
                                    v-model="confirmPassword"
                                    class="form-control"
                                    minlength="8"
                                    required
                                >

                                <button
                                    class="btn btn-outline-secondary"
                                    type="button"
                                    @click="showConfirmPassword = !showConfirmPassword"
                                >

                                    {{ showConfirmPassword ? "Hide" : "Show" }}

                                </button>

                            </div>

                        </div>

                        <button
                            class="btn btn-success w-100"
                            :disabled="loading"
                        >

                            {{ loading ? "Registering..." : "Register" }}

                        </button>

                    </form>

                    <div class="text-center mt-4">

                        Already have an account?

                        <RouterLink to="/login">

                            Login

                        </RouterLink>

                    </div>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<script setup>

import { ref } from "vue"

import { useRouter, RouterLink } from "vue-router"

import api from "@/services/api"

import { useToastStore } from "@/stores/toast"

const router = useRouter()

const toast = useToastStore()

const loading = ref(false)

const showPassword = ref(false)

const showConfirmPassword = ref(false)

const confirmPassword = ref("")

const form = ref({

    name: "",

    email: "",

    phone: "",

    password: ""

})

async function register() {

    if (form.value.password !== confirmPassword.value) {

        toast.trigger(

            "Passwords do not match.",

            "danger"

        )

        return

    }

    loading.value = true

    try {

        const response = await api.post(

            "/auth/register",

            form.value

        )

        toast.trigger(

            response.data.message,

            "success"

        )

        router.push("/login")

    }

    catch (error) {

        toast.trigger(

            error.response?.data?.message ||

            "Registration failed.",

            "danger"

        )

    }

    finally {

        loading.value = false

    }

}

</script>