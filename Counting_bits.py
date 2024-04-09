class Solution(object):
    def countBits(self, n):
      #T(C(N))=O(N) and S(C(N)=O(N) it requires non contigous memeory allocation iteratively
        out=[0]#initilazing output list
        while (len(out)<=n):#iterating to output's length
            out.extend([i+1 for i in out])#extendign the output's binary form bits 
            
        return out[:n+1]#printing the output
