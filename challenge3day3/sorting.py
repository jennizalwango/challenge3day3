listi = [1,2,3,4,5,6,'j','q','c']
evens=[]
odds =[]
characters = []
def list_sort():
    for x in  listi:
        if type(x) == str:
            characters.append(x)
        elif type(x) == int:
            if x % 2 == 0:
                evens.append(x)
            elif  x % 2 ==1:
                odds.append(x)
    my_dict = {}    
    my_dict['evens'] = evens
    my_dict['odds'] = odds
    my_dict['characters'] = characters 
    return my_dict
function = list_sort()    
print(function)
















    # my_dict['even'] = sorted('even')
#     my_dict['odd'] = sorted('odd')
#     my_dict['character'] = sorted('character')
#     return'my_dict'
# print(list.sort = () )
# print(results)









             