import { applyMiddleware, createStore } from 'redux'
import reducer from './reducer'
import loggingMiddleware from 'redux-logger'
import thunkMiddleware from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'

export default createStore(reducer, composeWithDevTools(applyMiddleware( thunkMiddleware, loggingMiddleware)))

export * from './reducer'
