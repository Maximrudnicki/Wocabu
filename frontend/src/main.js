import "bootstrap/dist/css/bootstrap.min.css"
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import directives from '@/directives';
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

directives.forEach(directive => {
    app.directive(directive.name, directive)
})

app.use(store).use(router, axios).mount('#app')

import "bootstrap/dist/js/bootstrap.js"
