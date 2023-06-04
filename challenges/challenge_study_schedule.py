def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    counter = 0
    for periods in permanence_period:
        (entry_time, exit_time) = periods
        if not isinstance(entry_time, int) or not isinstance(exit_time, int):
            return None
        if entry_time <= target_time and exit_time >= target_time:
            counter += 1
    return counter
