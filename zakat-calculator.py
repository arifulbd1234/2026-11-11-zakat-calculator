# Day 36 - 2026-11-11 - Zakat Calculator
# Zakat hisab kore: tomar sompod nisab er upore gele 2.5% zakat dite hoy.
# Jara Muslim tader jonno proti bochor zakat ber kora shohoj kore dey.
# Cash, bank balance, gold, silver, business er mal - shob miliye hisab kore.

# Nisab: 85 gram gold ba 595 gram silver er damer soman sompod thakle zakat farz hoy.
GOLD_NISAB_GRAMS = 85
SILVER_NISAB_GRAMS = 595
ZAKAT_RATE = 0.025  # 2.5%


def nisab_amount(gold_price_per_gram, silver_price_per_gram):
    """Gold o silver er bortoman dam diye nisab ber kore (jeta kom, setai nisab)."""
    gold_nisab = GOLD_NISAB_GRAMS * gold_price_per_gram
    silver_nisab = SILVER_NISAB_GRAMS * silver_price_per_gram
    return min(gold_nisab, silver_nisab)


def total_zakatable_wealth(cash, bank_balance, gold_grams, gold_price_per_gram,
                           silver_grams, silver_price_per_gram,
                           business_goods_value, money_lent_out, debts):
    """Shob zakat-joggo sompod jog kore rin bad diye mot sompod ber kore."""
    gold_value = gold_grams * gold_price_per_gram
    silver_value = silver_grams * silver_price_per_gram
    total = (cash + bank_balance + gold_value + silver_value
             + business_goods_value + money_lent_out)
    return total - debts


def calculate_zakat(cash=0, bank_balance=0, gold_grams=0, gold_price_per_gram=0,
                    silver_grams=0, silver_price_per_gram=0,
                    business_goods_value=0, money_lent_out=0, debts=0):
    """Mot sompod, nisab ar zakat er poriman soho ekta summary dey."""
    nisab = nisab_amount(gold_price_per_gram, silver_price_per_gram)
    wealth = total_zakatable_wealth(
        cash, bank_balance, gold_grams, gold_price_per_gram,
        silver_grams, silver_price_per_gram,
        business_goods_value, money_lent_out, debts)
    zakat_due = wealth >= nisab
    zakat_amount = round(wealth * ZAKAT_RATE, 2) if zakat_due else 0
    return {
        "mot_sompod": round(wealth, 2),
        "nisab": round(nisab, 2),
        "zakat_farz": zakat_due,
        "zakat_poriman": zakat_amount,
    }


def print_zakat_summary(result):
    """Hisab ta sundor kore dekhay."""
    print(f"Mot zakat-joggo sompod: {result['mot_sompod']:,.2f} taka")
    print(f"Nisab (sorbonimno seema): {result['nisab']:,.2f} taka")
    if result["zakat_farz"]:
        print(f"Zakat farz hoyeche! Dite hobe: {result['zakat_poriman']:,.2f} taka (2.5%)")
    else:
        print("Zakat farz hoy ni - sompod ekhono nisab er niche ache.")


if __name__ == "__main__":
    # Example 1: Shudhu bank balance ar cash ache, gold nai
    print("Example 1: Cash + bank balance")
    result1 = calculate_zakat(
        cash=50000, bank_balance=300000, debts=20000,
        gold_price_per_gram=14000, silver_price_per_gram=180)
    print_zakat_summary(result1)

    # Example 2: Gold ache, kintu sompod kom - zakat farz hobe na
    print("\nExample 2: Olpo gold, kom sompod")
    result2 = calculate_zakat(
        cash=10000, gold_grams=2, gold_price_per_gram=14000,
        silver_price_per_gram=180)
    print_zakat_summary(result2)

    # Example 3: Business er mal + gold + cash - zakat ber kora
    print("\nExample 3: Business + gold + cash")
    result3 = calculate_zakat(
        cash=100000, bank_balance=500000, gold_grams=10,
        gold_price_per_gram=14000, silver_grams=50,
        silver_price_per_gram=180, business_goods_value=400000,
        money_lent_out=50000, debts=100000)
    print_zakat_summary(result3)
