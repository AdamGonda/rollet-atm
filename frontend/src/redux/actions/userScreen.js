import { host } from '../../config'
import { reset } from 'redux-form';
export const SET_WITDHDRAW_RESULT = 'SET_WITDHDRAW_RESULT'
export const GO_BACK = 'GO_BACK'

export const withdraw = amount => (dispatch, getState) => {
  fetch(`${host}/withdraw`,{
    method: 'POST',
    headers: {
			Accept: 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({amount})
  })
  .then(res => res.json())
  .then(json => {
    dispatch(reset('withdrawForm'))
    dispatch({type: SET_WITDHDRAW_RESULT, payload: json})
  })
  .catch(err => console.log(err))
}

export const goBack = () => ({
  type: GO_BACK
})
