if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

all_values = list(arr)
  
# new_list is a set of list1 
new_list = set(all_values) 
  
# removing the largest element from temp list 
new_list.remove(max(new_list)) 
  
# elements in original list are not changed 
# print(list1) 
  
print(max(new_list)) 