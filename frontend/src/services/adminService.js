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

// Activate or Deactivate Staff
export async function updateStaffStatus(staffId, isActive) {

    const response = await api.put(

        `/admin/staff/${staffId}/status`,

        {
            is_active: isActive
        }

    )

    return response.data

}

// Get Treks Assigned To Staff
export async function getStaffTreks(staffId) {

    const response = await api.get(
        `/admin/staff/${staffId}/treks`

    )

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

// ----------------------------------------------------
// Users
// ----------------------------------------------------

export async function getUsers(params = {}) {

    const response = await api.get("/admin/users", {
        params
    })

    return response.data

}

export async function updateUserStatus(userId, isActive) {

    const response = await api.put(

        `/admin/users/${userId}/status`,

        {
            is_active: isActive
        }

    )

    return response.data

}

// ----------------------------------------------------
// Reports
// ----------------------------------------------------

export async function getReports() {

    const response = await api.get("/admin/reports")

    return response.data

}