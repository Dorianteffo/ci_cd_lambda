variable "bucket_name" {
  type        = string
  default     = "movie-api-data-daily"
}

variable "lambda_ecr_repo" {
  type        = string
  default     = "ecr-repo-lambda"
}

variable "eventbridge_rule" {
  type        = string
  default     = "run_daily"
}

variable "lambda_iam_role_name" {
  type        = string
  default     = "s3_cloudwatch_ecr_lambdarole"
}




