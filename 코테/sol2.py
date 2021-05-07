from itertools import combinations
def solution(orders, course):
    menu = set()
    answer=[]

    for i in orders:
        for j in i:
            menu.add(j)
    menu = [i for i in menu]
    menu.sort()
    while course:
        hot_menu = dict()
        k = course.pop()
        # 메뉴로 만들수있는 모든조합
        menu_list = list(combinations(list(menu),k))
        while menu_list:
            cnt = 0
            check = menu_list.pop(0)
            # i번째 손님
            for i in range(0,len(orders)):
                # 모든 조합
                order_list = list(combinations(list(sorted(orders[i])),k))
                if check in order_list:
                    cnt+=1
            if cnt>=2:
                hot_menu[check] = cnt
        for i in hot_menu:
            if hot_menu[i] == max(hot_menu.values()):
               answer.append(''.join(i))    
    
    print(answer)
    return answer

orders = ["XYZ", "XWY", "WXA"]
solution(orders,[2,3,4])

# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]