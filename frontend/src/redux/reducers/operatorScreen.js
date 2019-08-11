import { views, SWITCH_TO_VIEW, SET_TRANSACTIONS, SET_BILLS } from '../actions/operatorScreen'

const initState = {
  view: views.MAIN,
  transactionHistory: [],
  bills: []
}

export const operatorScreen = (state = initState, action) => {
  switch (action.type) {
    
    case SWITCH_TO_VIEW:
      return {
        ...state,
        view: action.payload
      }

    case SET_TRANSACTIONS:
      return {
        ...state,
        transactionHistory: action.payload.transactions
      }

    case SET_BILLS:
      return {
        ...state,
        bills: action.payload.bills
      }

    default:
      return state
  }
}
