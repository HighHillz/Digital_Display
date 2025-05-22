import sys
sys.stdout.reconfigure(encoding='utf-8')

class Display :
    def __init__ (self, value) :
        self.value = value
        self.display = []
    

    def getLenght(self) :
        length = 0
        value = self.value

        while(value >= 0) :
            value = value//10
            length+=1

            if(value == 0) :
                break

        return length
    

    def buildDisplay(self) :
        display_count = self.getLenght()
        display_dim = {
            "width": 5*display_count-(display_count-1),
            "height": 7
        }

        for i in range(display_dim["height"]) :
            self.display.append([])
            for j in range(display_dim["width"]) :
                self.display[i].append(0)

    def drawDigit(self, n, display_number) :
        delta = 4 * (display_number - 1)

        # Helper functions use arrow syntax to preserve 'self'
        def top_horizontal() :
            for i in range(1, 4) :
                self.display[1][i + delta] = 1
          
        def middle_horizontal() :
            for i in range(1, 4) :
                self.display[3][i + delta] = 1
            
        def bottom_horizontal() :
            for i in range(1, 4) :
                self.display[5][i + delta] = 1
            
        

        def top_left_vertical() :
            for i in range(1, 4) :
                self.display[i][1 + delta] = 1
            
        

        def top_right_vertical() :
            for i in range(1, 4) :
                self.display[i][3 + delta] = 1

        def bottom_left_vertical() :
            for i in range(3, 6) :
                self.display[i][1 + delta] = 1

        def bottom_right_vertical() :
            for i in range(3, 6) :
                self.display[i][3 + delta] = 1
        
        if n == 0:
            top_horizontal()
            bottom_horizontal()
            top_left_vertical()
            top_right_vertical()
            bottom_left_vertical()
            bottom_right_vertical()
        elif n == 1:
            top_right_vertical()
            bottom_right_vertical()
        elif n == 2:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_right_vertical()
            bottom_left_vertical()
        elif n == 3:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_right_vertical()
            bottom_right_vertical()
        elif n == 4:
            top_left_vertical()
            middle_horizontal()
            top_right_vertical()
            bottom_right_vertical()
        elif n == 5:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_left_vertical()
            bottom_right_vertical()
        elif n == 6:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_left_vertical()
            bottom_left_vertical()
            bottom_right_vertical()
        elif n == 7:
            top_horizontal()
            top_right_vertical()
            bottom_right_vertical()
        elif n == 8:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_left_vertical()
            top_right_vertical()
            bottom_left_vertical()
            bottom_right_vertical()
        elif n == 9:
            top_horizontal()
            middle_horizontal()
            bottom_horizontal()
            top_left_vertical()
            top_right_vertical()
            bottom_right_vertical()
            
        
        for i in range(len(self.display)) :
            for j in range(len(self.display[i])) :
                if (self.display[i][j] == 1) :
                    self.display[i][j] = 1
                else :
                    self.display[i][j] = 0
                
    def drawNumber(self) :
        value = self.value
        l = []

        while value >= 0 :
            l.append(value % 10)
            value //= 10
            if(value == 0) :
                break
        
        l = l[::-1]

        for i in range(len(l)) :
            self.drawDigit(l[i], i+1)
        
    def displayNumber(self) :
        self.buildDisplay()
        self.drawNumber()

        for i in range(len(self.display)) :
            for j in range(len(self.display[i])) :
                if (self.display[i][j] == 1) :
                    print("🟨", end="")
                else :
                    print("⬛", end="")
            print()

if __name__ == "__main__":
    ans = "y"

    while ans == "y":
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a non-negative number.")
        Display(n).displayNumber()
        
        ans = input("Do you want to enter another number? ('y'/any key): ").strip().lower()