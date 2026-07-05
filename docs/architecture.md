# Data Governance Agent Architecture

Data governance agent that manages data catalogs, enforces access policies, classifies sensitive data, tracks data ownership, and ensures compliance with data regulations across the organization.

## Domain Tools

- **catalog_dataset**: Register a dataset in the data catalog with metadata
- **classify_data**: Classify data sensitivity level (public, internal, confidential, restricted)
- **set_access_policy**: Set access policy for a dataset based on classification
- **track_ownership**: Assign or transfer data ownership and stewardship
- **check_compliance**: Check dataset compliance against regulations (GDPR, CCPA, HIPAA)