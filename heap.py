

class MinHeap(object):

    def __init__(self):
        self.heap = [] 
        self.current_size = 0

    def push(self, v):
        self.heap.append(v)
        self.current_size += 1
        self.sift_down(0, self.current_size-1)

    def heap_pop(self):
        el = self.heap.pop()
        if el:
            i = self.heap[0]
            self.heap[0] = el
            self.sift_up(0)
            return i
        return el

    def sift_down(self, startpos, pos):
        n = self.heap[pos]
        while pos > 0:
            parentpos = (pos-1) // 2
            parent = self.heap[parentpos]
            if n < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = n 

    def sift_up(self, pos):
        endpos = len(self.heap)
        startpos = pos
        childpos = 2*pos + 1
        n = self.heap[pos]
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and self.heap[childpos] > self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        self.heap[pos] = n
        self.sift_down(startpos, pos)

h = MinHeap()
for i in range(8, -1, -2):
    h.push(i)
h.push(5)

print(h.heap)