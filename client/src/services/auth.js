import Client from './api'

export const SignInUser = async (data) => {
  try {
    const res = await Client.post('users/login', data)
    localStorage.setItem('token', res.data.token)
    return res.data.user
  } catch (error) {
    throw error
  }
}

export const SignUpUser = async (data) => {
  try {
    const res = await Client.post('users/signup', data)
    return res.data
  } catch (error) {
    throw error
  }
}

export const CheckSession = async () => {
  try {
    const res = await Client.get('users/session')
    return res.data
  } catch (error) {
    throw error
  }
}
