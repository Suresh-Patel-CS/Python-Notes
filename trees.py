

class Treenode:
    def __init__(self,data):
        self.data = data
        self.childern = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.childern.append(child)

def build_product_tree():
    root = Treenode('Electronics')
    
    latop = Treenode('Latop')

    root.add_child(latop)

if __name__ == '__main__':
    build_product_tree()