class Univariate():
	#obj = Univariate()
		
	def QuanQual(dataset):
	    Quan=[]
	    Qual=[]
	    for ColumnName in dataset.columns:
	        #print(ColumnName)
	        if (dataset[ColumnName].dtypes=="O"):
	            #print("Qual")
	            Qual.append(ColumnName)
	        else:
	            #print("Quan")
	            Quan.append(ColumnName)
	    return Quan,Qual
		
	def Frequency_Table(ColumnName, dataset):
	    Frequency_Table = pd.DataFrame(columns=("Unique_values", "Frequency", "Relative_Frequency", "Cumsum"))
	    Frequency_Table["Unique_values"] = dataset[ColumnName].value_counts().index
	    Frequency_Table["Frequency"] = dataset[ColumnName].value_counts().values
	    Frequency_Table["Relative_Frequency"] = (Frequency_Table["Frequency"] / Length_Count)
	    Frequency_Table["Cumsum"] = Frequency_Table["Relative_Frequency"].cumsum()
	    return Frequency_Table

	def Univariate(dataset, Quan):

	def Find_Outlier(descriptive, Quan):
	    lesser = []
	    greater = []
	    for ColumnName in Quan:
	        if(descriptive[ColumnName]["Min"] < descriptive[ColumnName]["Lower_Bound"]):
	            lesser.append(ColumnName)
	        if(descriptive[ColumnName]["Max"] > descriptive[ColumnName]["Upper_Bound"]):
	            greater.append(ColumnName)
	    return lesser, greater

	def Replace_Outlier(descriptive, Quan):
	    for ColumnName in lesser:
	        dataset[ColumnName][dataset[ColumnName] < descriptive[ColumnName]["Lower_Bound"]]=descriptive[ColumnName]["Lower_Bound"]
	    for ColumnName in greater:
	        dataset[ColumnName][dataset[ColumnName] > descriptive[ColumnName]["Upper_Bound"]]=descriptive[ColumnName]["Upper_Bound"]
	    return descriptive
			     
			    