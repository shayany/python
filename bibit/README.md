Bibit
_____

Bibit takes place in a 2D pyramid of triangles. The pyramids vary in size, from the smallest of
size 1 being a single cell:
<pre>
   ^
  / \
 " — "
</pre>
doubling to the pyramid with 4 cells:
<pre>
    ^
   / \
  " — "
 / \ / \
" — " — "
</pre>
Double again to get the pyramid with 16 cells:
<pre>
        ^
       / \
      " — "
     / \ / \
    " — " — "
   / \ / \ / \
  " — " — " — "
 / \ / \ / \ / \
" — " — " — " — "
</pre>
This could be doubled to one with 64 cells:
<pre>
                ^
               / \
              " — "
             / \ / \
            " — " — "
           / \ / \ / \
          " — " — " — "
         / \ / \ / \ / \
        " — " — " — " — "
       / \ / \ / \ / \ / \
      " — " — " — " — " — "
     / \ / \ / \ / \ / \ / \
    " — " — " — " — " — " — "
   / \ / \ / \ / \ / \ / \ / \
  " — " — " — " — " — " — " — "
 / \ / \ / \ / \ / \ / \ / \ / \
" — " — " — " — " — " — " — " — "
</pre>
and so on, so that the number of cells is a power of 4.

Each cell is either black or white, representing a bit. Therefore, each triangle corresponds to a
binary number, where the bits are numbered in reading order:
<pre>
    ^
   /0\
  " — "
 /1\2/3\
" — " — "
</pre>
So this triangle with two black cells and two white cells
<pre>
    ^
   /1\
  " — "
 /0\1/1\
" — " — "
</pre>
corresponds to the binary number 1101 = 0x05.

The binary number 1100 corresponds to this pyramid:
<pre>
    ^
   /0\
  " — "
 /0\1/1\
" — " — "
</pre>
Similary, the binary number
<pre>
0101110 11010 011 0
= 0101 1101 1010 0110 = 0x5da6
</pre>
corresponds to this pyramid:
<pre>
        ^
       /0\
      " — " 
     /1\1/0\
    " — " — "
   /0\1/0\1/1\
  " — " — " — "
 /0\1/1\1/0\1/0\
" — " — " — " — "
</pre>
Tribit is a kind of checksum algorithm, which takes a binary number and calculates
a single-bit checksum.

It does this by matching patterns in the input pyramid, and reducing those patterns
according to the following 16 transition rules:
<pre>
0000 -> 0000
0001 -> 1000
0010 -> 0001
0011 -> 0010
0100 -> 0000
0101 -> 0010
0110 -> 1011
0111 -> 1011
1000 -> 0100
1001 -> 0101
1010 -> 0111
1011 -> 1111
1100 -> 1101
1101 -> 1110
1110 -> 0111
1111 -> 1111
</pre>
So the third rule 0010 -> 0001 states that a group of four triangles with this shape
changes like this:
 <pre>
    ^             ^
   /0\           /1\
  " — "    ->   " — "
 /1\0/0\       /0\0/0\
" — " — "     " — " — "
</pre>
For a pyramid with 16 cells, the rules apply in groups of 4:
<pre>
        ^
       /A\
      " — " 
     /A\A/A\
    " — " — "
   /B\C/C\C/D\
  " — " — " — "
 /B\B/B\C/D\D/D\
" — " — " — " — "
</pre>
where the group C is upside-down and the bits numbered like this:
<pre>
 " — " — "
  \1/2\3/
   " — "
    \0/
     "
</pre>
Example:
<pre>
        ^
       /0\
      " — "
     /1\1/0\
    " — " — "
   /0\1/0\1/1\
  " — " — " — "
 /0\1/1\1/0\1/0\
" — " — " — " — "
</pre>
Group A is
<pre>
    ^
   /0\
  " — "
 /1\1/0\
" — " — "
</pre>
(0110) and transforms to (1011):
<pre>
    ^
   /1\
  " — "
 /1\0/1\
" — " — "
</pre>
In this way, the entire pyramid transforms to this:
<pre>
        ^
       /1\
      " — "
     /1\0/1\
    " — " — "
   /1\1/1\1/0\
  " — " — " — "
 /0\1/1\1/1\0/0\
" — " — " — " — "
</pre>
This is step 1.

The next step is this:
<pre>
        ^
       /1\
      " — "
     /1\1/1\
    " — " — "
   /0\1/1\1/1\
  " — " — " — "
 /1\1/1\1/0\0/0\
" — " — " — " — "
</pre>
The algorithm iterates like this.

There is one additional rule: If a pattern matches at group level, then the entire pyramid
reduces to a simpler one.

So, if we have this pyramid:
 <pre>
        ^
       /1\
      " — "
     /1\1/1\
    " — " — "
   /1\1/1\1/0\
  " — " — " — "
 /1\1/1\1/0\0/0\
" — " — " — " — "
</pre>
this reduces to this smaller pyramid
<pre>
    ^
   /1\
  " — "
 /1\1/0\
" — " — "
</pre>
in a single step.

Transitively, if you have this pyramid:
<pre>
                ^
               /0\
              " — "
             /0\0/0\
            " — " — "
           /0\0/0\0/0\
          " — " — " — "
         /0\0/0\0/0\0/0\
        " — " — " — " — "
       /0\0/0\0/0\0/0\0/0\
      " — " — " — " — " — "
     /0\0/0\0/0\0/0\0/0\0/0\
    " — " — " — " — " — " — "
   /0\0/0\0/0\0/0\0/0\0/0\0/0\
  " — " — " — " — " — " — " — "
 /0\0/0\0/0\0/0\0/0\0/0\0/0\0/0\
" — " — " — " — " — " — " — " — "
</pre>
this reduces to
<pre>
  ^
 /0\
" — "
</pre>
in a single step.

The rules are structured so that it is always well-defined how to transform a pyramid.

Your task is to implement a program that takes any string of 0 and 1s of suitable length, lowest bit at the end on the command
line, internally constructs the corresponding pyramid, prints the pyramid as a binary string on one line (so the first line
is the same as the input), applies the rules, prints the resulting pyramid in each step as a binary string in one line,
and loops until the pyramid is reduced to a single bit and you print either a 0 or 1 on a single line.

Sample session:
<pre>
> tribit.exe 0100
0100
0000
0
</pre>
Please include the dump of a session starting with your birthday as an integer in MMDDYY divded by two, encoded to binary
in your response.
So if you are born the 24th of December 1980, the seed is 122480/2 = 61240 and it becomes this invocation:
<pre>
> tribit.exe 1110111100111000
…
1
</pre>
For reference, here is a visual dump of the rules:
<pre>
    ^             ^
   / \           / \
  " — "   ->    " — "
 / \ / \       / \ / \
" — " — "     " — " — "

    ^             ^
   /#\           / \
  " — "   ->    " — "
 / \ / \       / \ /#\
" — " — "     " — " — "

    ^             ^
   / \           /#\
  " — "   ->    " — "
 /#\ / \       / \ / \
" — " — "     " — " — "

    ^             ^
   /#\           / \
  " — "   ->    " — "
 /#\ / \       /#\ / \
" — " — "     " — " — "

    ^             ^
   / \           / \
  " — "   ->    " — "
 / \#/ \       / \ / \
" — " — "     " — " — "

    ^             ^
   /#\           / \
  " — "   ->    " — "
 / \#/ \       /#\ / \
" — " — "     " — " — "

    ^             ^
   / \           /#\
  " — "   ->    " — "
 /#\#/ \       /#\#/#\
" — " — "     " — " — "

    ^             ^
   /#\           /#\
  " — "   ->    " — "
 /#\#/ \       /#\ /#\
" — " — "     " — " — "

    ^             ^
   / \           / \
  " — "   ->    " — "
 / \ /#\       / \#/ \
" — " — "     " — " — "

    ^             ^
   /#\           /#\
  " — "   ->    " — "
 / \ /#\       / \#/ \
" — " — "     " — " — "

    ^             ^
   / \           /#\
  " — "   ->    " — "
 /#\ /#\       /#\#/ \
" — " — "     " — " — "

    ^             ^
   /#\           /#\
  " — "   ->    " — "
 /#\ /#\       /#\#/#\
" — " — "     " — " — "

    ^             ^
   / \           /#\
  " — "   ->    " — "
 / \#/#\       / \#/#\
" — " — "     " — " — "

    ^             ^
   /#\           / \
  " — "   ->    " — "
 / \#/#\       /#\#/#\
" — " — "     " — " — "

    ^             ^
   / \           /#\
  " — "   ->    " — "
 /#\#/#\       /#\#/ \
" — " — "     " — " — "

    ^             ^
   /#\           /#\
  " — "   ->    " — "
 /#\#/#\       /#\#/#\
" — " — "     " — " — "
</pre>
