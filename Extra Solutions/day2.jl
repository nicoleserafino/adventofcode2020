g(a,b,c,d) = parse(Int,a) <= count(c,d)<= parse(Int,b)
sum(map(x->g(x...),split.(readlines("2020/Day02/input2.txt"),r"(\s|:\s|-)")))