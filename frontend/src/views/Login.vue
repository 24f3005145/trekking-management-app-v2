<template>
  <div class="container-fluid vh-100">

    <div class="row h-100">

      <!-- Left Side -->
      <div
        class="col-lg-6 d-none d-lg-flex
               bg-success text-white
               align-items-center justify-content-center">

        <div class="text-center">

          <h1 class="display-3 fw-bold">

            🥾 TrekMate

          </h1>

          <p class="lead mt-3">

            Adventure starts here.

          </p>

        </div>

      </div>

      <!-- Right Side -->

      <div
        class="col-lg-6 d-flex
               align-items-center
               justify-content-center">

        <div
          class="card shadow-lg p-4"
          style="width:420px;">

          <h2 class="text-center mb-4">

            Login

          </h2>

          <form @submit.prevent="login">

            <div class="mb-3">

              <label class="form-label">

                Email

              </label>

              <input
                v-model="email"
                type="email"
                class="form-control"
                required>

            </div>

            <div class="mb-4">

              <label class="form-label">

                Password

              </label>

              <input
                v-model="password"
                type="password"
                class="form-control"
                required>

            </div>

            <button
              class="btn btn-success w-100">

              Login

            </button>

          </form>

          <p class="text-center mt-4">

            Don't have an account?

            <RouterLink to="/register">

              Register

            </RouterLink>

          </p>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>



import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import api from '@/services/api'
import { useAuthStore } from '@/stores/auth'

import { useToastStore } from "@/stores/toast"           // Toast

const router = useRouter()

const auth = useAuthStore()

const toast = useToastStore()              // Toast

const email = ref("")
const password = ref("")

//const error = ref("")              // used Toast instead

async function login(){


    try{

        const response=await api.post(
            "/auth/login",
            {
                email:email.value,
                password:password.value
            }
        )

        auth.login(
            response.data.token,
            {
                id:response.data.user_id,
                name:response.data.name,
                role:response.data.role
            }
        )

        if(response.data.role==="Admin"){

            router.push("/dashboard/admin")

        }

        else if(response.data.role==="Trek Staff"){

            router.push("/dashboard/staff")

        }

        else{

            router.push("/dashboard/trekker")

        }

    }

    catch (err) {

      password.value = ""

      toast.trigger(

          err.response?.data?.message ||

          "Invalid email or password.",

          "error"

      )
    }

}

onMounted(() => {

    const message = sessionStorage.getItem("toastMessage")
    const type = sessionStorage.getItem("toastType")

    if (message) {

        toast.trigger(
            message,
            type || "error"
        )

        sessionStorage.removeItem("toastMessage")
        sessionStorage.removeItem("toastType")

    }

})

</script>