import atm_controller


class StubBill(object):
    def __init__(self, id, type, quantity):
        self.id = id
        self.value = type
        self.quantity = quantity


# >> enough money <<-------------------------

# not bigger than 10 000 [ changeable amount ]
def test_withdraw_2000():
    amount = 2000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 1


def test_withdraw_5000():
    amount = 5000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 1
    assert res['2000'] == 0


def test_withdraw_7000():
    amount = 7000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 1
    assert res['2000'] == 1


def test_withdraw_10000():
    amount = 10000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 1
    assert res['5000'] == 0
    assert res['2000'] == 0


# not bigger than 10 000 [ unchangeable amount ]
def test_withdraw_1000():
    amount = 1000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_3000():
    amount = 3000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_1001():
    amount = 1001
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_2100():
    amount = 2100
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_5100():
    amount = 5100
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_900():
    amount = 900
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


# bigger than 10 000

# odd [ changeable amount ]
def test_withdraw_23000():
    amount = 23000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 1
    assert res['5000'] == 1
    assert res['2000'] == 4


def test_withdraw_13000():
    amount = 13000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 1
    assert res['2000'] == 4


def test_withdraw_15000():
    amount = 15000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 1
    assert res['5000'] == 1
    assert res['2000'] == 0


def test_withdraw_29000():
    amount = 29000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 1
    assert res['10000'] == 0
    assert res['5000'] == 1
    assert res['2000'] == 2


def test_withdraw_159000():
    amount = 159000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 7
    assert res['10000'] == 1
    assert res['5000'] == 1
    assert res['2000'] == 2


# odd [ unchangeable amount ]
def test_withdraw_17300():
    amount = 17300
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_523030():
    amount = 523030
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_15200():
    amount = 15200
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


# even [ changeable amount ]
def test_withdraw_22000():
    amount = 22000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 1
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 1


def test_withdraw_48000():
    amount = 48000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 2
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 4


def test_withdraw_284000():
    amount = 284000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 14),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 14
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 2


def test_withdraw_88000():
    amount = 88000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 4
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 4


# even [ unchangeable amount ]
def test_withdraw_88001():
    amount = 88001
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_10001():
    amount = 10001
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_20500():
    amount = 20500
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_41030():
    amount = 41030
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


# >> not enough money <<-------------------------

# not bigger than 10 000 [ changeable amount ]

def test_withdraw_2000():
    amount = 2000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 0),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_5000():
    amount = 5000
    stub_bills = [
        StubBill(3, 5000, 0),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_8000():
    amount = 8000
    stub_bills = [
        StubBill(3, 5000, 0),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 3),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_10000():
    amount = 10000
    stub_bills = [
        StubBill(3, 5000, 0),
        StubBill(5, 10000, 0),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


# bigger than 10 000 [ changeable amount ]
def test_withdraw_12000_not_enough_2000():
    amount = 12000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 0),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_12000_not_enough_10000():
    amount = 12000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 0),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 2
    assert res['2000'] == 1


def test_withdraw_15000_not_enough_5000():
    amount = 15000
    stub_bills = [
        StubBill(3, 5000, 0),
        StubBill(5, 10000, 10),
        StubBill(1, 20000, 10),
        StubBill(4, 2000, 10),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 1
    assert res['5000'] == 0
    assert res['2000'] == 0


def test_withdraw_25000_not_enough_10000_and_20000():
    amount = 25000
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 0),
        StubBill(1, 20000, 0),
        StubBill(4, 2000, 0),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == True
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 5
    assert res['2000'] == 0


# bigger then 10 000 [ unchangeable ]
def test_withdraw_25200():
    amount = 25200
    stub_bills = [
        StubBill(3, 5000, 10),
        StubBill(5, 10000, 0),
        StubBill(1, 20000, 0),
        StubBill(4, 2000, 0),
    ]

    res = atm_controller.withdraw(amount, stub_bills)

    assert res['is_success'] == False
    assert res['20000'] == 0
    assert res['10000'] == 0
    assert res['5000'] == 0
    assert res['2000'] == 0