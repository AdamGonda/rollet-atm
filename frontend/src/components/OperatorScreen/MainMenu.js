import React from 'react'
import Style from 'styled-components'
import {views} from "../../redux/actions/operatorScreen";


export default ({switchToView}) => {
    return (
        <Wrapper>
            <button style={{'placeSelf': 'end center'}} onClick={() => switchToView(views.HISTORY)}>
                Check history
            </button>
            <button style={{'placeSelf': 'start center'}} onClick={() => switchToView(views.FILL_BILL)}>
                Fill bills
            </button>
        </Wrapper>
    )
}

const Wrapper = Style.div`
    display: grid;
    height: 280px;
    grid-row-gap: 10px;
    
    button {
        border: none;
        background-color: var(--accent);
        color: white;
        font-size: 20px;
        font-weight: 600;
        padding: 10px 20px; 
        border-radius: 10px;
        width: 215px;
        
        :focus {
            outline: 0;
        }
    }
`
