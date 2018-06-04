#对于N个人组成的环形链，指定0位，按顺序定位1 ～（N-1），从0开始报数，每第M个人移除出链，直到最后一个人
'''
JOSEPH 问题

1）根据人数生成环形链
2）计数，从指定顺序开始遍历链
   1 - 初始位置为 0
   2 - 到计数第M时，移除该节点，如果该节点上级节点和下级节点都存在，将该节点的上级节点和下级节点链接起来；如果有一个不存在，则剩余那个是最后一个节点。
   3 - 从下级节点开始，重新计数

'''


class node():
    def __init__(self,value):
        self.value = value
        self.next = None



List = [0,2,3,4,5,6]

def generate_chain(List):

    return chain

def play(chain,m):
    count = 0
    last_node = node()
    while True:
        count+=1
        if count %m == 0:
            if node.next.next !=node:
                last_node.next = node.next
                print(node.value)
            else:
                print(node.next.value)
                break
        last_node = node
        node = node.next

