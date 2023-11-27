# GDPR Compliance Plan for Real-Time Movie Review Analysis Project 

Version 1.0 | 24/11/2023

## Project Overview
- **Project Name:** Real-Time Movie Review Analysis
- **Description:** Development of a system to analyze real-time movie reviews using Kafka for data streaming and Memgraph for the graph database. The goal is to generate film recommendations based on user reviews.
- **Data Controller:** MovieHub Technologies, Inc.
- **Sub-processors:** Kafka, Memgraph
- **Managers:** Amine Scientist, Hicham Engineer, Yassine ESSAIDI, Hicham Dev
- **Data Protection Officers:** Amine Scientist, Hicham Engineer
- **Contact:** contact.dpo@moviehub.dev

## Data Inventory and Objective Specification
### Data Types Collected
- **User Information (UI):** User ID, Age, Gender
- **Movie Review Data (MRD):** User ID, Movie ID, Rating, Timestamp
- **Movie Information (MI):** Movie ID, Title, Genres, Release Date, IMDb URL


### Data Collection Points
- User registration
- Interaction with the application
- Data streaming through Kafka

### Data Collection and Processing Objective
- Provide real-time movie recommendations based on user reviews.

### Legal Basis for Processing
- Explicit user consent and contract execution.

## Data Flow Mapping
### Data Sources
- User inputs
- Kafka streaming for real-time movie reviews
- Memgraph for storing and querying movie data

### Data Processing Activities
- Collection, transformation, and analysis of real-time movie review data
- Graph-based storage and retrieval of movie information

### Data Storage Locations
- Secure Memgraph Cloud (EU-based)
- Encrypted local storage for application data

### Data Recipients
- Memgraph for storage and retrieval
- Development and support team

### Transborder Data Transfers
- No user data transferred outside the EU.

## Transparency and Privacy Notice
### Privacy Policy Details
- Clearly explains data usage, third-party sharing, and user rights.
- DPO contact information provided for privacy concerns.

### Distribution Method of Privacy Notice
- Notification during user registration
- Accessible in the application settings

## Consent Management
### Consent Mechanism
- Active opt-in during registration
- Easily accessible option to modify consent in user profiles

### Consent Documentation
- Timestamped record of consent
- Version of the privacy policy accepted

## Data Subject Rights
- Access: Users can view their movie review data in the application.
- Rectification: Editable via user profile settings; support team notified for assistance if needed.
- Erasure: 'Delete My Account' feature for complete data erasure.
- Data Portability: Export feature in machine-readable format available in settings.
- Objection to Processing: DPO contact information provided for objections.

## Data Security Measures
### Technical Measures
- End-to-end encryption for data in transit and at rest.

### Organizational Measures
- Regular data protection and security training for all staff.
- Role-based data access controls.

## Data Minimization and Retention Policy
### Minimization Strategies
- Collect only necessary data for movie recommendations.

### Retention Schedule
- Data kept as long as the user account is active, plus one year for backup.

### Data Elimination Procedures
- Secure data erasure from all systems and backups after the retention period.

## Data Processing Agreements (DPA)
### DPA Details with Sub-processors
- Clear roles, responsibilities, and GDPR compliance requirements.
- Kafka and Memgraph adhere to GDPR standards.

### Rights of Audit
- MovieHub retains the right to audit Kafka and Memgraph's data practices.

## Data Protection Impact Assessment (DPIA)
- DPIA required due to the real-time processing of user movie reviews.
- Risk analysis and mitigation strategies implemented, including anonymization.

## Incident Response and Data Breach Protocol
### Incident Detection Methods
- Monitoring tools for detecting data breaches.

### Breach Reporting Procedures
- Internal process for immediate reporting to DPO and authorities.

### Notification Format and Timeline
- Immediate notification to affected users in case of a data breach.

## Compliance Monitoring and Audit
### Compliance Monitoring Schedule
- Regular internal compliance checks.

### Internal Audit Schedule
- Annual external audit for GDPR compliance.

### Non-compliance Findings Action Plan
- Remediation plan in place with escalation procedures to the management.

## Documentation and Record Keeping
### Data Processing Activity Logs
- Detailed logs maintained in compliance software.

### Data Protection Documentation
- Securely stored with user account data.

### Training Records
- Logs of all staff training sessions and attendance.

## Data Protection Officer (DPO)
### DPO Appointment
- Amine Scientist and Hicham Engineer appointed with independence in the role.

### DPO Responsibilities
- Oversee compliance, act as a point of contact for data subjects and authorities.

### DPO Reporting Structure
- Direct line with CTOs and the board.

## Training and Awareness
### Training Program Plan
- GDPR basics, application-specific data handling, and security protocols.

### Training Frequency
- Annual training for all staff, additional training during role changes.

### Awareness Campaigns
- Monthly newsletter on data protection best practices.

## Review and Update Mechanism
### Review Frequency
- Bi-annual review of the GDPR compliance plan.

### Update Procedures
- Changes approved by DPO and legal team.

### Change Management Process
- Documented procedure for implementing changes throughout the organization.

## Validation
- **Prepared by:** Amine Scientist, Hicham Engineer
- **Reviewed by:** Yassine ESSAIDI, Hicham Dev



# Github commands

<!-- github command -->
#### create branch:
```bash
git branch -c name_of_the_branch
```
#### create & switch to this branch:
```bash
git checkout -b name_of_the_branch
```
#### delete a branch:
```bash
git branch -d name_of_the_branch
```

<!-- close github command -->