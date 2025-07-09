# 🧑‍🎓 AWS Serverless Student Data App

A **fully serverless web application** built using AWS to collect and retrieve student data using HTML, JavaScript, Python, and DynamoDB.

This project demonstrates an event-driven, scalable, and cost-efficient application using modern cloud architecture.

---

## 🌐 Live Website

Click below to visit the live app:

🔗 http://devopsmasterbkt.s3-website.eu-north-1.amazonaws.com/ 
_(Hosted using S3 + CloudFront, powered by AWS)_


## ⚙️ Tech Stack

- 🗂️ **Amazon S3** – Static web hosting (HTML, CSS, JS)
- 🐍 **AWS Lambda** – Python functions for backend logic
- 🔁 **API Gateway** – Exposes RESTful endpoints (GET/POST)
- 🗃️ **DynamoDB** – Serverless NoSQL database
- 🌐 **CloudFront** – HTTPS + CDN + caching for secure & fast delivery

---

## ✨ Features

✅ Add new student data  
✅ Retrieve all student entries  
✅ Zero servers or containers  
✅ Works globally, scalable & secure  
✅ CloudFront for SSL and speed  

---

## 📁 Project Structure

aws-serverless-student-app/
├── index.html # Frontend interface
├── scripts.js # API call logic (GET & POST)
├── lambda/
│ ├── save_student.py # POST Lambda: Save data
│ └── get_students.py # GET Lambda: Fetch all data
└── README.md # You're reading it



---

## 🚀 How to Deploy on AWS

### 1. 🎨 Upload Frontend to S3
- Create a new S3 bucket
- Enable static website hosting
- Upload `index.html` and `scripts.js`

### 2. 🗃️ Set up DynamoDB
- Table name: `studentData`
- Primary key: `studentid` (String)

### 3. 🐍 Create Lambda Functions
- Function 1: `save_student.py`  
  ➤ Permission: `dynamodb:PutItem`
  
- Function 2: `get_students.py`  
  ➤ Permission: `dynamodb:Scan`

### 4. 🌐 Setup API Gateway
- Create a REST API:
  - `POST /` → `save_student` Lambda
  - `GET /` → `get_students` Lambda
- Enable **CORS** for both

### 5. 🔒 Configure CloudFront
- Origin: S3 bucket
- Enable HTTPS
- Connect to domain (optional)

---

## 🧠 Learnings

- AWS IAM roles and permissions
- Lambda event structures and error handling
- API Gateway integration and CORS
- Dynamically updating DOM with JavaScript
- Hosting secure apps using CloudFront

---

## 🛠️ Future Improvements

- Form validation before submitting
- Add delete/update operations
- Add AWS Cognito for login/authentication
- Add CI/CD using AWS SAM or GitHub Actions

---

## 🧑‍💻 Author

**Subrat Tandon**  
[GitHub](https://github.com/subrattandon) | [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📜 License

This project is licensed under the MIT License — feel free to use and build on it!

