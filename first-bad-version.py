# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n, last=0, first=0):
        """
        :type n: int
        :rtype: int
        """
        if(last - first == 1):
            return last
        if(n == 1 and isBadVersion(n)):
            return 1
        if(isBadVersion(n)):
            if(first == 0):
                return self.firstBadVersion(n//2, last=n, first = first)
            else:
                return self.firstBadVersion(n-(first//2), last=n, first = first)
        else:
            return self.firstBadVersion((n+last)//2, last= last, first=n)