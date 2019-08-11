import React from 'react'
import {connect} from 'react-redux'
import WithdrawForm from './WithdrawForm'
import {withdraw, goBack} from '../../redux/actions/userScreen'
import Style from 'styled-components'

const UserScreen = ({withdrawResult, withdraw, goBack}) => {
    const errMsg = `No bills to pay.`

    React.useEffect(() => {
        return () => goBack()
    }, [])

    return (
        <Wrapper>
            {withdrawResult == null ? (
                <>
                    <h2>Withdraw money</h2>
                    <WithdrawForm onSubmit={withdraw}/>
                </>
            ) : (
                <WithdrawResult>
                    {withdrawResult && withdrawResult.is_success ? (
                        <div style={{'textAlign': 'center'}}>
                            <button onClick={goBack}>Back</button>
                            <h3>Bills</h3>
                            <Bills>
                                {Object.entries(withdrawResult)
                                    .filter(([key, value]) => Number(key))
                                    .map(([bill, quantity]) => ({bill, quantity}))
                                    .map((x, idx) => (
                                        <div key={idx}>
                                            <span>{x.bill}</span>
                                            <span>x</span>
                                            <span>{x.quantity}</span>
                                        </div>
                                    ))}
                            </Bills>

                        </div>
                    ) : (

                        <ErrorMsg>
                            <button onClick={goBack}>Back</button>
                            <p>{errMsg}</p>
                        </ErrorMsg>
                    )}
                </WithdrawResult>
            )}
        </Wrapper>
    )
}

const mapStateToProps = state => {
    return {
        withdrawResult: state.userScreen.withdrawResult
    }
}

const mapDispatchToProps = dispatch => {
    return {
        withdraw: v => dispatch(withdraw(v.amount)),
        goBack: () => dispatch(goBack())
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(UserScreen)

const Wrapper = Style.div`
  display: grid;
  grid-template-rows: 0.9fr 2fr;
  width: 100%;
  height: 100%;
  grid-row-gap: 25px;
  
  h2 {
    margin: 0;
    place-self: end center;
    font-size: 28px;
    
  }
  
`

const WithdrawResult = Style.div`
  display: grid;
  grid-template-rows: 0.9fr 2fr;
  place-items: center center;
  
  button {
    margin-left: -320px;
    margin-top: 20px;
    background-color: rgba(0,0,0,0);
    font-size: 22px;
    border:none;
    color: white;
    font-weight: 600;
    
    :focus {
      outline: 0;
    }
  }
  
  h3 {
    font-size: 25px;
    margin: 25px 0 35px 0;
    place-self: center;
  }
`

const Bills = Style.div`
    display: grid;
    width: 370px;
    
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-row-gap: 30px;
    
    div {
        font-size: 23px;
        font-weight: 600;
        
        span {
            margin: 0 7px;
        }
    }
`


const ErrorMsg = Style.div`  
  p {
    margin-top: 65px;
    font-size: 35px;
    font-weight: 600;
  }
  
  button {
    margin-left: -60px;
  }
`
