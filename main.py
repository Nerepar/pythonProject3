from listrandom import ListRandom

if __name__ == '__main__':
    inn = ListRandom(start=1, end=6)

    print(inn.all_digit_is_odd)
    print(inn.digits_more(5))
    inn.print_list()
    inn.all_digit_is_max()
    inn.all_digit_is_min()
    inn.all_digit_is_sred()
