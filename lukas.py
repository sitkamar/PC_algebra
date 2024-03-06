input = [50,20,1,1,1,7,0.6,1,1,9]
out = [0,58.6]
for i in range(1,len(input)-1):
    out.append(out[i]*1.022)
print(out,len(out))
i = 1
res_in = [0]
res_out = [0]
for j in range(len(input)):
    res_in.append(input[j]/((1+i)**(j+1)))
    res_in[j+1]*=1000000
    res_out.append(out[j]/((1+i)**(j+1)))
    res_out[j+1]*=1000000
print(res_in)
print(res_out)
print(sum(res_in))
print(sum(res_out))
print(sum(res_out)-sum(res_in))


chs_v = 459533.9943438731
chs_n = 35425009.34566163
i_v = 1
i_n = 0.5
vvp = i_n + chs_n*(i_v-i_n)/(chs_v+chs_n)
print(vvp)
