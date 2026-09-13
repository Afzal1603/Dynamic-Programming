import sys
from collections import *

def solve(m,n):
	dp=[[-1]*n for _ in range(m)]
	def helper(i,j):
		if i==m-1 and j==n-1:
			return 1
		if dp[i][j]!=-1:
			return dp[i][j]
		right=0
		down=0
		if i+1<m:
			down=helper(i+1,j)
		if j+1<n:
			right=helper(i,j+1)
		dp[i][j]=right+down
		return dp[i][j]
	return helper(0,0)


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	m,n=map(int,input().split())
	print(solve(m,n))



if __name__=="__main__":
	main()