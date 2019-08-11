export const SELECT_ROLE = 'SELECT_ROLE'

export const selectRole = role => {
  return ({
    type: SELECT_ROLE,
    payload: role
  })
}


