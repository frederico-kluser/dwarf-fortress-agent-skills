# Adder (Computing)

> Fonte: [Adder (Computing)](https://dwarffortresswiki.org/index.php/Adder_(Computing)) — Dwarf Fortress Wiki (GFDL/MIT)

*For the species of snake, see Adder.*

Understanding of principles of addition are important to many dwarven logic devices. Addition can be used in devices to keep track of various values, such as the number of items in a stockpile, the number of years that have passed since a particular event, or more abstract computation.

Addition is simplest when dealing with binary values. Addition in other number bases is possible, but this article focuses on binary addition. Addition requires the choice of an arbitrary number of bits, or digits, to add, although numbers larger than the adder is designed for can be added via sequential additions with carry. For purposes of this discussion, the least significant digit will be considered the first or right-most digit.

Before beginning an adder, one should become familiar with the logic gates NOT, OR, XOR, and AND. Descriptions of these gates are available for mechanical, fluid, creature, and animal logic. Addition also requires values to add, which need to be stored in some kind of memory "memory").

# Incrementation

Simple designs typically do not require a full adder, but only incrementation or decrementation of a certain value-- adding or subtracting one from the value every time an event occurs.

### 1 bit incrementation

The simplest increment is a 1 bit increment-- that is, the addition of two single bit binary values. There are two possibilities: 0+1=1 and 1+1=10-- but since we have only a single bit, we abandon the higher bit, so 1+1=0. This table of values is the same table as a NOT operation. Note that our table of values for a decrement is identical to this as well-- a NOT is both a 1 bit increment and a 1 bit decrement.

### 2 bit incrementation

It's clear that a 1 bit increment isn't very useful. However, we can easily generate a carry from our 1 bit increment by considering the value of our 1st bit. When we increment our first bit, it will generate a carry affecting our 2nd bit if and only if our first bit is 1 (true), so by XORing our second (more significant) bit with our first bit, we generate the proper value for our second bit. It's important to note that this XOR must be carried out on the original value of the first bit, rather than the incremented (NOT) value!

### 2 bit decrementation

With 2 bits, decrementation becomes slightly different from addition, but not by much. The difference is just that we will generate a carry only if our first bit is 0! Thus, our second digit becomes equal to \[2\]XOR(NOT\[1\]), rather than \[2\]XOR\[1\].

### 3 or more bit incrementation or decrementation

When we reach 3 or more bits, we need to add an additional layer of complexity. Consider what would happen if we incremented 1101: if we just \[4\]XOR\[3\] (XOR of our 4th bit with our 3rd bit), we would mistakenly find the value as 0110, rather than 1110. We need to make our carries propagate through the system properly. A dedicated incrementer can build this functionality into its bits, by incrementing the next higher bit every time it changes from 1 to 0, but not when it changes from 0 to 1. This process can be described logically by implementing a new carry bit, and working from the right, using the following algorithm (this isn't any particular language, it's just pseudocode:)

`set [carry] equal to [1]  -- if our first bit is 1, begin a carry`\
`[1] becomes equal to NOT[1] -- our first bit inverts its value`\
`set n equal to 2  -- move to the next bit position`\
`while n. An 8-bit hybrid system is demonstrated at .

### n bit subtract

Subtracting, again, is remarkably similar to addition. Here, however, we have to consider that subtraction is not commutative, so we have to consider than one value is being subtracted from the other. We will consider our second value, represented by n' bit positions, to be the subtrahend, the value that is subtracted from the first value (minuend).

Again, the basis of subtraction is the XOR operation. Consider the four possibilities for a given bit: 0-0=0, 1-0=1, 0-1=-1=1, 1-1=0. The difference is how we treat our carry. For our first, rightmost bit, we begin by setting our carry to 0 (false). After that, we generate a carry either if both our carry and subtrahend are 1, and if our minuend is zero and either our carry or subtrahend is 1. In other words, our carry for our first bit is equal to (\[carry\]AND\[1'\])OR(NOT\[1\]AND(\[carry\]OR\[1'\])). This works for subtractions of any length.

## Add with carry

In the previous examples, it's been clear that our values were at risk of rolling over. For instance, adding 1 to 1111 results in 0. Traditional (non-dwarven) computers typically have both an add and an add with carry function. The two combined allow the addition of values larger than the bit length.

Adding with carry begins with a simple add of the lowest chunk of two particular values. For instance, given the values 000001 and 001111, we might start with the lowest three digits of each, the 001 and the 111, and add them, which results in 000. However, for our next add, we will preserve the carry generated by the last (third) bit of the addition, rather than discarding it at the beginning of our next carry. Now, we add the next three digits of each value (000 and 001), but include the carry from our previous addition. These sequential additions gives us the proper value (010000) without sufficient bit length to add each value otherwise.

A system capable of both addition and add-with-carry is considered a full adder. Full adders, even 1-bit full adders, can add values of any bit length. For an example using fluid logic, see User:Kyace/Adder.

## Look-ahead carry

While a simple adder is capable of reliable addition, it can be extremely slow. Consider a 8-bit adder: the value of the 8th bit depends on the carry derived from the 7th bit, which in turn depends on the carry derived from the 6th bit, and so on. The entire addition has to be carried out sequentially, rather than adding the bits in parallel. Because of the way the carry ripples through the value, such systems are called *ripple carry adders.* When water or creatures are used in the circuits, this can mean a day or more to add two 8 bit values. However, the process can be improved considerably, at the expense of greater complexity, by implementing a look-ahead system.

Look ahead systems break the values up into sequences of bits, based on the fact that if both values of the nth bit are 0 ((NOT\[n\])AND(NOT\[n'\])), any carry will end at that bit, and that if both values are 1 (\[n\]AND\[n'\]), that bit will generate a carry. Based on this, it's possible to process, in parallel, the addition of various bit-lengths based on the knowledge that carries will not propagate past a carry-ending bit. This can vastly improve the time necessary to add two values.

Jong's dwarven computer uses look-aheads for faster addition, and is capable of add-with-carry. The design can be further compressed to a very compact and versatile full adder: User:Larix/Adder. For an example using creature logic, see Look-ahead Add.

## Multiplication and division

While beyond the scope of this article, similar logical tools can be used to multiply or divide two values. In the simplest (but slowest) implementation, either can be represented by sequential addition or subtraction, integrating an adder with a counter. It can also be done using Egyptian multiplication and division.

- User:BaronW's page demonstrates the action of just such an awe-inspiring mechanical calculator.
