import Client from './api'

export const CreateArtist = async data => {
  const res = await Client.post('/', data)
  return res.data
}

export const FindArtistById = async id => {
  const res = await Client.get(`/${id}`)
  return res.data
}

export const RemoveArtist = async artist_id => {
  const res = await Client.delete(`/${artist_id}`)
  return res.data
}