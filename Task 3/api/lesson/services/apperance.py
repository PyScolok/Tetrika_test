def apperance(intervals):
    # create array from intervals dict
    timestamps = form_timestamps_list(intervals)
    lesson_is_started = False
    tutor_at_lesson = False
    pupil_at_lesson = False
    total_time = 0

    # Iterate over the array and, upon meeting the timestamp,
    # change the state of the corresponding subject.
    # Under a certain condition, change the total time spent in the lesson.
    for t in timestamps:
        if t in intervals['lesson']:
            lesson_is_started = not lesson_is_started
            if not lesson_is_started:
                break # lesson end
        elif t in intervals['tutor']:
            tutor_at_lesson = not tutor_at_lesson
            if tutor_at_lesson and pupil_at_lesson and lesson_is_started:
                total_time += t
            elif not tutor_at_lesson and pupil_at_lesson and lesson_is_started:
                total_time -= t
        elif t in intervals['pupil']:
            pupil_at_lesson = not pupil_at_lesson
            if tutor_at_lesson and pupil_at_lesson and lesson_is_started:
                total_time += t
            elif tutor_at_lesson and not pupil_at_lesson and lesson_is_started:
                total_time -= t
    return abs(total_time)


def form_timestamps_list(intervals):
    timestamps = []
    for i in intervals.keys():
        for j in intervals[i]:
            timestamps.append(j)
    timestamps.sort()
    return timestamps