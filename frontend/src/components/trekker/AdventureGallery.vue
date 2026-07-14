<template>

<section class="my-5">

    <h2 class="fw-bold text-center mb-4">

        Adventure Gallery

    </h2>

    <div class="row g-4">

        <div
            class="col-md-4"
            v-for="image in images"
            :key="image">

            <img
                :src="image"
                class="gallery-image rounded shadow-sm"
            >

        </div>

    </div>

</section>

</template>

<script setup>

import gallery1 from "@/assets/images/gallery/gallery1.jpg"
import gallery2 from "@/assets/images/gallery/gallery2.jpg"
import gallery3 from "@/assets/images/gallery/gallery3.jpg"
import gallery4 from "@/assets/images/gallery/gallery4.jpg"
import gallery5 from "@/assets/images/gallery/gallery5.jpg"
import gallery6 from "@/assets/images/gallery/gallery6.jpg"

// ---------------------------------------------------------
// Static gallery images.
// ---------------------------------------------------------

const images = [

    gallery1,
    gallery2,
    gallery3,
    gallery4,
    gallery5,
    gallery6

]

</script>

<style scoped>

.gallery-image{

    width:100%;
    height:250px;
    object-fit:cover;

    transition:.3s;

}

.gallery-image:hover{

    transform:scale(1.03);

}

</style>