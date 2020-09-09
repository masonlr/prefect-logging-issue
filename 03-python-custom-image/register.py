#!/usr/bin/env python


import prefect
from prefect import task, Flow
from prefect.environments.storage import Docker


@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("test message")


flow = Flow("python-custom", tasks=[hello_task])
base_image = "python-custom:latest"

flow.storage = Docker(base_image=base_image, local_image=True)
flow.register(project_name="test")
