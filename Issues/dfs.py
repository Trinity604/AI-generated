# This is sample code for trying out Code Transformation.
from typing import List

def dfs_path(value: int, root: Node, path: List[int] | None):
  if root is None:
    return ''
  else:
    if not path:
      path = []

    path.append(root.value)
    if root.value == value:
      return '->'.join([str(n) for n in path])

    p = dfs_path(value, root.left, path)
    if p != '':
      return p
    else:
      p = dfs_path(value, root.right, path)
      if p != '':
        return p

    path.pop()

    return p