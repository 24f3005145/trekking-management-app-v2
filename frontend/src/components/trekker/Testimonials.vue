<template>

<section class="my-5">

    <h2 class="fw-bold text-center mb-4">

        What Our Trekkers Say

    </h2>

    <div class="row g-4">

        <div
            class="col-md-4"
            v-for="testimonial in testimonials"
            :key="testimonial.name">

            <div class="card h-100 p-4">

                <h5>{{ testimonial.name }}</h5>

                <p class="text-warning">

                    ⭐⭐⭐⭐⭐

                </p>

                <p>

                    "{{ testimonial.review }}"

                </p>

            </div>

        </div>

    </div>

</section>

</template>

<script setup>

const testimonials = [

    {
        name:"Rahul",
        review:"An unforgettable trekking experience. The guides were fantastic."
    },

    {
        name:"Sneha",
        review:"Beautiful trails, well organized and completely safe."
    },

    {
        name:"Amit",
        review:"One of the best adventure trips I've ever been on."

    }

]

</script>