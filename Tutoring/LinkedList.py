class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

  def __str__(self):
    prev_data = self.previous.data if self.previous else None
    next_data = self.next.data if self.next else None
    return f"Node(data: {self.data}, previous: {prev_data}, next: {next_data})"

class LinkedListIterator:
  def __init__(self, head):
    self.trace = head

  def __next__(self):
    # maintains position in list
    if self.trace is None:
      raise StopIteration
    else:
      # return data trace is pointing
      # advance iteration
      data = self.trace.data
      self.trace = self.trace.next
      return data

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __iter__(self):
    return LinkedListIterator(self.head)

  def push_front(self, data):
    # added line to avoid nested nodes
    if isinstance(data, Node):
      data = data.data

    node = Node(data)
    self.length += 1

    if self.head is None:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head.previous = node
      self.head = node

  def push_back(self, data):
    # added line to avoid nested nodes
    if isinstance(data, Node):
      data = data.data

    node = Node(data)
    self.length += 1

    if self.tail is None:
      self.tail = node
      self.head = node
    else:
      node.previous = self.tail
      self.tail.next = node
      self.tail = node

  def print_list(self):
    node_list = []
    while self.head:
      if self.head.data:
        node_list.append(self.head.data)
      self.head = self.head.next
    for val in node_list:
      print(val.data)
    
  def insert(self, position, data):    
    # added line to avoid nested nodes
    if isinstance(data, Node):
      data = data.data

    if position < 0 or position > self.length:
      return False
    
    if position == 0:
      self.push_front(data)
      return True
    elif position == self.length:
      self.push_back(data)
      return True
    else:
      node = Node(data)

      trace = self.head

      for _ in range(position):
        trace = trace.next

      trace.previous.next = node
      node.previous = trace.previous

      node.next = trace
      trace.previous = node
      self.length += 1

      return True
    

  def remove(self, node_val):
    if self.head is None:
      return False
    elif self.head.next is None:
      if self.head.data == node_val:
        self.length -= 1
        self.head = None
        self.tail = None
        return True
      else:
        return False
    else:
      trace = self.head

      while trace is not None:
        if trace.data == node_val:
          self.length -= 1
          if trace.previous is None:
            self.head = trace.next
            self.head.previous = None
          else:
            trace.previous.next = trace.next
          if trace.next is None:
            self.tail = trace.previous
          else:
            trace.next.previous = trace.previous
          return True
        else:
          trace = trace.next
      

  def pop_front(self):
    if self.head is None:
      return None
    elif self.head.next is None:
      data = self.head.data
      self.length -= 1
      self.head = None
      self.tail = None
      return data
    else:
      data = self.head.data
      self.length -= 1
      self.head = self.head.next
      return data

  def pop_back(self):
    if self.tail is None:
      return None
    elif self.tail.previous is None:
      data = self.tail.data
      self.length -= 1
      self.head = None
      self.tail = None
      return data
    else:
      data = self.tail.data
      self.length -= 1
      self.tail = self.tail.previous
      self.tail.next = None #added line
      return data
    
  def __str__(self):
    result = "["
    curr = self.head

    while curr is not None:
      if curr.next is not None:
        result += f"{curr.data}, "
      else:
        result += f"{curr.data}"
      curr = curr.next
    result += "]"
    return result

# Create a linked list to test
ll = LinkedList()

# Add nodes directly with values
ll.push_front(1)  # List should be: 1
ll.push_front(2)  # List should be: 2 -> 1
ll.push_front(3)  # List should be: 3 -> 2 -> 1
ll.push_back(4)   # List should be: 3 -> 2 -> 1 -> 4

# print list
print(ll)  # Should print: [3,2,1,4]

ll.pop_front()
# print list
print(ll)  # Should print: [2,1,4]

ll.pop_back()
# print list
print(ll)  # Should print: [2,1]

ll.insert(2, 3)
# print list
print(ll)  # Should print: [2,1,3]

ll.remove(1)
# print list
print(ll)  # Should print: [2,3]

for item in ll:
  print(item)