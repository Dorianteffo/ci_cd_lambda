FROM public.ecr.aws/lambda/python:3.12

ARG AUTHORIZATION

ENV Authorization=${AUTHORIZATION}

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "api_data.lambda_handler" ]