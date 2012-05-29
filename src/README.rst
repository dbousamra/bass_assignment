ThoughtWorks Graduate Programming Interview Questions
=====================================================

How to run:
-----------
Compilation:
~~~~~~~~~~~~

``javac -d bin -sourcepath src src/question3/Question3.java ``

Running:
~~~~~~~~

``java -cp bin/ question3.Question3 input/question3/question3.in``


Description of Solution:
------------------------

I chose the Mars Rover problem to submit. I completed the other three questions, but decided to submit Mars Rover because I felt it was the problem most suited to showing off OO design patterns.

My solution utilizes a main runner class (Problem3.java) that handles input and dispatches the Rover and Plateau objects purely to test input cases. It doesn't do much. The Rover class (Rover.java) represents a Mars Rover and is made up of a Position and Plateau object. The Plateau object is responsible solely for validation of moves. I chose to include Plateau inside a Rover object, rather then the other way around (A plateau containing many rovers) as it resulted in a more decoupled solution. The Position object is responsible handling the logic involved in moving and turning the Rover.

I've used immutability as often as the design allowed, without compromising readability. Whenever a rover moves, it's position is replaced by a new position, rather then changed in place. This makes it much easier to test. I've also used Enum classes wherever possible to represent Rover descriptions (direction and commands) to add some slight type safety and readability, rather then dealing with strings everywhere.

Assumptions:
------------
 - That if a Rover TRIES to move outside the Plateaus designated area it is a catastrophic failure and the program should be halted with a RuntimeException.

 - That input into the program from a file won't be large sized. I read the input file into a list container, rather then on the fly. If input was too large to be contained within memory the JVM will crash. I decided reading it into a List was fine for now as I cannot forsee input being that large. If required I could implement buffered reading using the BufferedReader class.

 - That an input file name will be passed into the program using the args array as the first parameter.




