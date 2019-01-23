import axios from 'axios'
//ACTION TYPES
const GOT_USER_DATA = 'GOT_USER_DATA'

//ACTION CREATORS
const gotUserData = (userData) => {
  return {
    type: GOT_USER_DATA,
    avatar: userData.avatar,
    fullname: userData.fullname,
    username: userData.username
  }
}

//THUNK CREATORS
export const gettingUserData = (searchUser) => {
  return async function (dispatch) {
    let response = await axios.get(`/${searchUser}`, searchUser);
    console.log(response)
    console.log(typeof response.data)
    console.log(response.data.avatar)
    dispatch(gotUserData(response.data))
  }
}

const initialState = {
  fullname: '',
  username: '',
  avatar: ''
}


export default function(state = initialState, action) {
  const newState = {...state}
  switch (action.type) {
    case GOT_USER_DATA:
      newState.username = action.username;
      newState.fullname = action.fullname;
      newState.avatar = action.avatar;
      return newState
    default:
      return state;
  }
}
