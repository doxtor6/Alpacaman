# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:37:48 2023

@author: timmy
"""

from ast import Delete
import time
import readline 
from xml.sax.xmlreader import InputSource
import databasecode
import generate
import os
import json
import finetune
def write_list(a_list,memoryfile):
    # store list in binary file so 'wb' mode
    with open(memoryfile, 'w') as fp:
        fp.write(json.dumps(a_list))
def read_list(memoryfile):
    # for reading also binary mode is important
    if os.stat(memoryfile).st_size == 0: return []
    with open(memoryfile, 'r') as fp:
        n_list = json.load(fp)
        return n_list

def makeatake():
    inputtest = input("Enter your input:")
    User = "User"
    t = time.localtime()
    current_time = time.strftime("%D,%H:%M:%S", t)
    databasecode.savedanmu([[User,current_time,inputtest]])

def prepareprompter():
    t = time.localtime()
    current_time = time.strftime("%D,%H:%M:%S", t)
    insbegin = "\n\n### Instruction:\n"
    resbegin = "\n\n### Response:\n"
    pastmessage = databasecode.readdamu(5)
    finalinstruction = ""
    counter = 0
    for i in pastmessage:
        if i[1]!= "alpacaman": 
            finalinstruction = insbegin + i[3] + finalinstruction
        else:
            counter+=1
            if i[3]!="": finalinstruction = resbegin + i[3] + finalinstruction
    finalinstruction = "Current time:" + current_time +finalinstruction
    return finalinstruction,counter
    

def main():
    makeatake()
    text = prepareprompter()[0]
    outputtemp = generate.evaluate(text)
    resbegin = "\n\n### Response:\n"
    insbegin = "\n\n### Instruction:\n"
    for i in outputtemp:
        try:
            output = next(outputtemp)
            stateonly = (output.split(resbegin)[prepareprompter()[1]+1]).split(insbegin )[0].strip()
            if "###" in stateonly: break
        except:
            break
    stateonly = stateonly.split("\n\n###")[0]
    print(stateonly)
    outputtemp = ""
    t = time.localtime()
    current_time = time.strftime("%D,%H:%M:%S", t)

    finetunelist = [{"instruction":text,"input": "","output":stateonly }]
    write_list(finetunelist,"alpacaman_data.json")
    boolfinetune = input("Do you want to finetune this conversation, (You can modify the 'output' in alpacaman_data.json at this moment to inject memory.): (Y/N)")
    if boolfinetune =="Y":
        nepch = input("Enter the number of epochs for finetune. A large number means this conversation is harder to forget.（Recommend 10 as default)： ")
        inputjson = read_list("alpacaman_data.json")
        databasecode.savedanmu([["alpacaman",current_time,inputjson[0]["output"]]])
        finetune.train(generate.modelforfinetune,num_epochs = int(nepch))
    else:
        databasecode.deletelastdanmu()

    

if __name__ == "__main__":
    while True:
        main()