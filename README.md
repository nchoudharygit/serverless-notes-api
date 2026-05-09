# Serverless Notes API

A serverless REST API built with **AWS Lambda**, **API Gateway**, and **DynamoDB**, provisioned entirely using **AWS CloudFormation** as Infrastructure as Code.

---

## Architecture

```
Client (curl / Postman)
        |
        v
  API Gateway (REST API)
        |
        v
  AWS Lambda (Python 3.11)
        |
        v
  DynamoDB (Notes Table)
```

All infrastructure is defined and deployed using a single CloudFormation template (`template.yaml`).

---

## Tech Stack

| Layer            | Technology                  |
|------------------|-----------------------------|
| Compute          | AWS Lambda (Python 3.11)    |
| API              | Amazon API Gateway (REST)   |
| Database         | Amazon DynamoDB             |
| IaC              | AWS CloudFormation          |
| Language         | Python 3.11                 |
| Version Control  | GitHub                      |

---

## API Endpoints

| Method | Endpoint      | Description         |
|--------|---------------|---------------------|
| GET    | /notes        | List all notes      |
| POST   | /notes        | Create a new note   |
| GET    | /notes/{id}   | Get note by ID      |
| DELETE | /notes/{id}   | Delete a note       |

---

## Project Structure

```
serverless-notes-api/
├── template.yaml          # CloudFormation stack (IaC)
├── lambda/
│   └── handler.py         # Lambda function (Python)
├── README.md
└── .gitignore
```

---

## Deployment

### Prerequisites
- AWS CLI configured (`aws configure`)
- An S3 bucket to store the CloudFormation package (or deploy directly)

### Deploy Steps

**1. Clone the repo**
```bash
git clone https://github.com/nchoudharygit/serverless-notes-api.git
cd serverless-notes-api
```

**2. Deploy the CloudFormation stack**
```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name serverless-notes-api \
  --capabilities CAPABILITY_IAM \
  --region ap-south-1
```

**3. Get the API URL**
```bash
aws cloudformation describe-stacks \
  --stack-name serverless-notes-api \
  --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" \
  --output text
```

**4. Test the API**
```bash
# Create a note
curl -X POST https://YOUR_API_URL/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "My first note", "content": "Hello from Lambda!"}'

# List all notes
curl https://YOUR_API_URL/notes
```

---

## Infrastructure (CloudFormation)

The `template.yaml` provisions:
- **Lambda Function** — Python handler with IAM execution role
- **API Gateway** — REST API with GET and POST methods
- **DynamoDB Table** — On-demand billing, `noteId` as partition key
- **IAM Role** — Least-privilege role for Lambda to access DynamoDB

---

## Skills Demonstrated

- Serverless architecture design (Lambda + API Gateway)
- Infrastructure as Code with AWS CloudFormation
- AWS IAM — least-privilege role design
- Python scripting for AWS SDK (boto3)
- REST API design and testing
- Git workflow and documentation

---

## Author

**Neha Choudhary** — DevOps & Cloud Engineer
AWS Certified Cloud Practitioner (May 2026)
