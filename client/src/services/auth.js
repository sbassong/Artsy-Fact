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

// // Does this have a purpose here?
// export const CheckSession = async () => {
//   try {
//     const res = await Client.get('users/session')
//     return res.data
//   } catch (error) {
//     throw error
//   }
// }
