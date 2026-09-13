import sys
from collections import *

def solve(s):
	n=len(s)
	dp=[-1]*(n)
	def helper(i):
		if i==n:
			return 1
		
		if s[i]=='0':
			return 0

		if dp[i]!=-1:
			return dp[i]
			
		ways =helper(i+1)
		if 10<=int(s[i:i+2])<=26:
			ways+=helper(i+2)
		dp[i]=ways
		return dp[i]
	return helper(0)


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	s=input()
	print(solve(s))



if __name__=="__main__":
	main()