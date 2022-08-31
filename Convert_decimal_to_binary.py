def dtob(nums):
  if nums >= 1:
    binary = nums//2
  return (binary%2,"")
if __name__ == '_main_':
  print( dtob(4))
  print (dtob(4))
  print (dtob(4))
  print (dtob(4))
  
  
  
  
  
  #other method
  def bi(n):
    return bin(n).replace("0b","")
if __name__ == '__main__':
    print(bi(4))
    print(bi(6))
    print(bi(65))
    print(bi(1025))
  
  
  
