def calc_total(bill, tip_percent):
    tip = bill * tip_percent / 100
    return bill + tip


def main():
    bill = float(input("bill: "))
    pct = float(input("tip %: "))
    print(f"total = {calc_total(bill, pct)}")


if __name__ == "__main__":
    main()
def calc_total(bill, tip_percent):
    return bill + bill * tip_percent / 100


def main():
    bill = float(input("bill: "))
    pct = float(input("tip %: "))
    print(f"total = {calc_total(bill, pct)}")


if __name__ == "__main__":
    main()
def calc_total(bill, tip_percent):
    return bill + bill * tip_percent / 100


def main():
    bill = float(input("bill: "))
    pct = float(input("tip %: "))
    total = calc_total(bill, pct)
    print(f"total = {total}")

    # إضافة شرط تحكم في التدفق (if)
    if total > 200:
        print("generous tip!")


if __name__ == "__main__":
    main()
