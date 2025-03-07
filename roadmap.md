# Founder Outreach App - Roadmap

## Overview
The Founder Outreach App automates job applications by sending AI-generated personalized emails directly to company founders. The application will:
- Store company details, including the founder’s email and job position.
- Generate customized email content using OpenAI’s GPT API based on the company website.
- Automate sending emails through the Gmail API on scheduled dates.
- Help job seekers bypass traditional HR processes and connect directly with decision-makers.

## Phase 1: Initial Setup
### 1. Database Setup
- Create a **PostgreSQL database** using Neon Console.
- Define a table with the following fields:
  - `id` (Primary Key, Auto-increment)
  - `company_name` (Text)
  - `company_website` (Text)
  - `job_position` (Text)
  - `founder_email` (Text)
  - `email_date` (Date)

## Phase 2: AI-Powered Email Generation
### 2. OpenAI GPT Integration
- Write a Python script to:
  - Fetch `company_website` from the database.
  - Use OpenAI’s GPT API to generate a personalized email.
  - Store the generated email in a variable for later sending.

## Phase 3: Email Automation
### 3. Gmail API Integration
- Set up **Gmail API credentials**.
- Write a Python script to:
  - Fetch email details from the database.
  - Send the AI-generated email to `founder_email` on the `email_date`.
  - Mark emails as sent in the database.

## Phase 4: Testing & Refinements
### 4. Testing
- Test sending a few emails manually.
- Handle edge cases like missing data or API failures.

### 5. Optimization
- Implement error handling & logging.
- Consider adding a retry mechanism for failed emails.

## Future Enhancements (Post-POC)
- **Follow-up emails** for non-responders.
- **Email tracking** to check if emails are opened.
- **Basic UI** for managing company entries.
- **Scaling strategy** to handle higher email volumes.

