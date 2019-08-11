import { SET_WITDHDRAW_RESULT, GO_BACK } from '../actions/userScreen'

const initState = {
	withdrawResult: null
}

export const userScreen = (state = initState, action) => {
  switch (action.type) {
    case SET_WITDHDRAW_RESULT:
      return {
        ...state,
        withdrawResult: action.payload
			}
			
		case GO_BACK:
			return {
				...state,
				withdrawResult: null
			}

    default:
      return state
  }
}
