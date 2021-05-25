class Solution:
    def isValid(self, s: str):
        st=[-1]
        dic={'(':')','{':'}','[':']',-1:None}
        for i in s:
            if i in dic:st.append(i)
            elif i != dic[st.pop()]:return False 
        return len(st)==1
p1=Solution()
print(p1.isValid('()'))
