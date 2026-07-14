import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
  headers: {
    "Content-Type": "application/json",
  },
});

// ---------------------------------------------------------
// Attach JWT Token
// ---------------------------------------------------------

api.interceptors.request.use((config) => {

  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;

});

// ---------------------------------------------------------
// Handle Unauthorized / Deactivated Accounts
// ---------------------------------------------------------

api.interceptors.response.use(

  (response) => response,

  (error) => {

    if (error.response) {

      const status = error.response.status;

      const message = error.response.data?.message;

      if (
        status === 403 &&
        (
          message === "Your account has been deactivated." ||
          message === "Your account has been deactivated. Please contact the administrator."
        )
      ) {

        localStorage.removeItem("token");
        localStorage.removeItem("role");
        localStorage.removeItem("user_id");
        localStorage.removeItem("name");

        sessionStorage.setItem(
          "toastMessage",
          "Your account has been deactivated. Please contact the administrator."
        );

        sessionStorage.setItem(
          "toastType",
          "error"
        );

        window.location.href = "/login";
      }

    }

    return Promise.reject(error);

  }

);

export default api;