#import required modules 
import pandas as pd 
import numpy as np 

#create new data frame for beginning inventory balances
BegInvDF = pd.read_csv("D:\ACC470\BegInvFINAL.csv") 

#aggregate all records in beginning inventory, grouping by inventory ID and summing each quantity
BegInvDF = BegInvDF.groupby("InventoryId").sum()
BegInvDF = BegInvDF.reset_index()

#rename column header for aggregate beginning inventory to BegQty 
BegInvDF = BegInvDF.rename(columns = {"onHand" : "BegQty"})

#create new data frame that contains only the aggregate beginning inventory balances and inventory IDs
AggBegInvDF = BegInvDF[["InventoryId","BegQty"]]

#create new data frame for purchases transactions
PurchasesDF = pd.read_csv("D:\ACC470\PurchasesFINAL.csv")

#aggregate all transactions in purchases, grouping by inventory ID and summing each quantity
PurchasesDF = PurchasesDF.groupby("InventoryId").sum()
PurchasesDF = PurchasesDF.reset_index()

#create new data frame that contains only the aggregate quantities purchased and inventory IDs
AggPurchasesDF = PurchasesDF[["InventoryId","Quantity"]]

#rename column header for aggregate purchases to PurchQty 
AggPurchasesDF = AggPurchasesDF.rename(columns = {"Quantity" : "PurchQty"})

#create new data frame for sales transactions
SalesDF = pd.read_csv("D:\ACC470\salesFINAL.csv")

#aggregate all transactions in sales, grouping by inventory ID and summing each quantity
SalesDF = SalesDF.groupby("InventoryId").sum()
SalesDF = SalesDF.reset_index()

#create new data frame that contains only the aggregate quantities sold and inventory IDs
AggSalesDF = SalesDF[["InventoryId","SalesQuantity"]]

#rename column header for aggregate sales to SalesQty
AggSalesDF = AggSalesDF.rename(columns = {"SalesQuantity" : "SalesQty"})

#create new data frame for ending inventory balances
EndInvDF = pd.read_csv("D:\ACC470\EndInvFINAL.csv")

#aggregate all records in ending inventory, grouping by inventory ID and summing each quantity
EndInvDF = EndInvDF.groupby("InventoryId").sum()
EndInvDF = EndInvDF.reset_index()

#create new data frame that contains only the aggregate ending inventory balances and inventory IDs
AggEndInvDF = EndInvDF[["InventoryId","onHand"]]

#rename column header for aggregate sales to SalesQty
AggEndInvDF = AggEndInvDF.rename(columns = {"onHand" : "EndQty"})

#Merge the beggining inventory, purchases, sales, and ending inventory data frames on inventory ID
Merge1DF = pd.merge(AggBegInvDF, AggPurchasesDF, on = "InventoryId", how ="outer")
Merge2DF = pd.merge(Merge1DF, AggSalesDF, on = "InventoryId", how ="outer")
FinalMergeDF = pd.merge(Merge2DF, AggEndInvDF, on = "InventoryId", how ="outer")

#create a new column in the merged data frame called Diff that contains the difference between ending inventory quanitity reported by the client and recalculated amount
FinalMergeDF["Diff"] = FinalMergeDF["BegQty"] + FinalMergeDF["PurchQty"] - FinalMergeDF["SalesQty"] - FinalMergeDF["EndQty"]

#display new column in merged data frame called Diff along with previous columns in merged data frame
total = FinalMergeDF["Diff"].sum() 
total = round(total) 
print(str("The total difference is ") + str(total)) 

#display the total number of records in ending inventory
print("The total number of records in ending inventory " + str(FinalMergeDF.shape[0])