def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return

    counter = 0

    for start_time, end_time in permanence_period:
        if not (isinstance(start_time, int) and isinstance(end_time, int)):
            return

        if start_time <= target_time <= end_time:
            counter += 1

    return counter
