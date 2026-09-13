import sys
from collections import *


def solve(m,n,grid):
	dp=[[-1]*n for _ in range(m)]
	def helper(i,j):
		if i==m-1:
			return grid[i][j]
		if dp[i][j]!=-1:
			return dp[i][j]
		ans=float('-inf')
		for dj in [1,-1]:
			nj=j+dj
			if 0<=nj<n:
				ans=max(ans,grid[i][j]+helper(i+1,nj))	
		dp[i][j]=ans
		return ans
	ans=float('-inf')
	for j in range(n):
		ans=max(ans,helper(0,j))
	return ans


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	m,n=map(int,input().split())
	grid=[]
	for _ in range(m):
		temp=list(map(int,input().split()))
		grid.append(temp)
	print(solve(m,n,grid))


if __name__=="__main__":
	main()