<template>
    <div class="container-fluid">

        <div class="d-flex justify-content-between align-items-center mb-4">
            <h2>Manage Users</h2>
        </div>

        <!-- Filters -->

        <div class="card shadow-sm mb-4">

            <div class="card-body">

                <div class="row g-3">

                    <div class="col-md-4">

                        <input
                            v-model="filters.search"
                            class="form-control"
                            placeholder="Search by name or email"
                        >

                    </div>

                    <div class="col-md-3">

                        <select
                            v-model="filters.role"
                            class="form-select"
                        >
                            <option value="">All Roles</option>
                            <option>Admin</option>
                            <option>Trek Staff</option>
                            <option>Trekker</option>
                        </select>

                    </div>

                    <div class="col-md-3">

                        <select
                            v-model="filters.status"
                            class="form-select"
                        >
                            <option value="">All Status</option>
                            <option value="active">Active</option>
                            <option value="inactive">Inactive</option>
                        </select>

                    </div>

                    <div class="col-md-2">

                        <button
                            class="btn btn-success w-100"
                            @click="loadUsers"
                        >
                            Search
                        </button>

                    </div>

                </div>

            </div>

        </div>

        <!-- Users Table -->

        <div class="card shadow-sm">

            <div class="table-responsive">

                <table class="table table-hover align-middle mb-0">

                    <thead class="table-light">

                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Role</th>
                            <th>Status</th>
                            <th width="160">Action</th>
                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="user in users"
                            :key="user.id"
                        >

                            <td>{{ user.name }}</td>

                            <td>{{ user.email }}</td>

                            <td>{{ user.phone || "-" }}</td>

                            <td>{{ user.role }}</td>

                            <td>

                                <span
                                    class="badge"
                                    :class="user.is_active
                                        ? 'bg-success'
                                        : 'bg-danger'"
                                >
                                    {{ user.is_active ? "Active" : "Inactive" }}
                                </span>

                            </td>

                            <td>

                                <button
                                    v-if="user.is_active"
                                    class="btn btn-sm btn-outline-danger"
                                    @click="toggleStatus(user, false)"
                                >
                                    Deactivate
                                </button>

                                <button
                                    v-else
                                    class="btn btn-sm btn-outline-success"
                                    @click="toggleStatus(user, true)"
                                >
                                    Activate
                                </button>

                            </td>

                        </tr>

                        <tr v-if="!users.length">

                            <td
                                colspan="6"
                                class="text-center py-4"
                            >
                                No users found.
                            </td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

    </div>
</template>

<script setup>

import { ref, reactive, onMounted } from "vue"

import {

    getUsers,

    updateUserStatus

} from "@/services/adminService"

const users = ref([])

const filters = reactive({

    search: "",

    role: "",

    status: ""

})

async function loadUsers() {

    users.value = await getUsers(filters)

}

async function toggleStatus(user, active) {

    const confirmed = window.confirm(

        `Are you sure you want to ${active ? "activate" : "deactivate"} ${user.name}?`

    )

    if (!confirmed) return

    await updateUserStatus(user.id, active)

    await loadUsers()

}

onMounted(loadUsers)

</script>