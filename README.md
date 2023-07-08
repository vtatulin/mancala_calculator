# mancala_calculator
simple python class for mancala board and some calculations

## what mancala looks like

coordinates of pits:

        [  ] [12][11][10][ 9][ 8][ 7] [  ]
        [13]                          [ 6]
        [  ] [ 0][ 1][ 2][ 3][ 4][ 5] [  ]

initial position of seeds:

        [  ] [ 4][ 4][ 4][ 4][ 4][ 4] [  ]
        [ 0]                          [ 0]
        [  ] [ 4][ 4][ 4][ 4][ 4][ 4] [  ]

## usage

```python
from board import Board
b = Board()
#look at the board:
print(b)
b.mowe(2) ##mowing from second pit
```