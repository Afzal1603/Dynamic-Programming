import sys
from collections import *


def solve(m,n,grid):
	dp=[[-1]*n for _ in range(m)]
	def helper(i,j):
		if i==m-1 and j==n-1:
			return grid[i][j]
		if dp[i][j]!=-1:
			return dp[i][j]
		right=float('inf')
		down=float('inf')
		if i+1<m:
			down=helper(i+1,j)
		if j+1<n:
			right=helper(i,j+1)
		dp[i][j]=grid[i][j]+min(down,right)
		return dp[i][j]
	return helper(0,0)


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