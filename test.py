import mlflow
#mlflow.tensorflow.autolog()
mlflow.set_experiment("Users/srigandhan.v@cdsazure.onmicrosoft.com/MLFLOW_CLI_TEST")
mlflow.start_run()
mlflow.log_param("t1","t1")
mlflow.log_metric("m1",0.33)
mlflow.end_run()
