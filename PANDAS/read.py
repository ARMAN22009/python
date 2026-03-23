import pandas as pd

dataframe=pd.read_csv("C:\\Users\\Arman\\Downloads\\subs.csv")
print(dataframe)
print(type(dataframe))                                          # now it is a dataframe

# dataframe1=pd.read_csv("C:\\Users\\Arman\\Downloads\\subs.csv",squeeze=True)
# print(dataframe1)
# print(type(dataframe1))                                        #                         


resume ={
    "name":"Arman",
    "age":20,
    "sex":"male",
}

print(pd.DataFrame(resume))