#verifies if all the input are strings that are in letters format and makes a list of numbers for each letters present
def analyze_input(sex1, sex2):
    if (not(isinstance(sex1, str)) and (not(isinstance(sex2, str)))):
        return "Both input are Wrong"
    elif (not(isinstance(sex1, str)) or (not(isinstance(sex2, str)))):
        return "one input is wrong"
    else:
        if not(sex1.isalpha()):
            return "input name 1 should contain only letters"
        elif not(sex2.isalpha()):
            return "Input name 2 should contain only letters"
        else:
            work_string = sex1 +"Loves"+ sex2
            action_string = work_string.lower()
            illiterate_string = action_string
            unique_letters = []
            computable_list = []
            for i in illiterate_string:
                if i not in unique_letters:
                    number = action_string.count(i)
                    unique_letters.append(i)
                    computable_list.append(number)
            computable_list.sort(reverse=True)
            return computable_list
    
#Receives the list and break it into two equal lists with the middle value aside for lists with odd number of items       
def list_computer(list):
    print(list)
    try:
        length = len(list)
        if (length % 2) == 0:
            spilt_point = int((length / 2))
            list1 = list[:spilt_point]
            list2 = list[spilt_point:]
            return list1, list2
        else:
            spilt_point = int(length / 2)
            list1 = list[:spilt_point]
            middle = list[spilt_point]
            list2 = list[(spilt_point + 1):]
            return list1, middle, list2
    except:
        return list

# calculates the list by adding the first item of first and last item of the second list then appending the mid value
def list_calculator(value):
    try:
        x = value
        if len(x) == 2:
            value1, value2 = x
            length1 = len(value1)
            list = []
            value2.reverse()
            for i in range(length1):
                z = value1[i] + value2[i]
                list.append(z)            
            return list
        elif len(x) == 3:
            value1, mid_value, value2 = x
            length1 = len(value1)
            list = []
            value2.reverse()
            for i in range(length1):
                z = value1[i] + value2[i]
                list.append(z)
            list.append(mid_value)            
            return list
        else:
            return "Internal Error"
        return x  
    except:
        return value
#verifies the results if it exceeds 100% it then computed again    
def ver_results(result):
    try:
        x, y = result
        corrected_list = []
        if not((x > 9) and (y > 9)):
            if x > 9:
                vue = str(x)
                list = []
                for i in vue:
                    list.append(int(i))
                corrected_list.extend(list)
                corrected_list.append(y)
            if y > 9:
                vue = str(y)
                list = []
                for i in vue:
                    list.append(int(i))
                corrected_list.extend(list)
                corrected_list.insert(0, x)
            return corrected_list
        elif (x > 9) and (y > 9):
            value1, value2 = str(x), str(y)
            list = []
            for i in value1:
                list.append(int(i))
            for i in value2:
                list.append(int(i))
            return list
        else:
            return 0
    except:
        return result

# breaks the tuple format Adds  the percentage to the computed value    
def percentile(tuples):
    try:
        x, y = tuples 
        value = str(x)+str(y)+str("%")     
        return value 
    except:
        return tuples
     
# calls the required function until the conditions are achieved      
def LoveCalc(input1, input2):
    initial_value = list_calculator(list_computer(analyze_input(input1, input2)))
    try:
        while (len(initial_value) > 2):
            initial_value = list_calculator(list_computer(initial_value))
        result = tuple(initial_value)
        initial_value1 = ver_results(result)
        if bool(initial_value1):
            while (len(initial_value1) > 2):
                initial_value1 = list_calculator(list_computer(initial_value1))
            return percentile(tuple(initial_value1)) 
        else:
            return percentile(tuple(initial_value))
    except:
        return initial_value
    
def ChangeToInteger(item):
    list1 = list(item)
    list1.remove("%")
    x, y  = tuple(list1)
    value = int(x + y)
    return value

def WhichIsGreater(value1, value2):
    if value1 > value2:
        return str(value1) + "%"
    else:
        return str(value2) + "%"

