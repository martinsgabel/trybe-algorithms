def study_schedule(permanence_period, target_time):
    if not target_time or type(target_time) != int:
        return None

    counter = 0
    num = int(target_time)
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if period[0] <= num and period[1] >= num:
            counter += 1

    return counter


# -vv (mais detalhes do erro)
