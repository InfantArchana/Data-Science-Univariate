class Univariate():
	#obj = Univariate()

	# Seperate the Quantitative and Qualitative Data
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
		
	# Frequency Table
	def Frequency_Table(ColumnName, dataset):
	    Frequency_Table = pd.DataFrame(columns=("Unique_values", "Frequency", "Relative_Frequency", "Cumsum"))
	    Frequency_Table["Unique_values"] = dataset[ColumnName].value_counts().index
	    Frequency_Table["Frequency"] = dataset[ColumnName].value_counts().values
	    Frequency_Table["Relative_Frequency"] = (Frequency_Table["Frequency"] / Length_Count)
	    Frequency_Table["Cumsum"] = Frequency_Table["Relative_Frequency"].cumsum()
	    return Frequency_Table
		
	# Univariate continuous calculation - Measure of Central Tendency, Measure of Location of Data and Measure os Spread  
	def Univariate(dataset, Quan):
	    descriptive = pd.DataFrame(index=["Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%", "99%", "Q4:100%", 
                                  "IQR", "1.5rule", "Lower_Bound", "Upper_Bound", "Min", "Max", "skew", "kurtosis",
                                 "Var", "Std_Dev"], columns=Quan)
    for ColumnName in Quan:
        descriptive[ColumnName]["Mean"] = dataset[ColumnName].mean()
        descriptive[ColumnName]["Median"] = dataset[ColumnName].median()
        descriptive[ColumnName]["Mode"] = dataset[ColumnName].mode()[0]
        descriptive[ColumnName]["Q1:25%"] = dataset.describe()[ColumnName]["25%"]
        descriptive[ColumnName]["Q2:50%"] = dataset.describe()[ColumnName]["50%"]
        descriptive[ColumnName]["Q3:75%"] = dataset.describe()[ColumnName]["75%"]
        descriptive[ColumnName]["99%"] = float(np.percentile(dataset[ColumnName],[99]))
        descriptive[ColumnName]["Q4:100%"] = dataset.describe()[ColumnName]["max"]
        descriptive[ColumnName]["IQR"] = descriptive[ColumnName]["Q3:75%"] -  descriptive[ColumnName]["Q1:25%"]
        descriptive[ColumnName]["1.5rule"] = 1.5 * descriptive[ColumnName]["IQR"]
        descriptive[ColumnName]["Lower_Bound"] = descriptive[ColumnName]["Q1:25%"] - descriptive[ColumnName]["1.5rule"]
        descriptive[ColumnName]["Upper_Bound"] = descriptive[ColumnName]["Q3:75%"] + descriptive[ColumnName]["1.5rule"]
        descriptive[ColumnName]["Min"] = dataset[ColumnName].min()
        descriptive[ColumnName]["Max"] = dataset[ColumnName].max()
        descriptive[ColumnName]["skew"] = dataset[ColumnName].skew()
        descriptive[ColumnName]["kurtosis"] = dataset[ColumnName].kurtosis()
        descriptive[ColumnName]["Var"] = dataset[ColumnName].var()
        descriptive[ColumnName]["Std_Dev"] = dataset[ColumnName].std()
    return descriptive

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
			     
			    