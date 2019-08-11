import math


def calc_fives_tens_and_twenties(withdraw_obj, amount, bills):
    # all changeable if enough bills
    filtered_bills = [bill for bill in bills if bill.value != 2000]
    sorted_bills = sorted(filtered_bills, key=lambda x: x.value, reverse=True)
    _leftover = amount

    for bill in sorted_bills:
        if _leftover % bill.value == 0:
            # finish
            if bill.quantity > 0 and bill.quantity >= math.trunc(_leftover / bill.value):
                withdraw_obj[str(bill.value)] = math.trunc(_leftover / bill.value)
                withdraw_obj['is_success'] = True
                _leftover = 0
                break

        elif _leftover % bill.value < bill.value:
            # move to next bill
            if bill.quantity > 0 and bill.quantity >= math.trunc(_leftover / bill.value):
                withdraw_obj[str(bill.value)] = math.trunc(_leftover / bill.value)
                _leftover = _leftover % bill.value
                continue

    return withdraw_obj


def withdraw(amount, bills):
    """
    Calculates the bills to pay the costumer if possible
    when she tries to withdraw the amount

    :param amount: The amount the costumer try to withdraw
    :param bills: The bills available in the machine at the time
    :return: {is_success: boolean, bill_type_1: integer ... bill_type_n: integer}
    """
    res = get_initial_withdraw(bills)

    if amount > 10000:
        if amount % 2000 == 0:
            # even numbers

            bill_2000 = [bill for bill in bills if bill.value == 2000][0]
            is_2000_bills_deductible = True
            leftover = amount
            while leftover % 10000 != 0:

                if bill_2000.quantity >= 1:
                    leftover -= 2000
                    res['2000'] += 1
                else:
                    is_2000_bills_deductible = False
                    break

            if is_2000_bills_deductible:
                calc_fives_tens_and_twenties(res, leftover, bills)

            return res

        else:
            # odd numbers
            # and which can't be changed
            if amount % 5000 == 0:
                calc_fives_tens_and_twenties(res, amount, bills)

                return res

            else:
                bill_2000 = [bill for bill in bills if bill.value == 2000][0]
                bill_5000 = [bill for bill in bills if bill.value == 5000][0]

                if bill_5000.quantity >= 1 and bill_2000.quantity >= 1:
                    is_2000_bills_deductible = True
                    leftover = amount - 7000

                    if leftover % 2000 == 0:
                        res['5000'] = 1
                        res['2000'] = 1

                        while leftover % 10000 != 0:
                            if bill_2000.quantity >= 1:
                                leftover -= 2000
                                res['2000'] += 1
                            else:
                                is_2000_bills_deductible = False
                                break

                        if is_2000_bills_deductible:
                            calc_fives_tens_and_twenties(res, leftover, bills)

                        return res

                    else:
                        # unchangeable amount
                        return res

                return res

    else:
        bill_10000 = [bill for bill in bills if bill.value == 10000][0]
        bill_5000 = [bill for bill in bills if bill.value == 5000][0]
        bill_2000 = [bill for bill in bills if bill.value == 2000][0]

        if amount == 5000:
            if bill_5000.quantity >= 1:
                res['is_success'] = True
                res['5000'] = 1

        elif amount == 7000:
            if bill_5000.quantity >= 1 and bill_2000.quantity >= 1:
                res['is_success'] = True
                res['5000'] = 1
                res['2000'] = 1

        elif amount == 9000:
            if bill_5000 >= 1 and bill_2000 >= 2:
                res['is_success'] = True
                res['5000'] = 1
                res['2000'] = 2

        elif amount == 10000:
            if bill_10000.quantity >= 1:
                res['is_success'] = True
                res['10000'] = 1

            elif bill_5000.quantity >= 2:
                res['is_success'] = True
                res['5000'] = 2

        elif amount % 2000 == 0:
            if bill_2000.quantity >= amount / 2000:
                res['is_success'] = True
                res['2000'] = amount / 2000

        return res


def get_initial_withdraw(bills):
    initial_withdraw = {'is_success': False}

    for bill in bills:
        initial_withdraw[str(bill.value)] = 0

    return initial_withdraw
