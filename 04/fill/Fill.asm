// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Pseudocode:
// blackens screen
//
// addr = SCREEN
// n = 8191
// i = 0
// LOOP
//    if i > n goto END
//    RAM[addr] = -1
//    addr = addr + 1
//    i = i + 1
//    goto LOOP
// END

  @SCREEN
  D=A
  @addr
  M=D
  @8191
  D=A
  @n
  M=D
  @i
  M=0
(LOOP)
  @i
  D=M
  @n
  D=D-M
  @END
  D;JGT
  @addr
  A=M
  M=-1
  @addr
  M=M+1
  @i
  M=M+1
  @LOOP
  0;JMP
(END)
  @END
  0;JMP
  
// LOOP
//   if KBD != 0
//     
//   goto LOOP
