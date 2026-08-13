from atm import ATM


def test_initial_balance():
    atm = ATM(1000)
    assert atm.check_balance() == 1000


def test_deposit():
    atm = ATM(1000)
    atm.deposit(500)
    assert atm.check_balance() == 1500


def test_withdraw():
    atm = ATM(1000)
    atm.withdraw(300)
    assert atm.check_balance() == 700


def test_insufficient_funds():
    atm = ATM(1000)

    try:
        atm.withdraw(1500)
        assert False
    except ValueError:
        assert True


def test_negative_deposit():
    atm = ATM(1000)

    try:
        atm.deposit(-100)
        assert False
    except ValueError:
        assert True


def test_negative_withdraw():
    atm = ATM(1000)

    try:
        atm.withdraw(-100)
        assert False
    except ValueError:
        assert True


if __name__ == "__main__":
    test_initial_balance()
    test_deposit()
    test_withdraw()
    test_insufficient_funds()
    test_negative_deposit()
    test_negative_withdraw()

    print("Todas las pruebas fueron exitosas.")