class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []

        for i in logs:
            if i.split()[1].isdigit() == True:
                nums.append(i)

        for i in nums:
            logs.remove(i)

        logs = sorted(logs, key=lambda x: (x.split()[1:], x.split()[0]))

        logs.extend(nums)

        return logs