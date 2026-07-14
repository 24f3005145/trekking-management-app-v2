import { defineStore } from "pinia"

// =====================================================
// Global Toast Store
// =====================================================

export const useToastStore = defineStore("toast", {

    state: () => ({

        show: false,

        message: "",

        type: "success",

        timeoutId: null

    }),

    actions: {

        // -------------------------------------------------
        // Display a toast notification.
        // -------------------------------------------------

        trigger(message, type = "success") {

            // -------------------------------------------------
            // NEW: Clear previous timeout if another toast
            // is triggered before the current one disappears.
            // -------------------------------------------------

            if (this.timeoutId) {

                clearTimeout(this.timeoutId)

            }

            this.message = message

            this.type = type

            this.show = true

            this.timeoutId = setTimeout(() => {

                this.show = false

                this.timeoutId = null

            }, 3000)

        }

    }

})