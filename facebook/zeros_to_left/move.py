def move_zeros_to_left(arr):
  A = arr
  read = write = len(A) - 1
  while read >= 0:
    if read != 0:
      A[write] = A[read]
      write -= 1
    read -= 1
  for i in range(write):
    A[i] = 0
  return A

A = [1,10,20,0,59,63,0,88,0]
print(move_zeros_to_left(A))