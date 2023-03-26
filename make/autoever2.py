import sys 

# 1 <= object <= N (1<=N<=100)
# object 별 tag (1<=tag<=10)
# key : a-z, _  1<= len <= 5
# val : a-z,A-Z,_,=,. 1<len<20
# 하나의 object에 달린 태그들의 key는 서로 다름
# 1 <= Q <= 1000
# input : object part set N
# output : SearchByTags(key,val) set
# S 반환하도록 key,val 정할 수 잇으면 yes 아니면 no
#
N = int(sys.stdin.readline())
pick_pick_list = []
obj_dict = {}
for i in range(1,N+1):
    make_dict = list(map(str,sys.stdin.readline().rstrip().split(',')))
    dic_dic = {}
    for r in make_dict:
        tmp = r.split("=")
        dic_dic[tmp[0]] = tmp[1]
    obj_dict[i] = dic_dic

Q = int(sys.stdin.readline())
pick_list = []
for i in range(Q):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    pick_list.append(tmp_list)



if Q == 1:
    print('yes')
else :
    for pick in pick_list:
        pick_dict = {}
        th = pick[0]
        
        for a in enumerate(pick[1:]):
            pick_dict[a[0]+1] = obj_dict[a[1]]
            
        key_list = []
        kv = pick_dict[1]
        kv_candidate = {}
        obj1_keys = list(kv.keys())
        
        for key in obj1_keys:
            cnt = 0
            tmp = 0
            val_list = [kv[key]]
            
            for r in range(2,len(pick_dict)+1):
                cnt += 1
                if key not in list(pick_dict[r].keys()):
                    val_list = []
                    break
                val_list.extend([pick_dict[r][key]])
                if cnt == (len(pick_dict)-1):
                    
                    val_list = list(set(val_list))
                    kv_candidate[key] = val_list
                
        cmp_dict = {}
        
        for i in obj_dict:
            if i not in pick[1:]:
                cmp_dict[i] = obj_dict[i]
        if not cmp_dict:
            print('yes')
        else : 
            ans = []
            for key in kv_candidate:
                flag = False
                cnt = 0
                for obj in cmp_dict:
                    try :
                        if cmp_dict[obj][key] in kv_candidate[key] :
                            flag *= False
                        else :
                            flag = True
                    except KeyError as k:
                        flag = True           
                ans.append(flag)
            
            if True in ans :
                print('yes')
            else : print('no')

    