FROM public.ecr.aws/lambda/python:3.13

RUN pip install pdm

COPY pyproject.toml ${LAMBDA_TASK_ROOT}
COPY pdm.lock ${LAMBDA_TASK_ROOT}

RUN pdm install --global --project . --prod

COPY ./src ${LAMBDA_TASK_ROOT}/src

CMD [ "src.infrastructure.lambda_function.handler" ]