
####################################################################
## convert CSV file to Delta 
## 
## requirements:
##      OpenJDK for access to Java and associated libraries (v11)
##      PySpark (Spark for Python) library (v 3.2.0)
##      Delta Spark open-source library 
## pythion libraries used:
##      pip install pyspark==3.2.0
##      pip install delta-spark==1.1.0
###################################################################
from pyspark.sql import SparkSession
from delta.tables import *

##create spark session with delta core 2.12 v1.1.0
sc  = SparkSession.builder \
    .master("local") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.1.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()


#input file location
cust_file = 'files/customers/customers-5M.csv'
#read file into spark session dataframe
df_cust = sc.read.options(header='True', inferSchema='True', delimiter=',').csv(cust_file)

#view the data 
#dataframe_csv.show() 

#write to delta format locaclly 
df_cust.write.format("delta").save("delta/customer/")



txn_file = 'csv_files/txn/txn-100M.csv'
df_txn = sc.read.options(header='True', inferSchema='True', delimiter=',').csv(txn_file)

#dataframe_csv.show()
df_txn.write.format("delta").save("delta/txn/")



