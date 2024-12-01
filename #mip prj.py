#mip prj

"""

9. Container 2D Loading Minimize Cost
 • There are 𝐾 trucks 1,2,…,𝐾 to transport 𝑁 items (2D shape) 
1, 2,…,𝑁. Truck 𝑘 has the container size 𝑊
 𝑘 ×𝐿[𝑘]. Item 𝑖 has size 
 𝑖 ×𝑙[𝑖] . Items loaded in a truck can not overlap. The cost of using 
truck 𝑘 is 𝑐[𝑘]. Find a solution that load 𝑁 items into 𝐾 trucks such 
that the total cost of trucks used is minimal.
 • A solution is represented by 𝑡[𝑖], 𝑥[𝑖], 𝑦[𝑖], and 𝑜[𝑖] in which 
(𝑥[𝑖], 𝑦[𝑖]) is the coordinate of item 𝑖 loaded in truck 𝑡[𝑖], 𝑜[𝑖] = 1, if 
the item 𝑖 is rotated 90 degree

 •Example
 • Input
 5 5
 90 70
 10 70
 80 30
 100 60
 20 90
 180 120 8
 20 100 10
 160 50 6
 120 140 11
 180 30 7
 
 • Output
 1 1 0 0 0
 2 1 0 70 1
 3 1 0 80 0
 4 1 90 0 1
 5 1 150 0 0
 
 • Input
Line 1: contains 𝑁 and 𝐾 (1 ≤ 𝑁,𝐾 ≤ 1000)
Line 𝑖 + 1 (𝑖 = 1,2,…,𝑁)contains 2 integers 𝑤[𝑖] and 𝑙[𝑖] (1 <
 = 𝑤[𝑖],𝑙[𝑖] ≤ 1000)
Line 1 + 𝑁 +𝑘 (𝑘 = 1,…,𝐾)contains 𝑊[𝑘],𝐿[𝑘]and 𝑐[𝑘] (1 <
 = 𝑊[𝑘],𝐿[𝑘] ≤ 1000,1 ≤ 𝑐[𝑘] ≤ 1000)
Output
Line 𝑖 (𝑖 = 1,2,...,𝑁): write 4 integers 𝑖,𝑡[𝑖],𝑥[𝑖],𝑦[𝑖],𝑜[𝑖]



Idea:


"""


class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return (self.height * self.width)
    
        
        
class Truck(Rectangle): # has Width, Height and Cost: the idea is to plot this out as a plane Oxy and put item so as to fit in it, so far no idea how to implement
    
    items_in_truck = []
    num_item_in_truck = 0
    
    def __init__(self, width, height, cost):
        super().__init__(width, height)
        self.cost = cost
        storage_width = "0" * self.width
        storage = [ storage_width for x in range(self.height)]  # [0][0] - [row][col] - [height == num_of_row][width == num_of_col]
        
    def area_value(self):
        return (self.area() / self.cost)
    
    def edges_value(self):
        edge_ratio = self.width/self.height if self.width > self.height else self.height/self.width
        return (self.area() / (edge_ratio * self.cost))
    
    def place_item(self, item, x, y):
        if self.num_item_in_truck == 0:
            self.items_in_truck.append((item, 0, 0))
        elif self.num_item_in_truck == 1:
            self.items_in_truck.append((item, self.items_in_truck[0][0] +1, self.items_in_truck[0][0] +1))  # still missing the tuple function to get the height/width of the item
            # also gotta check to see where to put the item     
            
        
        

class Item(Rectangle):

    orientation = 0

    def __init__(self, width, height):
        super().__init__(width, height)
        
    def rotate(self):
        if self.orientation == 0: 
            self.orientation = 1
            self.width, self.height = self.height, self.width   
        else:
            self.orientation = 0
            self.width, self.height = self.height, self.width   
        return self
        

        
# return n, k, list of Item and list of Truck
def input_data():
    n, k = (int(x) for x in input().split())
    items = []
    for i in range(n):
        width, height = (int(x) for x in input().split())
        items.append(Item(width, height))
    trucks = []
    for j in range(k):
        Width, Height, Cost = (int(y) for y in input().split())
        trucks.append(Truck(Width, Height, Cost)) 
    return n, k, items, trucks 



n, k, items, trucks = input_data()  


#if __name__ == "__main__":
#    n, k, items, trucks = input_data()
