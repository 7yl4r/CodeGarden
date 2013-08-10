This experiment in python has been created for my own personal exploration of genetic algorithms.

For more information please contact murray.tylar@gmail.com

======

In retrospect, this was a rough attempt to explore a problem very similar to that presented at the [2013 ICFP Contest](http://icfpc2013.cloudapp.net/) (excerpt below).

    Prologue
    ~~~~~~~~
    
    Game:    I have a program A, and I want you to guess it.
    Player:  Can you tell me what is A(16), A(42) and A(128)?
    Game:    Sure, A(16) = 17, A(42) = 43, and A(128) = 129.
    Player:  Is the program B0, where B0(x) = x + 1?
    Game:    No dice, A(9) = 9, but B0(9) = 10.
    Player:  What is A(11), A(12) then?
    Game:    Since you ask so nicely: A(11) = 11, A(12) = 13.
    Player:  Is the program B1, where 
             B1(x) = if ((x & 1) ^ 1) = 0 then x else x + 1
    Game:    That's right! You score one point. 
             I have a program A', and want you to guess it.
    Player:  Argh!!!
    
    We want you to guess a few thousand such programs, some slightly
    smaller, many a bit bigger. You will have 5 minutes to guess each
    one. You will most likely want to program a computer to do this.
