class Solution:
    def topStudents(self, positives: List[str], negatives: List[str], reports: List[str], student_id: List[int], k: int) -> List[int]:
        student = [[0,student_id[i]] for i in range(len(student_id))]
        positives = set(positives)
        negatives = set(negatives)
        for i,report in enumerate(reports):
            words = report.split(' ')
            for word in words:
                if word in positives:
                    student[i][0] += 3
                if word in negatives:
                    student[i][0] -= 1
        student = sorted(student,key = lambda key : (-key[0],key[1]))
        # print(student)
        return [student[i][1] for i in range(k)]
                    