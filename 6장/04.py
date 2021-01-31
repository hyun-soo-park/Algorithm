class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        answer = ''
        answer2 = {}
        answer3 = []

        for i in paragraph:
            if i.isalpha() == True or i == ' ':
                answer = answer + i.lower()
            else:
                answer += ' '

        for i in answer.split():
            if not i in banned:
                if not i in answer2:
                    answer2[i] = 1
                else:
                    answer2[i] +=1

        for i,count in answer2.items():
            answer3.append([i,count])

        answer3 = sorted(answer3,key = lambda x:x[1])

        return answer3[-1][0]