#Define the base class player
class Player:
  def play(self):
      print("The player is playing cricket." )

#Define the base class Batsman
class Batsman(Player):
  def play(self):
      print("The Batsman is batting. ")

#Define the base class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each object 
batsman.play()
bowler.play()