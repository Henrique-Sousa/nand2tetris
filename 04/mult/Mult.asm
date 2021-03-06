// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Pseudocode:
//   i = 1
//   sum = 0
//   n = R1
// LOOP
//   if i > n goto STOP
//   sum = sum + R0
//   i = i + 1
//   goto LOOP
// STOP
//   R2 = sum


  @i
  M=1     // i = 1
  @sum
  M=0     // sum = 0
  @R1
  D=M
  @n
  M=D     // n = R1
(LOOP)
  @i
  D=M
  @n
  D=D-M
  @STOP
  D;JGT   // jump to STOP if (i - n == 0)
  @R0
  D=M
  @sum
  M=D+M   // sum = sum + R0
  @i
  M=M+1   // i = i + 1
  @LOOP
  0;JMP
(STOP)
  @sum
  D=M
  @R2
  M=D     // R2 = sum
(END)
  @END
  0;JMP
