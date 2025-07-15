from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AWS Serverless Web App - Deployment Guide (2025)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title("Project Overview")
pdf.chapter_body("This guide explains how to deploy the 'AWS Serverless Student Data App' using AWS services.\nIt allows users to submit and view student data using a serverless architecture involving S3, API Gateway, Lambda, DynamoDB, and CloudFront.")

pdf.chapter_title("1. Create S3 Bucket (for Frontend Hosting)")
pdf.chapter_body("1. Go to AWS Console > S3 > Create Bucket\n2. Bucket Name: e.g., serverless-student-app\n3. Disable Block All Public Access\n4. Enable Static Website Hosting (Properties tab)\n5. Upload `index.html` and `scripts.js`\n6. Note the 'Static Website Hosting' URL")

pdf.chapter_title("2. Create DynamoDB Table")
pdf.chapter_body("1. Go to AWS Console > DynamoDB > Tables > Create Table\n2. Table name: studentData\n3. Partition key: studentid (String)")

pdf.chapter_title("3. Create Lambda Functions (Python)")
pdf.chapter_body("1. Go to AWS Console > Lambda > Create Function\n2. save_student.py → POST\n3. get_students.py → GET\n4. Add permissions for DynamoDB access")

pdf.chapter_title("4. Create REST API using API Gateway")
pdf.
