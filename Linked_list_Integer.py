#----------------------------
# input :
# 1. head of linked list
# 2. Arr with number which need to find in linked list
#-----------------------------
class Solution:
    def numComponents(self, head, G):
        H = set(G)
        
        count = 0         
        connected = False 
        
        while head:
            if head.val in H and not connected:
                connected = True
                count += 1
            elif head.val not in G and connected:
                connected = False
            
            head = head.next
            
        return count
        