include .env

# 開発用コンテナ起動。事前にdevcontainerをインストール：npm install -g @devcontainers/cli
run:
	sh .devcontainer/run_container.sh

stop:
	docker stop $(APP_NAME)
	docker rm $(APP_NAME)
	-docker network rm $(APP_NAME)_devcontainer_default

build:
	docker build --platform linux/amd64 --provenance false -t $(APP_NAME):latest .

push-dev:
	aws ecr get-login-password --region $(REGION) --profile $(AWS_PROFILE) | docker login --username AWS --password-stdin $(AWS_ECR_ACCOUNT)
	docker tag $(APP_NAME):latest $(DEV_ECR_REPOSITORY_URI):latest
	docker push $(DEV_ECR_REPOSITORY_URI):latest
	aws lambda update-function-code --region $(REGION) --profile $(AWS_PROFILE) --function-name $(APP_NAME) --image-uri $(DEV_ECR_REPOSITORY_URI):latest --publish