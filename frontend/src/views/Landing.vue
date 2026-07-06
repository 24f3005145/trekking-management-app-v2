<template>
  <PublicNavbar  />

  <!-- Hero Section -->
  <section class="py-5 bg-light">
    <div class="container">
      <div class="row align-items-center">

        <div class="col-lg-6">
          <h1 class="display-4 fw-bold text-success">
            Explore Nature.
            <br>
            Book Your Next Trek.
          </h1>

          <p class="lead mt-4 text-muted">
            TrekMate helps you discover amazing trekking adventures,
            book treks effortlessly, and track your journey—all in one place.
          </p>

          <div class="mt-4">
            <RouterLink to="/register" class="btn btn-success btn-lg me-3">
              Get Started
            </RouterLink>

            <RouterLink to="/login" class="btn btn-outline-success btn-lg">
              Login
            </RouterLink>
          </div>
        </div>

        <div class="col-lg-6 text-center mt-5 mt-lg-0">
          <img
            src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=900"
            class="img-fluid rounded shadow"
            alt="Mountain Trek"
          >
        </div>

      </div>
    </div>
  </section>

  <!-- Features -->
  <section class="py-5">
    <div class="container">

      <h2 class="text-center fw-bold mb-5">
        Why Choose TrekMate?
      </h2>

      <div class="row g-4">

        <div class="col-md-4">
          <div class="card h-100 p-4 text-center">
            <h3>🥾</h3>
            <h5 class="mt-3">Easy Booking</h5>
            <p class="text-muted">
              Browse available treks and reserve your slot in seconds.
            </p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 p-4 text-center">
            <h3>🗺️</h3>
            <h5 class="mt-3">Verified Treks</h5>
            <p class="text-muted">
              Explore routes managed by experienced trek staff.
            </p>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card h-100 p-4 text-center">
            <h3>📊</h3>
            <h5 class="mt-3">Track History</h5>
            <p class="text-muted">
              View your bookings and completed treks anytime.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Statistics -->
  <section class="py-5 bg-success text-white">
    <div class="container">

      <div class="row text-center">

        <div class="col-md-4">
          <h1 class="fw-bold">100+</h1>
          <p>Treks Organized</p>
        </div>

        <div class="col-md-4">
          <h1 class="fw-bold">500+</h1>
          <p>Happy Trekkers</p>
        </div>

        <div class="col-md-4">
          <h1 class="fw-bold">25+</h1>
          <p>Expert Trek Staff</p>
        </div>

      </div>

    </div>
  </section>

  <Footer />
</template>

<script setup>
import { RouterLink } from 'vue-router'
import PublicNavbar from '@/components/PublicNavbar.vue'
import Footer from '@/components/Footer.vue'
</script>