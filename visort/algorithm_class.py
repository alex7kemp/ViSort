        self.bubble_sorted = list(self.myList)
        
        for index in range(1, len(self.bubble_sorted)):
            value = self.bubble_sorted[index]
            location = index
            
            while location > 0 and self.bubble_sorted[location - 1] > value:
                self.bubble_sorted[location] = self.bubble_sorted[location - 1]
                location -= 1
                
            self.bubble_sorted[location] = value
        self.bubble_sorted[location] = value
