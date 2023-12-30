from random import randrange

def main():
    
    #obtain number of people participating
    number_people = get_int("How many people participate in the secret santa? ")
    if number_people % 2 != 0 or number_people == 0:
        raise Exception("The amount of people must be divisible by two (and non-zero)!")

    #put in names into a dictionary to track the number of times they were added
    dict_people = {}
    for t in range(number_people):
        person = input("Provide the name of the person participating, one-by-one: ")
        if person not in dict_people:
            dict_people[str(person)] = 1
        else:
            dict_people[str(person)] = dict_people[str(person)] + 1

    people = []
    for key in dict_people:
        if dict_people[key] == 1:
            people.append(str(key))
        else:
            for z in range(dict_people[key]):
                if z == 0:
                    people.append(str(key))
                else:
                    temp_person = str(key) + str(z)
                    people.append(temp_person)

    #check if number of people equals number in the beginning
    if len(people) != number_people:
        raise Exception("There is a different number of names put in than there are in the number")
    
    #create the pairs
    pairs = []
    while len(people)>=1:
        rand1 = pop_random(people)
        rand2 = pop_random(people)
        pair = rand1, rand2
        pairs.append(pair)

    #print out the pairs
    for i in range(len(pairs)):
        print("Pair "+str(i+1)+" is: "+str(pairs[i]))




def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please provide a number")




def pop_random(list): #from https://stackoverflow.com/questions/28748520/creating-random-pairs-from-lists
    nr = randrange(0, len(list))
    return list.pop(nr)




main()