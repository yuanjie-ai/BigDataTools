echo "主文件：$1"
MAIN=$1
PYFILES=''
CLUSTER_NAME=zjyprc-hadoop # c3prc-hadoop-spark2.0
QUEUE=development.miui_group.browser.browser_bigdata
# $INFRA_CLIENT/bin/hdfs dfs -rm -r output
# spark 2.x only
spark-submit --cluster $CLUSTER_NAME \
--queue $QUEUE \
# --py-files *.zip/*.py \
--master yarn-cluster \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON='/opt/soft/anaconda2/bin/python'  \
--conf spark.disable.stdout=false \
--conf spark.yarn.job.owners=yuanjie \
--executor-cores 2 \
--driver-memory 6g \
--num-executors 60 \
--executor-memory 6g \
MAIN
