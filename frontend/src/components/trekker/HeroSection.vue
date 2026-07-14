<template>
    <!-- =====================================================
         Trekker Hero Section
         Displayed at the top of the Trekker Dashboard
    ====================================================== -->

    <section class="hero-section d-flex align-items-center">

        <div class="container">

            <div class="row">

                <div class="col-lg-7">

                    <h1 class="display-4 fw-bold text-white">
                        Adventure Awaits Beyond Every Trail
                    </h1>

                    <p class="lead text-white mt-3">
                        Discover breathtaking trekking destinations,
                        explore nature, and create unforgettable memories.
                    </p>

                    <!-- Search Bar (UI only for now) -->
                    <div class="input-group mt-4 shadow">

                        <input
                            type="text"
                            class="form-control form-control-lg"
                            placeholder="Search your next trek..."
                        >

                        <button class="btn btn-success">
                            Explore
                        </button>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
// Hero section is purely presentational for now.
// Search functionality will be connected later.
</script>

<style scoped>

.hero-section {

    min-height: 75vh;

    background:
        linear-gradient(
            rgba(0,0,0,.55),
            rgba(0,0,0,.55)
        ),
        url("@/assets/images/hero-banner.jpg");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    border-radius: 15px;

    padding: 80px 0;

    margin-bottom: 40px;
}

.input-group {

    max-width: 600px;

}

.form-control {

    border: none;

}

.btn-success {

    padding-left: 30px;
    padding-right: 30px;

}

</style>