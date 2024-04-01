u_1= """
ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKey
ContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumtel
eportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversarblockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital
 signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati...
"""
l=("and","is","in","def","as","yield","assert","break","class","continue","except","finally","for","or","from","global","import",
"nonlocal","pass","raise","return","try","while","with","del","elif","if","else","not","True","False","None","async","lambda","await",)
a=[]
b=[]
c=[]
d=[]
def clue_decrypt(text):
    
    for i in l:
        if i  in text:
            a.append(i) 
    print(a)

u_2=( 1233,0,"",[],{},'False','0','None',None,-1,[1, 2, 3],"{'key': 'value'}",True,' ','[]','[1, 2, 3]','[]','[1, 2, 3]',"{}","{'a': 1}",'True','ali','1234',1,0.1,-0.1,True,' ','[]','[1, 2, 3]',"{}","{'a': 1}",'True','ali','1234',1,0.1,-0.1,True,' ','[]','[1, 2, 3]',"{}","{'a': 1}",'True','ali','1234',1,0.1,-0.1, )
def puzzles_solve(puzzles):
    
    for i in puzzles:
        if i:
            # print(f"salam {i}")
            b.append("True")
        else:
            # print(f"bye {i}")
            b.append("False")
    print(b)

clue_decrypt(u_1)
print("---------- \n --------- \n")
puzzles_solve(u_2)

def numbers_magic_calculate(start,end ):
    end_1= end +1
    for i in range(start,end_1):
        c.append(i)
    print(c)
    
magic_number_1= int(input("enter the start of magic number"))
magic_number_2= int(input("enter the end of magic number"))
numbers_magic_calculate(magic_number_1,magic_number_2)
from random import randint
t=0
f=0
import time
timer = time.time()

def numbers_exam():
    global t
    global f
    x=randint(0,15)
    while (time.time() - timer)<20:
        if x==1:
            x=int(input("0001 = ?  :"))
            if x==1:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==2:
            x=int(input("0010 = ?  :"))
            if x==2:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==3:
            x=int(input("0011 = ?  :"))
            if x==3:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==4:
            x=int(input("0100 = ?  :"))
            if x==4:
                t+=1
                numbers_exam()
                
            else:
                f+=1
                numbers_exam()
        elif x==5:
            x=int(input("0101 = ?  :"))
            if x==5:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==6:
            x=int(input("0110 = ?  :"))
            if x==6:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==7:
            x=int(input("0111 = ?  :"))
            if x==7:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==8:
            x=int(input("1000 = ?  :"))
            if x==8:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==9:
            x=int(input("1001 = ?  :"))
            if x==9:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==10:
            x=int(input("1010 = ?  :"))
            if x==10:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==11:
            x=int(input("1011 = ?  :"))
            if x==11:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==12:
            x=int(input("1100 = ?  :"))
            if x==12:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==13:
            x=int(input("1101 = ?  :"))
            if x==13:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==14:
            x=int(input("1110 = ?  :"))
            if x==14:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==15:
            x=int(input("1111 = ?  :"))
            if x==15:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
        elif x==0:
            x=int(input("0000 = ?  :"))
            if x==0:
                t+=1
                numbers_exam()
            else:
                f+=1
                numbers_exam()
numbers_exam()
print(f"your time is over and the result T = {t} and F = {f}")



def check_pass(k):

    list_users= {}
    for i in range(k):
        key = input(f"the user {i+1} pls enter your username :")
        password = input(f"the user {i+1} pls enter your pass :")
        list_users.update({key: password})
    pun_list = '…{}()[]“”!?-;:,.'

    for i in list_users.values():

        if len(i) >= 8:
            check_lower = "False"
            for j in i:
                try:
                    j = int(j)
                    pass
                except:
                    if j in pun_list:
                            pass
                    elif j == j.lower():
                        check_lower = "True"
                        break
                    else:
                        pass
            if check_lower == "False":
                pass
            elif check_lower == "True":
                check_upper = "False"
                for j in i:
                    try:
                        j = int(j)
                        pass
                    except:
                        if j in pun_list:
                            pass
                        elif j == j.upper():
                            check_upper = "True"
                            break
                        else:
                            pass
                if check_upper == "False":
                    pass
                else:
                    for j in i:
                        if j in pun_list:
                            for key,value in list_users.items():
                                if value == i:
                                    d.append(key)
                                    print(f"the user with true pass : {d}")
                            break
        else:
            pass
check_pass(2)
import turtle
def la(meow):
    meow.forward(20)
    meow.left(90)
    meow.forward(60)
    meow.penup()
    meow.goto(0,0)
    meow.pendown()
    meow.forward(60)
    meow.penup()
def tar(meow):
    meow.goto(-30,40)
    meow.pendown()
    meow.right(180)
    meow.forward(40)
    meow.right(90)
    meow.forward(30)
    meow.left(45)
    meow.forward(70)
    meow.penup()
def dot(meow):
    meow.goto(-43,20)
    meow.pendown()
    meow.circle(2)
    meow.penup()
    meow.goto(-50,20)
    meow.pendown()
    meow.circle(2)
    meow.penup()
    meow.goto(-180,-20)
    meow.pendown()
    meow.circle(2)
def ji(meow):
    meow.penup()
    meow.goto(-200,35)
    meow.pendown()
    meow.forward(30)
    meow.left(180)
    meow.forward(30)
    meow.right(80)
    meow.forward(40)
    meow.right(100)
    meow.forward(60)
    meow.left(110)
    for i in range(20):
        if i <5:
            meow.forward(i+2)
            meow.right(i) 
        elif i <10:
            meow.forward(i+7)
            meow.right(i+10) 
        else:
            meow.forward(i+5)
            meow.right(i+2) 

def turtle_meow():
    my_turtle = turtle.Turtle()
    la(my_turtle)
    tar(my_turtle)
    dot(my_turtle)
    ji(my_turtle)
    
    turtle.done()

    
turtle_meow()
clue=[]
clue.append(a)
clue.append(b)
clue.append(c)
clue.append(f)
clue.append(d)

def vault_unlock(clues):
    finall=[]
    finall.append(clues[0][0][0])
    finall.append(clues[1][0][0])
    finall.append(clues[2][0])
    finall.append(clues[3])
    try:
        finall.append(clues[4][0][0])
        print(finall)
        print(f"the password is : { finall[0]}{finall[1]}{finall[2]}{finall[3]}{finall[4]}")
        

    except:
        
        print(finall)
        print(f"the password is : { finall[0]}{finall[1]}{finall[2]}{finall[3]}")
vault_unlock(clue)