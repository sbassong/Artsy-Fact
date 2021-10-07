import Client from './api'

export const GetPostsByArtistId = async (artist_id) => {
  const res = await Client.get('')
  return res.data
}

export const CreatePost = async (data) => {
  const res = await Client.post('/', data)
  return res.data
}

export const RemovePost = async post_id => {
  const res = await Client.delete(`/${post_id}`)
  return res.data
}