import Client from './api'

export const LoginUser = async (data) => {
    const res = await Client.post('users/login', data)
    localStorage.setItem('token', res.data.token)
    return res.data.user
}

export const RegisterUser = async (data) => {
    const res = await Client.post('users/register', data)
    return res.data
}

export const CheckSession = async () => {
    const res = await Client.get('users/login')
    return res.data
  
}
