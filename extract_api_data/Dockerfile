FROM public.ecr.aws/lambda/python:3.12

ENV Authorization="Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTg3NWNjOTlkOGZhY2ZkZTg2OTJkMjk4MTQ5NjQ1YiIsInN1YiI6IjY1OTk5OGU4YmQ1ODhiMDFhOTU3M2FjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z0lbJN4SXfdHU9dJRlHGr7hO0HtvZagtMFD7l4L1W6E"

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "api_data.lambda_handler" ]