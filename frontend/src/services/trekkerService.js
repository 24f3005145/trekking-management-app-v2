import api from "./api";

export default {

    // ---------------------------------------------------------
    // Fetch all available treks with optional search & filters.
    // ---------------------------------------------------------
    async getTreks(params = {}) {

        const response = await api.get("/user/treks", {
            params
        });

        return response.data;

    },

    // ---------------------------------------------------------
    // Fetch complete details of a single trek.
    // ---------------------------------------------------------
    async getTrekDetails(id) {

        const response = await api.get(`/user/treks/${id}`);

        return response.data;

    },

    // ---------------------------------------------------------
    // Book a trek.
    // ---------------------------------------------------------
    async bookTrek(id) {

        const response = await api.post(`/user/book/${id}`);

        return response.data;

    },

    // ---------------------------------------------------------
    // Fetch logged-in user's bookings.
    // ---------------------------------------------------------
    async getBookings() {

        const response = await api.get("/user/bookings");

        return response.data;

    },
    // ---------------------------------------------------------
    // Fetch logged-in user's profile.
    // ---------------------------------------------------------
    async getProfile() {

        const response = await api.get("/user/profile");

        return response.data;

    },

    // ---------------------------------------------------------
    // Update logged-in user's profile.
    // ---------------------------------------------------------
    async updateProfile(data) {

        const response = await api.put("/user/profile", data);

        return response.data;

    },

    // ---------------------------------------------------------
    // Change logged-in user's password.
    // ---------------------------------------------------------
    async changePassword(data) {

        const response = await api.put("/user/change-password", data);

        return response.data;

    },
    // ---------------------------------------------------------
    // Start booking history export.
    // ---------------------------------------------------------
    async exportBookings() {

        const response = await api.post("/user/export-bookings");

        return response.data;

    },

    // ---------------------------------------------------------
    // Get export job status.
    // ---------------------------------------------------------
    async getExportStatus(jobId) {

        const response = await api.get(
            `/user/export-status/${jobId}`
        );

        return response.data;

    }

};