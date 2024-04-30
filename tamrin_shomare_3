dict = {"a_1": "None","a_2":"None","a_3":"None",
        "b_1":"None","b_2":"None","b_3":"None",
        "j_1":"None","j_2":"None","j_3":"None",
        "d_1":"None","d_2":"None","d_3":"None"
}
dict["a_3"]= "True"   #صورت سوال گفته

def input_1 (x):
    dict[x] = input(f"pls enter the answer {x} is True or False :")
    if dict[x] == "True" or dict[x] =="False":
        pass
    else:
        dict[x] = "None"
        print("enter again")
        input_1(x)

input_1("a_2")
def meow():
    if dict["a_2"] == "True":
        dict["b_3"] = "False"
        dict["j_2"]="False"
        dict["b_1"]="True"
        if dict["b_1"]=="True":
            dict["d_1"]= "False"
        dict["d_3"]= "False"
        if dict["d_3"]== "False":
            dict["b_2"]= "True"
        input_1("j_3")
        if dict["j_3"]== "True":
            dict["d_2"]="False"
        else:
            dict["d_2"]="True"
        input_1("j_1")
        if dict["j_1"]== "True":
            dict["a_1"]="False"
        else:
            dict["a_1"]="True"
        print(dict)
        print("ba tavajo be javab ha b moojrem ast")
    elif dict["a_2"] == "False":
        dict["b_3"] = "True"
        dict["j_2"]="True"
        dict["b_1"]="False"
        if dict["b_1"]=="False":
            dict["d_1"]= "True"
        dict["d_3"]= "True"
        if dict["d_3"]== "True":
            dict["b_2"]= "False"
        input_1("j_3")
        if dict["j_3"]== "False":
            dict["d_2"]="True"
        else:
            dict["d_2"]="False"
        input_1("j_1")
        if dict["j_1"]== "False":
            dict["a_1"]="True"
        else:
            dict["a_1"]="False"
        print(dict)
        print("tedad true = 7  false = 5 ta shod  va in khalaf sorat soale pas bazam b mojrem ast")
meow()





