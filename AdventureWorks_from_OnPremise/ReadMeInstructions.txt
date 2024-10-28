Hi All,

In this Project I use the AdventureWorksLT2019 database for doing ELT with Azure services.

1. I use SSMS for OnPremise database and link this database with a Self-Hosted IR (Integration Runtime) for the link with Data Factory and load the tables in the SSMS database.

2. I use this first time ADF for extracting the tables and load them into a Azure Data Lake Gen2(ADLS) with an LookUp, ForEach and Copy activities.

3. Then I use Databricks for doing transformations to the raw tables, creating new tables doing bronze, silver and gold layers (Lakehouse architecture), we mount the ADLS and load the gold tables in a gold directory in the container.

4. Finally, I créate views in Azure Synpase for analytical purposes.

