class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsGrph = {}

        for pre in prerequisites:
            if pre[1] in crsGrph:
                crsGrph[pre[1]].append(pre[0])
            else:
                crsGrph[pre[1]] = [pre[0]]

        vstd = set()

        for crs in range(numCourses):
            if not self.crsScdule(crs, vstd, crsGrph):
                return False
        return True


    def crsScdule(self, crs, vstd, crsGrph):
        if crs in vstd:
            return False
        
        if crs not in crsGrph:
            return True

        vstd.add(crs)

        for pre in crsGrph[crs]:
            if not self.crsScdule(pre, vstd, crsGrph):
                return False

        vstd.remove(crs)

        crsGrph[crs] = []

        return True