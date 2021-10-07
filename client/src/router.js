import VueRouter from 'vue-router'

import ArtistsList from './pages/ArtistsList'
import ArtistDetails from './pages/ArtistDetails'
import About from './pages/About'


const routes = [
  {path: '/artists', component: ArtistsList, name: 'ArtistsList'},
  {path: '/artists/details/:artist_id', component: ArtistDetails, name: 'ArtistDetails'},
  {path: '/about', component: About, name: 'About'}
]

export default new VueRouter({ routes, mode: 'history' })