# R2AE_DATABRICKS

## Introduction
Welcome to the DataBricks Project! This repository contains resources and tools for leveraging the power of DataBricks, a unified analytics platform designed to streamline data engineering, machine learning, and analytics tasks. Whether you’re a data engineer, data scientist, or analyst, this project aims to simplify your workflow and enhance productivity by harnessing the capabilities of DataBricks.

## What is DataBricks?
DataBricks is an enterprise cloud platform that provides a collaborative environment for big data analytics and machine learning. It integrates with Apache Spark to provide a scalable and high-performance solution for processing large datasets. DataBricks offers a range of features, including:

- Unified Analytics Platform: A collaborative workspace for data engineers and scientists.
- Interactive Notebooks: Support for multiple languages including Python, Scala, R, and SQL.
- Managed Clusters: Automated cluster management and scaling.
- MLflow Integration: Tools for managing the machine learning lifecycle.
- Delta Lake: ACID transactions and scalable metadata handling for reliable data lakes.

## Architecture

![Screenshot 2024-08-13 220622](https://github.com/user-attachments/assets/310b431f-5327-472d-8de7-c4e51f8cfe66)

## Setup and Start 

### 1. Create S3 Buckets
  
  Create the following S3 buckets:
1. r2ae-data-landing-stellar
2. r2ae-data-bronze-stellar
3. r2ae-data-silver-stellar
4. r2ae-data-gold-stellar

### 2. Upload Data Files
  
  Upload the **london_energy.csv** and **london_weather.csv** files to the **r2ae-data-landing-stellar** bucket.

### 3. IAM Configuration

1. Request **IAM** permissions for **S3AllAccess** to obtain the **Access Key** and **Secret Access Key**.
2. Save these keys securely; you will need them for configuring Databricks.

### 4. Set Up Databricks

1. Visit Databricks Website:
    - Go to [Databricks AWS Product Page](https://www.databricks.com/product/aws) and click on "**Try Databricks**."

      ![Screenshot 2024-08-14 010630](https://github.com/user-attachments/assets/d531e008-e24b-40cb-9847-f45ab14974ad)

2. Sign Up for a Free Trial:
    - Fill out the registration form.

      ![Screenshot 2024-08-14 011243](https://github.com/user-attachments/assets/e9459fee-c5e1-4601-946f-35139db9ff93)

    - You will receive a 14-day free trial.
      
3. Email Verification:
    - Check your email for a verification link.
    - Click the link, select the "**Premium Tier**," and provide a name for your Databricks Workspace.
    - Click "**Start quickstart**."

    ![Screenshot 2024-08-14 012250](https://github.com/user-attachments/assets/590491d5-f209-4dda-bcaf-40e854580c1d)

    
### 5. Configure Databricks on AWS

1. Access AWS Formalon:
    - Go to the AWS Formalon page provided in your Databricks setup instructions.

2. Create Stack:
    - Fill out the required information and click "**Create stack**."

3. Wait for Completion:
    - Wait until the Databricks stack status shows **CREATE_COMPLETE**.

### 6. Access Databricks Workspace

1. Log In:
    - Navigate to Databricks Workspace.
    - Log in using the credentials created during setup.

2. Open Workspace:
    - Click "**Open Workspace**" to access your Databricks environment.

### 7. Set Up Databricks Cluster

1. Create and Start Cluster:
    - Go to the Databricks workspace and create a new cluster if one is not already available.
    - Navigate to **Compute** -> **Create compute**

      ![Screenshot 2024-02-17 210922](https://github.com/user-attachments/assets/75bee505-d334-41df-99f0-7ac3bcb9d9c7)

    - **Create cluster**.
      
      ![Screenshot 2024-02-17 211828](https://github.com/user-attachments/assets/ab3353fa-6d5b-4af7-ae57-477afe9cda55)

### 8. Import Files into Databricks

1. Upload Files:
    - Import the files from the provided Git repository into your Databricks workspace.
    

### 9. Configure Secrets in Databricks

1. Update Secrets Configuration:
    - Open the notebook 01 : R2AE Databricks : Secrets.py.
    - In the cell labeled **Create S3_ACCESS_KEY** and **Create S3_ACCESS_SECRET**, input the **Access Key** and **Secret Access Key** obtained from **IAM**.
    - Run the cell and remove the keys once completed for security purposes.
      
### 10. Run Notebooks

1. Execute Cells:
    - Run all cells in the notebook.

### 11. Create Data Pipelines

1. Setup Data Pipeline:
    - Navigate to **Workflows** -> **Create job**.
    - Name your task and select the workspace.

      ![Screenshot 2024-02-18 013914](https://github.com/user-attachments/assets/138ad7e0-9c84-422d-9314-d536dde0d83b)


      ![Screenshot 2024-02-18 014035](https://github.com/user-attachments/assets/8081f743-b7bb-4be9-8ae2-02a16e098a6e)


      

Follow these steps carefully to configure and use your Databricks environment effectively. If you encounter any issues, consult the Databricks documentation or support for further assistance.
