class TNode:
  data = ""
  left = None
  right = None

def node(d, L = None, R = None):
  n = TNode()
  n.data = d
  n.left = L
  n.right = R
  return n

T = node ( "*",
      node ( "+",
        node ( "1" ),
        node ( "4" )
        ),
      node ( "-",
        node ( "9" ),
        node ( "5" )
        )
      )

def DFS ( T ):
  if not T: return
  print(T.data, end=" ")
  DFS(T.left)
  DFS(T.right)

def DFS_stack ( T ):
  stack = [T]
  while stack:
    V = stack.pop()
    print(V.data, end=" ")
    if V.right: stack.append(V.right)
    if V.left: stack.append(V.left)

DFS( T ); print()
DFS_stack( T ); print()