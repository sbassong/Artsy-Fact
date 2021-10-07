import Client from './api'

export const GetArtists = async () => {
  const res = await Client.get(`/artists`)
  return res.data
}

export const GetArtistById = async id => {
  const res = await Client.get(`/artists/${id}`)
  return res.data
}
