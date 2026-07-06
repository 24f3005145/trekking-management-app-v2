import api from "./api";

export default {

  getDashboard() {
    return api.get("/staff/dashboard");
  },

  async getAssignedTreks() {
    const response = await api.get("/staff/treks");
    return response.data;
  },
  
  async getTrekDetails(id) {
    const response = await api.get(`/staff/trek/${id}`);
    return response.data;
  },
  async getParticipants(id) {
    const response = await api.get(`/staff/trek/${id}/participants`);
    return response.data;
  },
  async updateStatus(id, data) {
    const response = await api.put(`/staff/trek/${id}/status`, data);
    return response.data;
  },

  async updateSlots(id, data) {
    const response = await api.put(`/staff/trek/${id}/slots`, data);
    return response.data;
  }

};

