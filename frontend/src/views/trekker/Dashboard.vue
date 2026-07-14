<template>

<div class="container-fluid">

    <!-- Hero Section -->

    <HeroSection />

    <!-- TrekMate Statistics -->

    <Statistics />

    <!-- Featured Treks -->

    <FeaturedTreks />

    <!-- Why Choose Us -->

    <WhyChooseUs />

    <!-- Testimonials -->

    <Testimonials />

    <!-- Adventure Gallery -->

    <AdventureGallery />

</div>

</template>

<script setup>

import HeroSection from "@/components/trekker/HeroSection.vue"
import Statistics from "@/components/trekker/Statistics.vue"
import FeaturedTreks from "@/components/trekker/FeaturedTreks.vue"
import WhyChooseUs from "@/components/trekker/WhyChooseUs.vue"
import Testimonials from "@/components/trekker/Testimonials.vue"
import AdventureGallery from "@/components/trekker/AdventureGallery.vue"

</script>