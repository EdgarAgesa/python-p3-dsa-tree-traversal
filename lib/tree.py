class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id, traversal='depth'):
    if traversal == 'depth':
      stack = [self.root]
      while stack:
        node = stack.pop()
        if node and node.get('id') == id:
          return node
        stack.extend(node.get('children', []))
    elif traversal == 'breadth':
      queue = [self.root]
      while queue:
        node = queue.pop(0)
        if node and node.get('id') == id:
          return node
        queue.extend(node.get('children', []))
    return None