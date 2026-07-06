import { createRouter, createWebHistory } from 'vue-router'

// NEW
import { useAuthStore } from '@/stores/auth'

// Public Pages
import Landing from '@/views/Landing.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'

// Layout
import MainLayout from '@/layouts/MainLayout.vue'

// Admin
import AdminDashboard from '@/views/admin/Dashboard.vue'
import Treks from '@/views/admin/Treks.vue'

// Staff
import StaffDashboard from '@/views/staff/Dashboard.vue'
import Staff from '@/views/admin/Staff.vue'
import StaffTreks from '@/views/staff/Treks.vue'
import TrekDetails from '@/views/staff/TrekDetails.vue'
import Participants from '@/views/staff/Participants.vue'

// Trekker
import TrekkerDashboard from '@/views/trekker/Dashboard.vue'

const routes = [
    {
        path: '/',
        name: 'Landing',
        component: Landing
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/dashboard',
        component: MainLayout,
        children: [
            {
                path: 'admin',
                name: 'AdminDashboard',
                component: AdminDashboard,

                // NEW
                meta: {
                    requiresAuth: true,
                    role: "Admin"
                }
            },
            {
                path: 'admin/treks',
                name: 'AdminTreks',
                component: Treks,

                // NEW
                meta: {
                    requiresAuth: true,
                    role: "Admin"
                }
            },
            {
                path: 'admin/staff',
                name: 'AdminStaff',
                component: Staff,

                // NEW
                meta: {
                    requiresAuth: true,
                    role: "Admin"
                }
            },
            {
                path: 'staff',
                name: 'StaffDashboard',
                component: StaffDashboard,

                // NEW
                meta: {
                    requiresAuth: true,
                    role: "Trek Staff"
                }
            },
            {
                path: 'staff/treks',
                name: 'StaffTreks',
                component: StaffTreks,

                meta: {
                    requiresAuth: true,
                    role: "Trek Staff"
                }
            },
            {
                path: 'staff/treks/:id',
                name: 'StaffTrekDetails',
                component: TrekDetails,

                meta: {
                    requiresAuth: true,
                    role: "Trek Staff"
                }
            },
            {
                path: 'staff/treks/:id/participants',
                name: 'StaffParticipants',
                component: Participants,

                meta: {
                    requiresAuth: true,
                    role: "Trek Staff"
                }
            },
            {
                path: 'trekker',
                name: 'TrekkerDashboard',
                component: TrekkerDashboard,

                // NEW
                meta: {
                    requiresAuth: true,
                    role: "Trekker"
                }
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// =====================================================
// NEW
// Authentication Route Guard
// =====================================================

router.beforeEach((to, from, next) => {

    const authStore = useAuthStore()

    const isLoggedIn = authStore.isLoggedIn

    const role = authStore.user?.role

    // -----------------------------
    // Protected Dashboard Routes
    // -----------------------------

    // =====================================================
    // NEW
    // Authentication Check
    // =====================================================

    if (to.meta.requiresAuth && !isLoggedIn) {

        return next("/login")

    }

    // =====================================================
    // NEW
    // Role Authorization
    // =====================================================

    if (
        to.meta.role &&
        role !== to.meta.role
    ) {

        switch (role) {

            case "Admin":
                return next("/dashboard/admin")

            case "Trek Staff":
                return next("/dashboard/staff")

            case "Trekker":
                return next("/dashboard/trekker")

            default:
                return next("/")
        }

    }

    // -----------------------------
    // Prevent Login/Register
    // when already logged in
    // -----------------------------

    if (
        isLoggedIn &&
        (to.path === "/login" || to.path === "/register")
    ) {

        switch (role) {

            case "Admin":
                return next("/dashboard/admin")

            case "Trek Staff":
                return next("/dashboard/staff")

            case "Trekker":
                return next("/dashboard/trekker")

            default:
                return next("/")
        }

    }

    next()

})

export default router