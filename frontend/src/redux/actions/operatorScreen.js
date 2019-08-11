import { host } from '../../config'
import { reset } from 'redux-form';

export const views = {MAIN: 'MAIN', FILL_BILL: 'FILL_BILL', HISTORY: 'HISTORY'}
export const SWITCH_TO_VIEW = 'SWITCH_TO_VIEW'
export const SET_TRANSACTIONS = 'SET_TRANSACTIONS'
export const SET_BILLS = 'SET_BILLS'

export const switchToView = view => ({
  type: SWITCH_TO_VIEW,
  payload: view
})

export const fetchTransactionHistory = () => (dispatch, getState) => {
  fetch(`${host}/transactions`)
  .then(res => res.json())
  .then(json => {
    dispatch({type: SET_TRANSACTIONS, payload: json})
  })
  .catch(err => console.log(err))
}

export const fetchBills = () => (dispatch, getState) => {
  fetch(`${host}/bills`)
  .then(res => res.json())
  .then(json => {
    dispatch({type: SET_BILLS, payload: json})
  })
  .catch(err => console.log(err))
}

export const fillUpBills = bills => (dispatch, getState) => {
  fetch(`${host}/fill_up_bills`,{
    method: 'POST',
    headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({bills})
  })
  .then(res => res.json())
  .then(json => {
    dispatch(reset('fillBillForm'))
    dispatch(fetchBills())
  })
  .catch(err => console.log(err))
}

