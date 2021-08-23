def solution(table, languages, preference):
    answer = ''
    job = ['SI', 'CONTENTS', 'HARDWARE', 'PORTAL', 'GAME']

    if len(languages) == 1:
        return languages[0]
    else:
        scores = []

        for t in table:
            split_table = t.split(" ")
            tmp_score = 0

            for i in range(len(languages)):
                if languages[i] in split_table:
                    tmp_score += (6 - split_table.index(languages[i])) * preference[i]

            scores.append(tmp_score)

        max_score = max(scores)
        jobs = []

        while max_score in scores:
            jobs.append(job[scores.index(max_score)])
            scores[scores.index(max_score)] = 0

        jobs = sorted(jobs)

        return jobs[0]