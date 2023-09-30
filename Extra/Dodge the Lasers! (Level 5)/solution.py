def solution(s):
	frac_sqrt_2_minus_1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

	def calculation(s):
		if s == 1:
			return 1
		if s < 1:
			return 0
		nn = frac_sqrt_2_minus_1*s//(10**100)
		return (s*nn + s*(s+1)//2 - nn*(nn+1)//2 - calculation(nn))

	s = int(s)
	return str(int(calculation(s)))