import { createRouter, createWebHistory } from 'vue-router'
import Words from '@/components/Words.vue'
import Groups from '@/components/Groups.vue'
import GroupDetails from '@/components/GroupDetails.vue'
import StudentGroupDetails from '@/components/StudentGroupDetails.vue'
import StudentDetails from '@/components/StudentDetails.vue'
import StudentDetailsStudent from '@/components/StudentDetailsStudent.vue'
import WordDetails from '@/components/modals/WordDetails.vue'
import Training from '@/components/trainings/Training.vue'
import AllTogether from '@/components/trainings/AllTogether.vue'
import WordTranslate from '@/components/trainings/WordTranslate.vue'
import WordAudio from '@/components/trainings/WordAudio.vue'
import Constructor from '@/components/trainings/Constructor.vue'
import Cards from '@/components/trainings/Cards.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'

const routes = [
  {
    path: '/',
    name: 'words',
    component: Words
  },
  {
    path: '/groups',
    name: 'groups',
    component: Groups
  },
  {
    path: '/groups/:id',
    name: 'group-details',
    component: GroupDetails
  },
  {
    path: '/groups/student/:id',
    name: 'student-group-details',
    component: StudentGroupDetails
  },
  {
    path: '/groups/:id/:student',
    name: 'student-details',
    component: StudentDetails
  },
  {
    path: '/groups/student/:id/:student',
    name: 'student-details-student',
    component: StudentDetailsStudent
  },
  {
    path: '/words/:id',
    name: 'word-details',
    component: WordDetails
  },
  {
    path: '/training',
    name: 'training',
    component: Training
  },
  {
    path: '/training/all-together',
    name: 'all-together',
    component: AllTogether
  },
  {
    path: '/training/word-translate',
    name: 'word-translate',
    component: WordTranslate
  },
  {
    path: '/training/constructor',
    name: 'constructor',
    component: Constructor
  },
  {
    path: '/training/cards',
    name: 'cards',
    component: Cards
  },
  {
    path: '/training/word-audio',
    name: 'word-audio',
    component: WordAudio
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
