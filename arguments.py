# convert eur to usd with given rate, otherwise use default
def eur_to_usd(amount, rate=0.846354):
    return amount / rate


# convert a list of amounts with given rate, otherwise use default, then sum
def convert_and_sum(amounts, **kwargs):

    # init sum
    sum = 0

    for amount in amounts:
        sum += eur_to_usd(amount, **kwargs)

    return sum

print(eur_to_usd(1))
print(eur_to_usd(1, rate=0.5))
print(convert_and_sum([1, 3]))
print(convert_and_sum([1, 3], rate=0.5))
