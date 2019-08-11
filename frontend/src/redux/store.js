import { compose, createStore, combineReducers, applyMiddleware } from 'redux'
import { app } from './reducers/app'
import thunk from 'redux-thunk'
import { userScreen } from './reducers/userScreen'
import { operatorScreen } from './reducers/operatorScreen'
import { reducer as formReducer } from 'redux-form'

const rootReducer = combineReducers({
	app,
	userScreen,
	operatorScreen,
	form: formReducer
})

const enhancer = compose(
	applyMiddleware(thunk),
	window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

export default createStore(rootReducer, enhancer)
