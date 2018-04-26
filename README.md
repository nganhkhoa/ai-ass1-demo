# Bloxorz game AI

Using console by the way

This project is only tested on Linux environment, Windows is not guaranteed to work fine.


## Demo

BFS: [asciinema](https://asciinema.org/a/ZmDTxfSMtGMaTbCVmb3B3xqge)

## To get things setup

```bash
pip install click
mkdir raw
python main.py

and choose generate stages
```

## The file structure

```bash
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
|---|---|---Stage.py
|---|---|---Tile.py
|---|---|---TileType.py
|---|---solver/
|---|---|---moves.py
|---|---|---Solver.py
|---|---|-------algorithm implement files
|---|---|---State.py
|---|---|---Block.py
|---|---stages/
|---|---|---GenStage.py
|---|---|---stages.py
```

## Game Structure

### Tiles

A tile is a square in the game. There are many types of tile.

1. The normal tile, this tile type has no effect on the block.
2. The soft tile, this tile cannot hold two blocks the same time. If our block is standing, this tile will break and our precious block will fall.
3. The button tile, this tile is a button type, pressing on the button will trigger something. And there are many type of buttons too.
4. The bridge tile, this tile is something that will be trigger by a button. In somecases, it will be close, you cannot move through it.
5. The goal tile, standing on this tile is considered win.
6. The split tile, stadning on this tile will teleport our block to 2 different places.

A button can be divided in many ways, in one way, the soft and hard one. If a button is a soft one, it can be pressed if one block is lay on top, while a hard one will need 2 blocks, standing block.

In another way to divide, a button can be a toggle button to bridges, or will open a set of bridges and close another set of bridges, or a combination of three.

After inspecting those types, I came up with an enumeration system:

```c++
// c++
enum class TileType : int {
    normal,
    goal,
    split,
    soft_ground,
    soft_button,
    hard_button,
    soft_special_button,
    hard_special_button
    soft_hell_button,
    hard_hell_button
};
```

And our tile class is as follows:

```c++
// c++
class Tile {
  public:
    TileType type;
    bool valid;         // if standing on this tile is ok
    int split_place[4]; // place after split

    Tile*[] toggle;       // Tiles to toggle
    Tile*[] open;         // Tiles to change to open
    Tile*[] close;        // Tiles to change to close
};
```

To construct a tile, we need to know exactly what type of Tile to construct.

A normal tile should be construct easiest: `Tile()`

A goal tile or a soft tile should be construct with no argument but the type: `Tile(TileType.goal)`, `Tile(TileType.soft_ground)`

A bridge at start could be missing, thus we need another argument to specify the state: `Tile(TileType.bridge, true)` or `Tile(TileType.bridge, false)`

A button, however is harder to construct, since we need a small constructor that gives our tile a list of bridges to toggle or to open and close only. A method is given:

```c++
// c++

// making a button which will toggle on active
Tile(TileType.soft_button, Tile*[] toggle);

// making a button which will open gates only
Tile(TileType.soft_special_button, Tile*[] open, NULL);

// making a button which will close gates only
Tile(TileType.soft_special_button, NULL, Tile*[] close);

// making a button which will open and closes set of bridges
Tile(TileType.soft_special_button, Tile*[] open, Tile*[] close);

// making a button which will open and closes set of bridges but also toggle some
Tile(TileType.soft_special_button, Tile*[] toggle, Tile*[] open, Tile*[] close);

// the same for hard button
```

Take close look that the bridges are given as `Tile*[]`. This is to make sure that this works even if more than 1 button point to the same bridge.

### Stage

A stage is a class defined only to store the board on first load, and place of block and a method to save all it's data to a binary file.

Given as follows:

```c++
// c++
class Stage {
  public:
    Tile[][] board;  // a 2 dimension matrix Tile
    int _x;
    int _y;
    char* name;

    Stage(char* name, Tile[][] b, int x, int y);
    void save(char* filename);
}
```

This class is used only to create binary files of stages and load to a State.

### Block

The Block is the core of whole game. Everything happens around block. For distinction, we will call it a Blox (form Bloxorz) if it's comprised of two Blocks. The Block by itself has only one index, the other index, we can calculate it through its state, standing or lying head North or lying head East.

When a split call is made, the Block will change its state to neutral. Thus we need another block to represent the splited Block. The Blox is implemented in State as an array. With selection bit to choose which Block will be move when move is call.

## Solver Folder

### moves

A numeration on how to move

```c++
// c++
enum moves {
    up,
    down,
    right,
    left
};
```

### State

This is the state to solve the game. A state is quite simple, just a board and a block, with some method to ease the use.

```c++
// c++
class State {
    Tile[][] board;
    Block blox[2];
    int selection = 1;

    void move(moves m) {
        void* ret = NULL;
        try {
            ret = blox[selection - 1]->move(m);
        }
        catch(everything) {
            throw error;
        }

        if (ret != NULL) {
            // ret is now a index after split
            blox[0]->split(ret);
            // post process
            // blox[1] = new Block(ret);
        }

        // try to join
        // if not split, just return
        // if not able to join, return
        this->join();
    }
};
```

When implementing algorithm, just need to call `move(direction)` and you're done. If when moving, an error occured (go out of board, standing in soft ground), it will throw and you can ignore the throw. The throw procedure is like a signal that a move is invalid.

### Solver

The solver framework is based on the strategy pattern, deppends on which mode we choose, it will run the algorithm. The solver main class stores the init state, the goal state if there's one and the algorithm mode to solve. Futhermore, when creating states, an already existed state might be generated again and again. To prevent the problem describe, the solver class will store a list of State Character.

The State Chracter is a string to defined in a STAGE that a STATE generated is unique. The character of a state is a sequence of these: the index of the two blocks, 

When the solver call on solve, it will run the algorithm on itself. Then with the init state, you can create a queue and solve.

A call to solver will be like this:

```c++
// c++
BinaryLoader* binary = new BinaryLoader();  // a fake binary loader
Stage* stage = binary->load("Filename");
State* init = new State(stage);
m = mode.bfs;  // bfs algo
Solver* problem = new Solver(init, mode);
problem->solve();
problem->printSolution();
```
