def study_schedule(permanence_period, target_time):
    if target_time == "" or target_time.isnumeric() is False:
        return None

    counter = 0
    for period in permanence_period:
        if period[0] == period or period[1] == period:
            counter += 1
        elif period[0] < target_time and period[1] > target_time:
            counter += 1

    return counter

    raise NotImplementedError


# retorno contador
# -vv (mais detalhes do erro)
