import { SELECT_ROLE } from "../actions/app";

export const roles = {USER: 'USER', OPERATOR: 'OPERATOR'}

const initState = {
	selectedRole: roles.USER
}

export const app = (state = initState, action) => {
	switch (action.type) {
  
    case SELECT_ROLE:
      return {
        ...state,
        selectedRole: action.payload
      }
		

		default:
			return state
	}
}
