FROM public.ecr.aws/lambda/python:3.13

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

COPY ./src ${LAMBDA_TASK_ROOT}/src
RUN mv ./src/lambda_function.py ./lambda_function.py

CMD [ "lambda_function.handler" ]