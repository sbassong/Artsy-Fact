import Client from './api'

export const GetPostsByArtistId = async (artist_id) => {
  const res = await Client.get('')
  return res.data
}

export const CreatePost = async (artist_id, data) => {
  const res = await Client.post('/', data)
  return res.data
}