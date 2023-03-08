def study_schedule(permanence_period, target_time):
    if target_time == " " or target_time.isnumeric() is False:
        return None

    counter = 0
    num = int(target_time)
    for period in permanence_period:
        if period[0] == num or period[1] == num:
            counter += 1
        elif period[0] < num and period[1] > num:
            counter += 1

    return counter


# -vv (mais detalhes do erro)
