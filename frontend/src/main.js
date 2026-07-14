
// Vue
import { createApp } from "vue"
import { createPinia } from "pinia"

// Application
import App from "./App.vue"
import router from "./router"

// Third-Party Styles
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap.bundle.min.js"

// Application Styles
import "./assets/css/style.css"

// Application Initialization
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount("#app")

