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


if __name__ == '__name__':
    interval = { 
        'lesson': [1594663200, 1594666800], 
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473] 
    }

    print(apperance(interval))