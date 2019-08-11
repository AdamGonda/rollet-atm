from flask import request
from flask import Flask
from data.models import Bill, Transaction, get_db_url, db, SUCCESS, FAILURE
import atm_controller
from datetime import datetime
from flask_cors import CORS
from sqlalchemy import desc


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_db_url()
db.init_app(app)
CORS(app)


def add_transaction_to_db_session(time, amount, is_success, db):
    transaction = Transaction()
    transaction.time = time
    transaction.success_status = is_success
    transaction.amount = amount
    db.session.add(transaction)


def convert_bills_to_dicts(bills):
    res = []

    for bill in bills:
        _bill = {
            'id': bill.id,
            'value': bill.value,
            'quantity': bill.quantity,
        }
        res.append(_bill)

    return res


def convert_transactions_to_dicts(transactions):
    res = []

    for transaction in transactions:
        _transaction = {
            'id': transaction.id,
            'time': transaction.time,
            'success_status': transaction.success_status,
            'amount': transaction.amount,
        }
        res.append(_transaction)

    return res



@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == "POST":
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        amount = int(request.json['amount'])
        bills = Bill.query.all()
        withdraw_action = atm_controller.withdraw(amount, bills)

        if withdraw_action['is_success']:
            for key, value in withdraw_action.items():
                if str(key).isdigit():
                    bill = [bill for bill in bills if bill.value == int(key)][0]
                    bill.quantity = bill.quantity - value

            add_transaction_to_db_session(time, amount, SUCCESS, db)
            db.session.commit()
            return withdraw_action

        else:
            add_transaction_to_db_session(time, amount, FAILURE, db)
            db.session.commit()
            return withdraw_action


@app.route('/fill_up_bills', methods=['GET', 'POST'])
def fill_up_bills():
    if request.method == "POST":
        bills = request.json['bills']
        for bill in bills:
            db_bill = Bill.query.filter_by(value=bill['value']).first()
            db_bill.quantity = db_bill.quantity + bill['quantity']

        db.session.commit()
        return '200'


@app.route('/bills')
def get_bills():
    bills = Bill.query.order_by((Bill.id))
    return {'bills': convert_bills_to_dicts(bills)}


@app.route('/transactions')
def get_transactions():
    transactions = Transaction.query.order_by(desc(Transaction.time))
    return {'transactions': convert_transactions_to_dicts(transactions)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
