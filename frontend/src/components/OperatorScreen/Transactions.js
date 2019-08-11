import React from 'react'
import Style from 'styled-components'
import {views} from "../../redux/actions/operatorScreen";


export default ({switchToView, transactionHistory}) => {
    return (
        <Wrapper>
            <button onClick={() => switchToView(views.MAIN)}>Back</button>
            <h3>Transactions</h3>
            <Transactions style={{ marginLeft: 250 }}>
                {transactionHistory &&
                transactionHistory.map((x, idx) => {
                    return (
                        <Transaction key={idx}>
                            <div>{x.time.slice(4, x.time.length - 4)}</div>
                            <div>{x.amount}</div>
                            <div>{x.success_status}</div>
                        </Transaction>
                    )
                })}
            </Transactions>
        </Wrapper>
    )
}

const Wrapper = Style.div`
    text-align: center;
    
    h3 {
        font-size: 30px;
        margin: 25px 0 20px 0;
        place-self: center;
      }
    
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
    
`

const Transactions = Style.div`
    display:grid;
    overflow: scroll;
    height: 145px;
    margin: 0 !important; 
    padding: 0 25px;
  } 
`

const Transaction = Style.div`
    display: flex;
    justify-content: space-between;
    align-items: center;
    
    background-color: white;
    border-radius: 5px;
    height: 42px;
    color: var(--transaction-text-color);
    margin-bottom: 7px;
    padding: 0 20px;
    font-weight: 600;
`
