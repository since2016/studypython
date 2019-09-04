class Node(object):
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.item)


class Tree(object):
    def __init__(self):
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node

        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):
        if self.root.item == item:
            return None
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.right and pop_node.right.item == item:
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, item):
        if self.root is None:
            return False

        parent = self.get_parent(item)
        if parent:
            # 判断是左/右子树
            del_node = parent.left if parent.left.item == item else parent.right
            # 如果要删除的节点左子树为空，
            if del_node.left is None:
                # 如果是parent的左节点, 就把该节点的右子树挂到parent的左子树/ 否则挂到右子树
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            # 如果是要删除的节点的右子树为空，
            elif del_node.right is None:
                # 如果要删除节点是parent的左子树， 把该节点挂到parent左子树/ 否则挂到右子树
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left

            else:
                # 左右子树都不为空, 寻找del_node 右子树的最左节点替代
                tmp_pre = del_node
                tmp_next = del_node.right
                # 如果del_node 右节点的左子树为空，刚好找到
                if tmp_next.left is None:
                    # 将tmp_next 替代del_node
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left

                    # 继续替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.right = del_node.right
                    tmp_next.left = del_node.left
                # 父节点也需处理
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False


    def inorder(self, node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item

    def postorder(self, node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.postorder(node.left)
        right_item = self.postorder(node.right)
        return left_item+right_item+result

    def preorder(self, node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.preorder(node.left)
        right_item = self.preorder(node.right)
        return result+left_item+right_item


if __name__ == '__main__':
    t = Tree()
    for i in range(1,10):
        t.add(i)

    print(t.preorder(t.root))
    print(t.inorder(t.root))
    print(t.postorder(t.root))