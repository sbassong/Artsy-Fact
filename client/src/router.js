import VueRouter from 'vue-router'

import ArtistsList from './pages/ArtistsList'
import ArtistDetails from './pages/ArtistDetails'
import About from './pages/About'
import Home from './pages/Home'
import LoginForm from './components/LoginForm'
import RegisterForm from './components/RegisterForm'


const routes = [
  {path: '/', component: Home, name: 'Home'},
  {path: '/artists', component: ArtistsList, name: 'ArtistsList'},
  {path: '/artists/details/:artist_id', component: ArtistDetails, name: 'ArtistDetails'},
  {path: '/about', component: About, name: 'About'},
  {path: '/users/login', component: LoginForm, name: 'LoginForm'},
  {path: '/users/register', component: RegisterForm, name: 'RegisterForm'}
]

export default new VueRouter({ routes, mode: 'history' })