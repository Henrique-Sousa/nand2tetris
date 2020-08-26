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
// MAIN
//    if KBD != 0
//      goto BLACK  
//    else 
//      goto WHITE    
// 
// BLACK   // blackens the screen
// addr = SCREEN
// n = 8191
// i = 0
// DRAW
//    if i > n goto MAIN
//    RAM[addr] = -1
//    addr = addr + 1
//    i = i + 1
//    goto DRAW
// 
// WHITE   // whitens the screen
// addr = SCREEN
// n = 8191
// i = 0
// CLEAR
//    if i > n goto MAIN
//    RAM[addr] = 0 
//    addr = addr + 1
//    i = i + 1
//    goto CLEAR

(MAIN)
  @KBD
  D=M
  @BLACK
  D;JNE
  @WHITE
  D;JEQ

(BLACK)
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
(DRAW)
  @i
  D=M
  @n
  D=D-M
  @MAIN
  D;JGT
  @addr
  A=M
  M=-1
  @addr
  M=M+1
  @i
  M=M+1
  @DRAW
  0;JMP
  
(WHITE)
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
(CLEAR)
  @i
  D=M
  @n
  D=D-M
  @MAIN
  D;JGT
  @addr
  A=M
  M=0
  @addr
  M=M+1
  @i
  M=M+1
  @CLEAR
  0;JMP
