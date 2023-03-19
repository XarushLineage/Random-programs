-- Define a data structure for the state of the robot
data Robot = Robot { position :: (Int, Int), direction :: Direction, moving :: Bool }
data Direction = North | East | South | West deriving (Enum, Show)

-- Define a function to move the robot one unit in the current direction
moveRobot :: Robot -> Robot
moveRobot robot
  | moving robot == False = robot
  | direction robot == North = Robot { position = (x, y+1), direction = North, moving = True }
  | direction robot == East = Robot { position = (x+1, y), direction = East, moving = True }
  | direction robot == South = Robot { position = (x, y-1), direction = South, moving = True }
  | direction robot == West = Robot { position = (x-1, y), direction = West, moving = True }
  where (x, y) = position robot

-- Define functions to turn the robot left or right
turnLeft :: Robot -> Robot
turnLeft robot = robot { direction = toEnum (mod (fromEnum (direction robot) - 1) 4) }

turnRight :: Robot -> Robot
turnRight robot = robot { direction = toEnum (mod (fromEnum (direction robot) + 1) 4) }

-- Define a function to stop the robot
stopRobot :: Robot -> Robot
stopRobot robot = robot { moving = False }

-- Define a function to display the current state of the robot
displayRobot :: Robot -> String
displayRobot robot = "Position: " ++ show (position robot) ++ ", Direction: " ++ show (direction robot) ++ ", Moving: " ++ show (moving robot)

-- Define a function to process user commands and update the state of the robot
processCommand :: Robot -> String -> Robot
processCommand robot "forward" = moveRobot robot
processCommand robot "backward" = moveRobot (robot { direction = toEnum (mod (fromEnum (direction robot) + 2) 4) })
processCommand robot "left" = turnLeft robot
processCommand robot "right" = turnRight robot
processCommand robot "stop" = stopRobot robot
processCommand robot _ = robot -- Invalid command, do not update state of robot

-- Define a function to handle user input and output
handleInput :: Robot -> IO ()
handleInput robot = do
  putStr "> "
  command <- getLine
  let newRobot = processCommand robot command
  if position newRobot `elem` [(x,y) | x <- [-5..5], y <- [-5..5]]
    then do
      putStrLn (displayRobot newRobot)
      handleInput newRobot
    else do
      putStrLn "Error: Out of bounds"
      handleInput robot

-- Define a main function to start the program
main :: IO ()
main = do
  putStrLn "Robot Movement Control"
  let initialRobot = Robot { position = (0, 0), direction = North, moving = False }
  putStrLn (displayRobot initialRobot)
  handleInput initialRobot
