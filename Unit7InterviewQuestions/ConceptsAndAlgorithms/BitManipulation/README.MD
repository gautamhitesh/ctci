1. Bits facts and tricks
   - X ^ 0s = X | e.g. 1011^0000= 1011
   - X ^ 1s = ~X | e.g 1011^1111= 0100
   - X ^ X = 0 
2. Two complements and negative numbers
   - Negative numbers are stored as complement of 2
   - -3 ===> concat(1, 2(N-1)-3) ===> 1 + (8-3) = 1101
   - -6 ===> 1 + (8-6) ===> 1010
3. Arithmetic vs Logical Right Shift
   - Arithmetic shift is without sign bit
4. Common Bit Tasks
   1. Get Bit:  num & (1<<i) ==> will return 0 if 0 1 if 1
   2. Set Bit: num | (1<<i) ==> will set bit to 1 rest are masked
   3. Clear Bit: num & ~(1<<i)
   4. Update Bit: num & ~(1<<i) | value << i