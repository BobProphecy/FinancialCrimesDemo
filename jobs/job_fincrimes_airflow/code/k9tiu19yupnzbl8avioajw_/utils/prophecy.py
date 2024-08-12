from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/pipe_financial_crimes": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipe_financial_crimes-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {"pipelines/pipe_financial_crimes" : "pipe_financial_crimes"}
