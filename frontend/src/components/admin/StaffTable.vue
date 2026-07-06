<template>

<div class="card shadow-sm border-0">

    <div class="card-body">

        <div class="d-flex justify-content-between align-items-center mb-3">

            <h4 class="mb-0">
                All Staff
            </h4>

            <small class="text-muted">

                {{ staff.length }} Staff Member(s)

            </small>

        </div>

        <div class="table-responsive">

            <table class="table table-hover align-middle">

                <thead>

                    <tr>

                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>

                    </tr>

                </thead>

                <tbody>

                    <tr
                        v-for="member in staff"
                        :key="member.id"
                    >

                        <td>{{ member.name }}</td>

                        <td>{{ member.email }}</td>

                        <td>{{ member.phone }}</td>

                    </tr>

                    <tr
                        v-if="staff.length===0"
                    >

                        <td
                            colspan="3"
                            class="text-center text-muted"
                        >

                            No staff found.

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </div>

</div>

</template>

<script setup>

defineProps({

    staff: {

        type: Array,

        default: () => []

    }

})

</script>