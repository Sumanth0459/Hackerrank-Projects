def count_substring(string, sub_string):
    
  ml=len(string)
  sl=len(sub_string)
  total=0
  for i in range(ml-sl+1):
    if string[i:(i+sl)]==sub_string:
        total+=1
  return total

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
  
  count = count_substring(string, sub_string)
  print(count)