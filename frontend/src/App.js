import React from 'react'
import { connect } from 'react-redux'
import { selectRole } from './redux/actions/app'
import { roles } from './redux/reducers/app'
import UserScreen from './components/UserScreen/UserScreen'
import OperatorScreen from './components/OperatorScreen/OperatorScreen'
import rolletShape from './images/rollet_shape.svg'
import Style from 'styled-components'

const App = ({ selectedRole, selectRole }) => {
  return (
    <>
      <img id="background-shape" src={rolletShape} />
      <Wrapper>
        <Description>
          <h1>Rollet Atm</h1>
          <p>
            This is a homework project <br/>  for the company Rollet <br/> who  will
            revolutionize parking. 
          </p>
          <p>My task was to develop a  <br/> note dispenser logic <br/>  of an ATM. </p>
        </Description>
        <Atm>
          <RoleChooser>
            <UserRoleBtn selected={selectedRole === roles.USER ? 'selected' : null} onClick={() => selectRole(roles.USER)}>User</UserRoleBtn>
            <OperatorRoleBtn selected={selectedRole === roles.OPERATOR ? 'selected' : null} onClick={() => selectRole(roles.OPERATOR)}>Operator</OperatorRoleBtn>
          </RoleChooser>

          <Screen>
            {selectedRole === roles.USER ? <UserScreen/> : <OperatorScreen/>}
          </Screen>
        </Atm>
      </Wrapper>
    </>
  )
}

const mapStateToProps = state => {
  return {
    selectedRole: state.app.selectedRole
  }
}

const mapDispatchToProps = dispatch => {
  return {
    selectRole: role => dispatch(selectRole(role))
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App)

const Wrapper = Style.div`
  display: grid;
  grid-template-columns: repeat(2, 1fr);
`
const Description = Style.div`
  grid-column: 1;
  width: 37vw;
  
  h1 {
    font-size: 37px;
  }
  
  p {
    font-size: 33px;
  }
  
`

const Atm = Style.div`
  display: grid;
  place-items: start;

  grid-column: 2;
`

const RoleChooser = Style.div`
  margin-left: -15px;
  place-self: center center;
  width:30vw;
  display:grid;
  grid-template-columns: 1.2fr 1fr;
  grid-column-gap: 20px;
  place-self: center start;
  place-items: center;
  height: 50px;
`

const RoleButton = Style.button`
  font-weight: 600;
  background-color: rgba(0,0,0,0);
  border:none;
  box-shadow: ${props => props.selected ? 'inset 0px 0px 0px 3px #fff' : 'none'};
  border-radius: 50px;
  font-size: 22px;
  color:white;
  padding: 5px 20px;
  
  :focus {
    outline: 0;
  }
`

const UserRoleBtn = Style(RoleButton)`
  place-self: center end;
`

const OperatorRoleBtn = Style(RoleButton)`
  place-self: center start;
`

const Screen = Style.div`
  border: 3px solid white;
  border-radius: 10px;
  width:30vw;
  height:20vw;
`
