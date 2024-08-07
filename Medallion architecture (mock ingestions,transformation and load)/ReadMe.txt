Hi ! This is a small Project about Medallion Architecture using DataBricks Community Edition, thats why all my resources are DataFrames, due to in Community Edition the use of a cluster is free and it just lives 2 hours, after 2 hours each of your tables will delete with the cluster.

This Project was made in order to understand the basic transformations that can be done with Databricks using Pyspark. (Files in bronze directory are mock files without any meaning).

I better used DBFS, you can upload files and convert them into dataframes for manipulations.


Notes:
Each of the paths I used are the paths in my DBFS, yours should be different, in the Bronze directory you can download the files that were used for this Project.

For understanting what Im doing please refer to "Instructions of architecture" directory,there are some images describing which transformation are needed to be done for  Bronze to Silver and  Silver to Gold. 