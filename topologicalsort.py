#针对有序对进行排序，其中有序对中的低序对象要排列在高序对象之前
'''
方法1：

1。遍历每个有序对，对每个元素排在其前面的元素个数计数，计算入度
2。为每个元素建立 排在其后面的字母的数组
2。根据入度进行排序

what I learnt from this programme:
1) list.pop() can only support index pop, not value pop, should use list.remove(value)
2) dict.pop() support key & value pop
3) dict can not be interated when the key changes
'''

from stdpackage import stdio





def count_from_file(file):
    print('enter count_from_file')
    tempdict = {}

    for data in file:
        obj1,obj2 = data[0],data[1]
        if obj1 not in tempdict.keys():
            tempdict[obj1]=[]
        if obj2 not in tempdict.keys():
            tempdict[obj2]=[obj1]
        else:
            tempdict[obj2].append(obj1)

    print('return temptict:{0} '.format(tempdict))
    return tempdict


def pop_zeroitem(leads_dict):
    '''
    recurse to pop all the 0-leads item to form the sorted list
    1 - checi if the original leads is 0
    2 - if yes, pop, and delete from all existed leadsdict
    3 - if not, continue

    :param leads_dict:
    :return: sorted list
    '''
    print('ender pop_zeroitem')
    List = []

    while leads_dict !={}:
        print('leads_dict is not NONE')
        keys = leads_dict.keys()

        for key in keys:
            if leads_dict[key] == []:
                List.append(key)
                print('List updated:{0}'.format(List))
                other_keys = keys - key
                for other_key in other_keys:
                    print('key is {0}, other key is {1}'.format(key,other_key))
                    if key in leads_dict[other_key]:
                        print('key"{0}" value is {1}, has key {2}'.format(other_key,leads_dict[other_key],key))
                        leads_dict[other_key].remove(key)
                        print('removed {0}, value left: {1} '.format(key,leads_dict[other_key]))

        for key in List:
            print('keys left: {0}'.format(leads_dict.keys()))
            if key in leads_dict.keys():
                leads_dict.pop(key)
            else:pass
    print('return List:{0} '.format(List))
    return List


def main():
    print('start')
    file = [['a','b'],['c','b'],['a','c'],['d','c'],['c','f']]
    #call function
    leads_dict = count_from_file(file)
    List = pop_zeroitem(leads_dict)

    print('list is {0}'.format(List))

main()