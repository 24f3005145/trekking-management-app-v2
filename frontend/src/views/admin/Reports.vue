<template>
    <div class="container-fluid">

        <h2 class="mb-4">
            Reports & Statistics
        </h2>

        <!-- Overview -->

        <div class="row g-4 mb-4">

            <div
                class="col-lg-3 col-md-6"
                v-for="card in overviewCards"
                :key="card.title"
            >

                <div class="card shadow-sm h-100">

                    <div class="card-body text-center">

                        <h6 class="text-muted">
                            {{ card.title }}
                        </h6>

                        <h2 class="fw-bold">
                            {{ card.value }}
                        </h2>

                    </div>

                </div>

            </div>

        </div>

        <!-- Difficulty -->

        <div class="card shadow-sm mb-4">

            <div class="card-header fw-bold">
                Trek Difficulty Distribution
            </div>

            <div class="card-body">

                <div
                    v-for="item in reports.difficulty_stats"
                    :key="item.difficulty"
                    class="mb-3"
                >

                    <div class="d-flex justify-content-between">

                        <span>{{ item.difficulty }}</span>

                        <span>{{ item.count }}</span>

                    </div>

                    <div class="progress">

                        <div
                            class="progress-bar"
                            :style="{
                                width: difficultyPercent(item.count)
                            }"
                        ></div>

                    </div>

                </div>

            </div>

        </div>

        <!-- Status -->

        <div class="card shadow-sm mb-4">

            <div class="card-header fw-bold">
                Trek Status
            </div>

            <div class="card-body">

                <div
                    v-for="item in reports.status_stats"
                    :key="item.status"
                    class="mb-3"
                >

                    <div class="d-flex justify-content-between">

                        <span>{{ item.status }}</span>

                        <span>{{ item.count }}</span>

                    </div>

                    <div class="progress">

                        <div
                            class="progress-bar bg-success"
                            :style="{
                                width: statusPercent(item.count)
                            }"
                        ></div>

                    </div>

                </div>

            </div>

        </div>

        <!-- Top Treks -->

        <div class="card shadow-sm mb-4">

            <div class="card-header fw-bold">
                Top Booked Treks
            </div>

            <div class="table-responsive">

                <table class="table table-hover mb-0">

                    <thead>

                        <tr>

                            <th>Trek</th>

                            <th>Bookings</th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="trek in reports.top_treks"
                            :key="trek.name"
                        >

                            <td>{{ trek.name }}</td>

                            <td>{{ trek.bookings }}</td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

        <!-- Monthly Bookings -->

        <div class="card shadow-sm mb-4">

            <div class="card-header fw-bold">
                Monthly Bookings
            </div>

            <div class="table-responsive">

                <table class="table table-striped mb-0">

                    <thead>

                        <tr>

                            <th>Month</th>

                            <th>Bookings</th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="month in reports.monthly_bookings"
                            :key="month.month"
                        >

                            <td>{{ month.month }}</td>

                            <td>{{ month.count }}</td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

        <!-- Users -->

        <div class="card shadow-sm">

            <div class="card-header fw-bold">
                Users By Role
            </div>

            <div class="table-responsive">

                <table class="table table-hover mb-0">

                    <thead>

                        <tr>

                            <th>Role</th>

                            <th>Users</th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="role in reports.users_by_role"
                            :key="role.role"
                        >

                            <td>{{ role.role }}</td>

                            <td>{{ role.count }}</td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

    </div>
</template>

<script setup>

import {

    ref,

    computed,

    onMounted

} from "vue"

import {

    getReports

} from "@/services/adminService"

const reports = ref({

    overview: {},

    difficulty_stats: [],

    status_stats: [],

    top_treks: [],

    monthly_bookings: [],

    users_by_role: []

})

const overviewCards = computed(() => [

    {
        title: "Total Treks",
        value: reports.value.overview.total_treks
    },

    {
        title: "Bookings",
        value: reports.value.overview.total_bookings
    },

    {
        title: "Users",
        value: reports.value.overview.total_users
    },

    {
        title: "Staff",
        value: reports.value.overview.total_staff
    },

    {
        title: "Trekkers",
        value: reports.value.overview.total_trekkers
    },

    {
        title: "Open Treks",
        value: reports.value.overview.open_treks
    },

    {
        title: "Completed",
        value: reports.value.overview.completed_treks
    }

])

function difficultyPercent(count) {

    const total = reports.value.overview.total_treks || 1

    return `${(count / total) * 100}%`

}

function statusPercent(count) {

    const total = reports.value.overview.total_treks || 1

    return `${(count / total) * 100}%`

}

async function loadReports() {

    reports.value = await getReports()

}

onMounted(loadReports)

</script>