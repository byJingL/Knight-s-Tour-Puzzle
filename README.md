# Knight's Tour Puzzle
The Knight’s Tour is a fun puzzle where you move the knight so that it visits every square of the chessboard once.
## Main Skill
Recursion, Backtracking, Matrices, OOP
## Rules
The knight is a chess piece. It moves in an L-shape and can jump over other pieces. It has to move 2 squares horizontally and 1 square vertically, or 2 squares vertically and 1 square horizontally. The rules of the knight's tour are as follows:
- The knight can start at any square.
- The knight must visit every square by moving in the L-shape.
- The knight can visit each square only once.
- The knight can finish anywhere on the board. This is called an 'open' tour of the board.
- You win if you visit every square on the board.
- You lose if you fail to visit every square only once without revisiting it.

## How to play
- Download [game.py](/game.py), [board.py](/board.py) and [excption.py](/exceptions.py)
- Run [game.py](/game.py)

## Examples
Player will be asked three questions to set the size of puzzle, the starting position and play or check solution.
### Check Solution
```
Enter your board dimensions: > 4 3
Enter the knight's starting position: > 1 3
Do you want to try the puzzle? (y/n): n

Here's the solution!
 ---------------
3|  1  4  7 10 |
2|  8 11  2  5 |
1|  3  6  9 12 |
 ---------------
    1  2  3  4 
```
### Play the game
```
Enter your board dimensions: > 4 3
Enter the knight's starting position: > 1 3
Do you want to try the puzzle? (y/n): y
 ---------------
3|  X __ __ __ |
2| __ __  1 __ |
1| __  2 __ __ |
 ---------------
    1  2  3  4 
Enter your next move: > 3 2
 ---------------
3|  * __ __ __ |
2| __ __  X __ |
1|  1 __ __ __ |
 ---------------
    1  2  3  4 
Enter your next move: > 
```
## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.