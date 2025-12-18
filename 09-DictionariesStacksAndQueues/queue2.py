from collections import deque

queue = deque(['Michael', 'Charlotte'])
queue.append('Olivia')
person = queue.popleft() # Działa błyskawicznie nawet przy milionach osób