def get_combinations(target, numbers):
    result = []
    numbers = sorted(numbers)
    
    def backtrack(remain, curr_combination, start):
        if remain == 0:
            result.append(curr_combination[:])
            return
        
        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i-1]:
                continue
                
            num = numbers[i]
            if num > remain:
                break
            
            curr_combination.append(num)
            backtrack(remain - num, curr_combination, i+1)
            curr_combination.pop()
    
    backtrack(target, [], 0)
    return result

input_num = int(input("Enter a target number: "))
input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

combinations = get_combinations(input_num, input_list)

if len(combinations) == 0:
    print("No valid combinations found.")
else:
    unique_combinations = set(tuple(sorted(comb)) for comb in combinations)
    print("Valid combinations:")
    for comb in unique_combinations:
        print(list(comb))
