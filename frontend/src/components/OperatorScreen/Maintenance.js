import React from 'react'
import Style from 'styled-components'
import {views} from "../../redux/actions/operatorScreen";
import FillBillForm from "./FillBillForm";


export default ({switchToView, bills, fillUpBills}) => {
    return (
        <Wrapper>
            <Back onClick={() => switchToView(views.MAIN)}>Back</Back>
            <BillsIn>
                {bills &&
                bills.map((x, idx) => {
                    return (
                        <Bill key={idx}>
                            <div>{x.value}</div>
                            <div>{x.quantity}</div>
                        </Bill>
                    )
                })}
            </BillsIn>
            <FillBillForm onSubmit={fillUpBills} />
        </Wrapper>
    )
}

const Wrapper = Style.div`
    text-align: center;
`

const Back = Style.button`
    margin-left: -320px;
    margin-top: 20px;
    background-color: rgba(0,0,0,0);
    font-size: 22px;
    border:none;
    color: white;
    font-weight: 600;
    
    :focus {
      outline: 0;
`

const BillsIn = Style.div`
    width: 85%;
    margin: 0 auto;
    margin-top: 30px;
    display: grid;
    place-items: center;
    grid-template-columns: repeat(4, 1fr);
`

const Bill = Style.div`
    font-size: 20px;
    font-weight: 600;
    
    div {
        margin-bottom: 5px;
    }
`

