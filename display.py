#Create a digital display
def createScreen(n) :
  for i in range(7) :
    screen[i].extend((5+(4*(n-1)))*[zero])

#Draw a number on the display at the specified position
def writeNum(n, field) :
  delta = 4*(field-1) #The "jump" needed to go to the next digit's position

  #Draw segments of the number (7 Segments)
  def draw1() : #Top horizontal
    screen[1][1+delta] = screen[1][2+delta] = screen[1][3+delta] = one

  def draw2() : #Middle horizontal
    screen[3][1+delta] = screen[3][2+delta] = screen[3][3+delta] = one

  def draw3() : #Bottom horizontal
    screen[5][1+delta] = screen[5][2+delta] = screen[5][3+delta] = one

  def draw4() : #Top left vertical
    screen[1][1+delta] = screen[2][1+delta] = screen[3][1+delta] = one

  def draw5() : #Top right vertical
    screen[1][3+delta] = screen[2][3+delta] = screen[3][3+delta] = one

  def draw6() : #Bottom left vertical
    screen[3][1+delta] = screen[4][1+delta] = screen[5][1+delta] = one

  def draw7() : #Bottom right vertical
    screen[3][3+delta] = screen[4][3+delta] = screen[5][3+delta] = one

  #Draw specified digit (0-9)
  if n == 0 :
    draw1(); draw4(); draw5(); draw6(); draw7(); draw3();
  elif n == 1 :
    draw5(); draw7();
  elif n == 2 :
    draw1(); draw2(); draw3(); draw5(); draw6();
  elif n == 3 :
    draw1(); draw2(); draw3(); draw5(); draw7();
  elif n == 4 :
    draw2(); draw4(); draw5(); draw7();
  elif n == 5 :
    draw1(); draw3(); draw4(); draw2(); draw7();
  elif n == 6 :
    draw1(); draw3(); draw4(); draw2(); draw6(); draw7();
  elif n == 7 :
    draw1(); draw5(); draw7();
  elif n == 8 :
    draw1(); draw2(); draw3(); draw4(); draw5(); draw6(); draw7();
  elif n == 9 :
    draw1(); draw2(); draw3(); draw4(); draw5(); draw7();

#Display screen on the console
def displayScreen() :
  for i in screen :
    for j in i :
      print(j, end="")
    print()

#Create a display array
screen = []
for i in range(7) :
  screen.append([])

#Colours specifying dark and bright cells respectively
zero = "⬛"
one = "🟨"

num = int(input("Enter an integer: "))
test = num

fields = 0
l = []

#Calculate the number of digits entered to create fields accordingly
while test > 0 :
  r = test % 10
  test //= 10
  fields += 1
  l.append(r)

l = l[::-1]

createScreen(fields)

#Write the digits at the right positions
for i in range(len(l)) :
  writeNum(l[i], i+1)

displayScreen()
