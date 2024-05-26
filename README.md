# Amazon-DSP-ROAS-Management

## Objective

This project aims to automate and optimise a ROAS driven amazon DSP campaign based on real-time KPI analysis (ROAS) across 1 market: UK using AWS services.

## Components and AWS Services

1. **Data Ingestion**: Amazon Kinesis
2. **Data Storage**: Amazon S3
3. **Data Processing**: AWS Lambda, AWS Glue
4. **Database**: Amazon RDS, Amazon DynamoDB
5. **Analytics and Monitoring**: Amazon QuickSight
6. **Automation**: Amazon CloudWatch
7. **High Availability & Fault Tolerance**: Elastic Load Balancing, Auto Scaling groups
8. **Disaster Recovery**: AWS Backup, Cross-region replication for S3 buckets

## Project Structure

- `src`: Contains the source code for different components.
  - `data_ingestion`: Kinesis producer and consumer scripts.
  - `data_processing`: Lambda function and Glue job scripts.
  - `automation`: CloudWatch automation scripts.
  - `database`: SQL script for creating tables in RDS.
  - `infrastructure`: Scripts to set up AWS infrastructure components.

## Setup Instructions

1. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set Up Infrastructure**:
    Run the infrastructure setup scripts to create VPC, S3 buckets, RDS, DynamoDB, Kinesis streams, Lambda functions, Glue jobs, CloudWatch alarms, and QuickSight.
    ```bash
    python src/infrastructure/vpc_setup.py
    python src/infrastructure/s3_bucket_setup.py
    python src/infrastructure/rds_setup.py
    python src/infrastructure/dynamodb_setup.py
    python src/infrastructure/kinesis_setup.py
    python src/infrastructure/lambda_setup.py
    python src/infrastructure/glue_setup.py
    python src/infrastructure/cloudwatch_setup.py
    python src/infrastructure/quicksight_setup.py
    python src/infrastructure/backup_setup.py
    ```

3. **Run Data Ingestion**:
    Start the Kinesis producer to simulate data streaming.
    ```bash
    python src/data_ingestion/kinesis_producer.py
    ```

4. **Data Processing and Automation**:
    Ensure that Lambda and Glue jobs are correctly set up and triggered by incoming data and CloudWatch alarms.

5. **Monitoring and Analytics**:
    Set up Amazon QuickSight for data visualization and monitor CloudWatch for automation.

## AWS Services Used

- **Amazon Kinesis**: For real-time data streaming.
- **Amazon S3**: For scalable data storage.
- **AWS Lambda**: For serverless data processing.
- **AWS Glue**: For ETL tasks.
- **Amazon RDS**: For structured data storage.
- **Amazon DynamoDB**: For NoSQL data storage.
- **Amazon QuickSight**: For data visualization.
- **Amazon CloudWatch**: For monitoring and automation.
- **Elastic Load Balancing**: For distributing incoming traffic.
- **Auto Scaling Groups**: For automatic scaling.
- **AWS Backup**: For disaster recovery.
- **Cross-Region Replication**: For S3 bucket replication.

