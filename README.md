# Bloxorz game AI

Using console by the way

This project is mainly tested on Linux environment, Windows is not guaranteed to work fine.

## Demo

[BFS](https://asciinema.org/a/ZmDTxfSMtGMaTbCVmb3B3xqge)

## To get things setup

### Requirements

Python 3.6 or above is required

Pip is also required to install packages

### Quick setup

```bash
pip install -r requirements.txt
python main.py
```

or use virtualenv for development

```bash
virtualenv bloxorz-env
source bloxorz-env/bin/activate
pip install -r requirements.txt
python main.py
```

### Dependencies

Click to catch arrows key pressed: [offical websites](http://click.pocoo.org/6/)

Colorama to use ansi escape code in Windows: [github](https://github.com/tartley/colorama)

## The file structure

```bash
/------------------------
|---main.py
|---raw/
|---|---stage1
|---|---stage2
|---|---...
|---bloxorz/
|---|---common/
|---|---|---getKey.py
|---|---|---menu.py
|---|---|---moves.py
|---|---game/
|---|---|---play.py
|---|---|---Stage.py
|---|---|---Tile.py
|---|---|---TileType.py
|---|---solver/
|---|---|---Solver.py
|---|---|---State.py
|---|---|---Block.py
|---|---|---mode.py
|---|---|
|---|---|---algorithm implement files
|---|---stages/
|---|---|---GenStage.py
|---|---|---stage1.py
|---|---|---stage2.py
|---|---...
```

## Game Structure

### Tiles

#### Examination

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

#### Tile class

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

    int* trigger(bool standing);
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
Tile(TileType.soft_hell_button, Tile*[] toggle, Tile*[] open, Tile*[] close);

// the same for hard button
```

Take close look that the bridges are given as `Tile*[]`. This is to make sure that this works even if more than 1 button point to the same bridge.

#### Trigger process

The tile has a trigger function which will do things based on what the Tile type is. If the tile is a button, according to the button type, it will open/close/toggle bridges. If the tile is a split tile and the block is standing, it will return the new address of the blocks. If the tile is a soft ground and the block is standing, it will throw a "Fall" error. If the tile is a Bridge and not valid, a "Hidden Bridge" will be thrown. Other situtation won't do anything to the board or throw anything.

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

This class is used only to create binary files of stages and load to a State on play.

### Block

The Block is the core of whole game. Everything happens around block. For distinction, we will call it a Blox (form Bloxorz) if it's comprised of two Blocks. The Block by itself has only one index, the other index, we can calculate it through its state, standing or lying head North or lying head East.

When a split call is made, the Block will change its state to neutral. Thus we need another block to represent the splited Block. The Blox is implemented in State as an array. With selection bit to choose which Block will be move when move is call.

## Solver Folder

### moves

A numeration on how to move

```c++
// c++
enum moves {
    nomoves,
    up,
    down,
    right,
    left,
    split,
    join,
    swap
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
    moves[] moves;

    void toggleActive() {
        if (this->selection == 2)
            this->selection = 1;
        else
            this->selection = 2
    }
};

void move(State* s, moves m) {
    void* ret = NULL;
    Block* block = &(s->blox[x->selection - 1])
    try {
        block->move(m);

        if (block is out of bound)
            throw outofbound

        // trigger the tiles
        ret = s->board[block->index()].trigger();

        if !(block->standing || block->spliting)
            // trigger the other block
    }
    catch(everything) {
        // reverse the move
        block->move(m.reverse())
        throw error;
    }

    s->moves.append(m)

    if (ret != NULL) {
        // ret is now a index after split
        s->blox[0]->split(ret);
        // post process
        // blox[1] = new Block(ret);

        s->moves.append(moves.split)
    }

    // try to join
    // if not split, return false
    // if not able to join, return false
    // else join and return true and add to list of moves
    if (s->join())
        s->moves.append(moves.join)
}
```

When implementing algorithm, just need to call `move(s, direction)` and you're done. If when moving, an error occured (go out of board, standing in soft ground), it will throw and you can ignore the throw. The throw procedure is like a signal that a move is invalid.

### Solver

// to be updated

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

### ALGORITHM

Algorithm explanation

#### BFS

```c++
List<State*>* queue = new Queue<State*>();
queue->enqueue(init);

int count = 0;
while (true) {
    if (queue->empty() || count > 50000)
        break;

    State* s = queue->dequeue();
    if (s->goal())
        return;

    moves* list_moves = gen_moves(s);

    for (moves m : s) {
        State* new_state = s->clone();
        new_state->move(m);
        queue->enqueue(new_state);
    }

    count++;
}
```

#### DFS

```c++
List<State*>* stack = new Stack<State*>();
stack->enqueue(init);

int count = 0;
while (true) {
    if (stack->empty() || count > 50000)
        break;

    State* s = stack->pop();
    if (s->goal())
        return;

    moves* list_moves = gen_moves(s);

    for (moves m : s) {
        State* new_state = s->clone();
        new_state->move(m);
        stack->push(new_state);
    }

    count++;
}
```

#### HILL CLIMBING
