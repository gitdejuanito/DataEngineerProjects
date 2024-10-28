Hi All,

In this Project the data sources come from some csv files from a GitHub. This Project do a Lakehouse transformations with Azure Services

1. First, I use Azure Data Factory (ADF) for getting the files from the web with HTTP linked services to each website, then I copy the files to an Azure Data Lake to a "raw" directory.

2. The next step is to use Databricks to do basic transformations and then I load the files to a "processed" container.

3. I créate a database in Azure Synapse and do UI CETAS (without code) for populating the database.
