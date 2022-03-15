def ip_addr(arr):
    d = dict()
    max_count = 0
    max_ip= []
    for i in arr:
        indexVal = i.index(" ")
        ip_list = i[:indexVal]
        if ip_list in d:
            d[ip_list] += 1
            if d[ip_list] > max_count:
                max_count = d[ip_list]
        else:
            d[ip_list] = 1
    
        for key,value in  d.items():
            if value == max_count:
                max_ip.append(key)
        
    return max_ip

arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXX dsf ZZZ"]
res = ip_addr(arr)
print(res)

# def ip_addr(arr):
#     d = dict()
    
#     countExist =0
#     for i in arr:
#         indexVal = i.index(" ")
#         ip = i[:indexVal]
#         countFirst = 1
#         if ip not in d:
#             d[ip] = countFirst + 1
#         else:
#             d[ip] = countExist +1
#             countExist +=1
#     # print(d)
#     #Another way of returning
#     # for key, values in d.items():
#     #     fin_max = max(d, key=d.get)
#     # return fin_max
#     v = list(d.values())
#     k = list(d.keys())
#     print(d,v,k)
#     resIP = k[v.index(max(v))]
        
#     return resIP

# arr= ["10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXXd zzz", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.2 ddddd yyy ZZZ", "10.10.10.1 BroXX yyyy ZZZ", "10.10.10.1 BroXX dsf ZZZ"]
# res = ip_addr(arr)
# print(res)