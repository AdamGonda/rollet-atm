import React from 'react'
import { connect } from 'react-redux'
import { fieldNames } from './FillBillForm'
import MainMenu from './MainMenu'
import Transactions from './Transactions'
import Maintenance from './Maintenance'
import {
  views,
  switchToView,
  fetchTransactionHistory,
  fetchBills,
  fillUpBills
} from '../../redux/actions/operatorScreen'

const OperatorScreen = ({
  view,
  switchToView,
  transactionHistory,
  fetchTransactionHistory,
  bills,
  fetchBills,
  fillUpBills
}) => {
  React.useEffect(() => {
    fetchTransactionHistory()
    fetchBills()
    return () => switchToView(views.MAIN)
  }, [])
  return (
    <div>
      {view === views.MAIN ? (
        <MainMenu switchToView={switchToView} />
      ) : (
        <>
          {view === views.FILL_BILL ? (
            <Maintenance switchToView={switchToView} bills={bills} fillUpBills={fillUpBills} />
          ) : (
           <Transactions switchToView={switchToView} transactionHistory={transactionHistory}/>
          )}
        </>
      )}
    </div>
  )
}

const mapStateToProps = state => {
  return {
    view: state.operatorScreen.view,
    transactionHistory: state.operatorScreen.transactionHistory,
    bills: state.operatorScreen.bills
  }
}

const mapDispatchToProps = dispatch => {
  return {
    switchToView: view => dispatch(switchToView(view)),
    fetchTransactionHistory: () => dispatch(fetchTransactionHistory()),
    fetchBills: () => dispatch(fetchBills()),
    fillUpBills: v => dispatch(fillUpBills(formatForAPI(v)))
  }
}

const formatForAPI = fromData => {
  return Object.entries(fromData).map(([key, value]) => {
    switch (key) {
      case fieldNames.TWENTY_THOUSAND:
        return {value: "20000", quantity: parseInt(value)}
      case fieldNames.TEN_THOUSAND:
        return {value: "10000", quantity: parseInt(value)}
      case fieldNames.FIVE_THOUSAND:
        return {value: "5000", quantity: parseInt(value)}
      case fieldNames.TWO_THOUSAND:
        return {value: "2000", quantity: parseInt(value)}
    }
  })
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(OperatorScreen)
