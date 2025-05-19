FROM public.ecr.aws/lambda/python:3.13

WORKDIR ${LAMBDA_TASK_ROOT}

RUN pip install pdm

COPY pyproject.toml ./
COPY pdm.lock ./

RUN pdm install --global --project . --prod

COPY ./src ./

CMD [ "infrastructure.lambda_function.handler" ]