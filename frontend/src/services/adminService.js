import api from "./api";

export async function getDashboardSummary() {
    const response = await api.get("/admin/dashboard-summary");
    return response.data;
}

export async function getTreks() {
    const response = await api.get("/admin/treks");
    return response.data;
}

export async function getRecentTreks() {
    const response = await api.get("/admin/recent-treks");
    return response.data;
}

export async function getRecentBookings() {
    const response = await api.get("/admin/recent-bookings");
    return response.data;
}

//-------------------------------------------------------------------------------------------------------------------
//NEW: Create a trek
export async function createTrek(data) {
    const response = await api.post("/admin/treks", data);
    return response.data;
}

// NEW: Update an existing trek
export async function updateTrek(id, data) {
    const response = await api.put(`/admin/treks/${id}`, data)
    return response.data
}

// NEW: Delete a trek
export async function deleteTrek(id) {
    const response = await api.delete(`/admin/treks/${id}`)
    return response.data
}
//------------------------------------------------------------------------------------------------------------------
// NEW: Fetch all staff members
export async function getStaff() {
    const response = await api.get("/admin/staff")
    return response.data
}

// NEW: Create a new staff member
export async function createStaff(data) {

    const response = await api.post("/admin/staff", data)

    return response.data

}

// NEW: Assign staff to a trek
export async function assignStaff(trekId, staffId) {

    const response = await api.put(
        `/admin/assign-staff/${trekId}`,
        {
            staff_id: staffId
        }
    )

    return response.data

}