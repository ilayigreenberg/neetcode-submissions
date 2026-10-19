class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupancy = 0
        self.dct = dict()
        self.recent = BiNode([], None, None)
        self.past = BiNode([], None, self.recent)
        self.recent.past = self.past



    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1
        self.dct[key][1] += 1

        prv_recent = self.recent.past
        prv_recent.next = new = BiNode(key, prv_recent, self.recent)
        self.recent.past = new

        return self.dct[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct[key][0] = value
            self.dct[key][1] += 1   # counter for not having problem of removing key from
                # dct cause it's near past although we've inserted it later near recent
        else:
            if self.occupancy == self.capacity:
                while self.occupancy:
                    past = self.past.next
                    self.past.next = past.next
                    past.next.past = self.past

                    if past.val not in self.dct or self.dct[past.val][1]:
                        if self.dct[past.val][1]:
                            self.dct[past.val][1] -= 1
                        del past
                    else:     
                        del self.dct[past.val]
                        self.occupancy -= 1
                        del past
                        break
                  
            # insertion to dct
            self.occupancy += 1
            self.dct[key] = [value, 0]

        prv_recent = self.recent.past
        #changing prv next field to the new one
        prv_recent.next = new = BiNode(key, prv_recent, self.recent)
        self.recent.past = new




class BiNode:
    def __init__(self, val=0, past=None, next=None):
        self.val = val
        self.past = past
        self.next = next
