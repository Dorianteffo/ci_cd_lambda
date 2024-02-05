up: 
	docker compose up --build -d

format: 
	docker exec lambda_job python -m black -S --line-length 79 .

isort:
	docker exec lambda_job isort .

type:
	docker exec lambda_job mypy --ignore-missing-imports .


lint: 
	docker exec lambda_job flake8 .


ci: isort format type lint 


infra-init: 
	docker compose -f docker-compose.yaml run --rm terraform -chdir=./terraform init

infra-apply: 
	docker compose -f docker-compose.yaml run --rm terraform -chdir=./terraform apply --auto-approve

infra-down: 
	docker compose -f docker-compose.yaml run --rm terraform -chdir=./terraform destroy --auto-approve

down: 
	docker compose down