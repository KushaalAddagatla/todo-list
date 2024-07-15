# Todo List App Documentation

## Overview of Tech Stack and Architecture

### Tech Stack

- **Frontend:**
  - **React:** A JavaScript library for building user interfaces, enabling dynamic and responsive web applications using components and state management.
  - **Fetch API:** A built-in JavaScript method used to make network requests to the backend for retrieving and manipulating data.

- **Backend:**
  - **Django:** A high-level Python web framework that promotes rapid development and clean design, providing a robust RESTful API for the frontend.
  - **Django REST Framework (DRF):** A powerful toolkit for building Web APIs, simplifying the process of creating a RESTful API with Django.

### Architecture

The application architecture consists of two main components:

1. **Frontend (React):**
   - The frontend application interacts with users, displaying the list of todos and allowing users to create, update, and delete todos.
   - It communicates with the backend via RESTful API calls to retrieve and manipulate data without using a traditional database.

2. **Backend (Django):**
   - The backend serves as the API provider, managing todo items in memory and processing requests from the frontend.
   - It exposes endpoints for CRUD operations on todo items, storing them temporarily in a list.


## Deployment Process to AWS

### Step 1: Deploying the React App on AWS S3

1. **Build the React App:**
   - Run the following command in your React project directory to create a production build:
     ```bash
     npm run build
     ```

2. **Create an S3 Bucket:**
   - Go to the AWS Management Console and navigate to the S3 service.
   - Create a new bucket, ensuring that the bucket name is globally unique.
   - Select the appropriate region and keep the default settings for the rest of the configuration.

3. **Configure Bucket for Static Hosting:**
   - After creating the bucket, go to the bucket's properties.
   - Enable "Static website hosting" and specify `index.html` as the index document.

4. **Upload Build Files:**
   - Upload the contents of the build folder generated from the React build process to the S3 bucket.

5. **Set Permissions:**
   - Configure the bucket policy to allow public access to the files. Here’s the policy:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadGetObject",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::assignment-todo-list-react/*"
         }
       ]
     }
     ```

### Step 2: Deploying the Django App on AWS EC2

1. **Launch an EC2 Instance:**
   - Go to the EC2 service in the AWS Management Console.
   - Launch a new instance using an Amazon Machine Image (AMI) with Ubuntu or Amazon Linux.
   - Choose an instance type (e.g., `t2.micro` for free tier).

2. **Configure Security Group:**
   - Set rules to allow HTTP (port 80) and HTTPS (port 443) traffic, as well as SSH (port 22) for accessing the instance.

3. **Connect to the EC2 Instance:**
   - Use SSH to connect to your instance:
     ```bash
     ssh -i "todo-list-react.pem" ubuntu@ec2-3-83-65-180.compute-1.amazonaws.com
     ```

4. **Set Up the Django Environment:**
   - Update the package list and install necessary packages:
     ```bash
     sudo apt update
     sudo apt install python3-pip python3-venv
     ```

   - Create a virtual environment and activate it:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - Install Django and Django REST Framework:
     ```bash
     pip install django djangorestframework django-cors-headers
     ```

5. **Deploy the Django Application:**
   - Clone your Django project from your repository or upload it directly to the EC2 instance.
   - Set up your Django project (e.g., configure `settings.py`, create views and URLs):
     ```bash
     cd your-django-project
     python manage.py runserver 0.0.0.0:8000
     ```

### Step 3: Connecting Frontend and Backend

1. **Update React API Endpoints:**
   - Ensure your React app is using the public DNS or IP of your EC2 instance for API calls.



