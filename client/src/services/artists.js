import Client from './api'

export const GetArtists = async => {
  const res = await Client.get(`/`)
  return res.data
}

export const GetArtistById = async id => {
  const res = await Client.get(`/${id}`)
  return res.data
}
