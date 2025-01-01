include .env

build:
	docker build --platform linux/amd64 --provenance false -t $(IMAGE_NAME):latest .

push-dev:
	aws ecr get-login-password --region $(REGION) --profile $(AWS_PROFILE) | docker login --username AWS --password-stdin $(AWS_ECR_ACCOUNT)
	docker tag $(IMAGE_NAME):latest $(DEV_ECR_repository_Uri):latest
	docker push $(DEV_ECR_repository_Uri):latest

