# Bloxorz game AI

Using console by the way

## To get things setup

```
mkdir raw
echo '1' | python main.py
```

## The file structure

```
/------------------------
|---main.py
|---raw/
|---|---stage1
|---|---stage2
|---|---...
|---bloxorz/
|---|---game/
|---|---|---play.py
|---|---|---mode.py
|---|---|---Block.py
|---|---|---Stage.py
|---|---|---Tile.py
|---|---|---TileType.py
|---|---solver/
|---|---|---moves.py
|---|---|---solver.py
|---|---|---State.py
|---|---stages/
|---|---|---GenStage.py
|---|---|---stages.py
```

The game folder has a structure for all the components of the game, how the Tile is structure, how the Block will move,...

The stages folder has a collection of Stages in the main 33 levels of Bloxorz hard coded in using the structure describe in the game folder.

The solver will hold a collection of algorithm to solve the game, the solver includes structure of State describe in the upcomming parts.

## Understanding Stage

The Stage is the initial State of the game, using a Stage structure to be able to store and load the files back in and move from there.

Stage has 2 member, an matrix of Tile presenting the stage and the state of the block when the game begins.

The Tile object is much more complicated. In the game, there are many types of Tile, to make the type, I used a simple enum type to define.
It would be easier now that we have the type correspond to the way it should behave. But a tricky part on buttons.
A button can either, open new bridges, close bridges, open or close a set of bridges depends partly on the bridge status.

`to be stated later`

## State and how to move the block

A state is defined as:

```
```

When we make a move, either up, down, left, or right, the State will get the next coordinate of the blocks and call trigger on the Tiles.
If the tile index is `out of range`, it is an invalid move, if not, the trigger will run and return to us the result after modifing the board and the blocks status.

As can be seen, when the tile is a button, it will check whether the block will turn on the button.
A simple button open/close set of bridges will modify the board.
While a split button will modify the blocks status.
If the tile is a fragile tile (called soft_ground), a condition will check for the block if it will fall.
In other cases except for the goal state, the result shall be `true`.

If the move is valid, State will add to moves.

## Solver

Our algorithm will make a move from a State and then check for return as invalid or valid.
If an invalid move is made, we will skip, and look for a valid move.

`What if no valid move found?`

A valid move will then be check by the algorithm and if a goal is found, the algorithm will stop.

A simple solver may work like this:


```python
class State:
    ...
    def MakeALeapToGalaxy(this):
        while True:
            if not this.CreateARandomMove():
                # failed to create a random move
                return False
            if this.invalid()
                this.revert()
                continue
            return True
    ...


def simplesolver(s: State):
    q = [s]
    while len(q) > 0:
        new_state = q[0]
        q = q[1:]
        
        # remember to deepcopy here
        
        if new_state.MakeALeapToGalaxy():
            if new_state.isGoal():
                print("I found a Goal")
                break
```


