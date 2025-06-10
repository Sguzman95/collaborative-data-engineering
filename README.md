# Collaborative Data Engineering Demo

This repository demonstrates Git collaboration between data engineers and analysts.

## Webinar: "Data Camp: Collaborative Data Engineering with Git"

**Presenter:** Amanda Crawford-Adamo (ex-Dropbox, ex-Microsoft)

**Contact:** [LinkedIn](https://www.linkedin.com/in/techacrawford/)

If you want to learn more about advanced git concepts for data engineering, take my
**[Advanced Git](https://app.datacamp.com/learn/courses/advanced-git)** course on DataCamp!

## Prerequisites for Airflow Setup

Before the webinar, please ensure you have the following installed and configured on your laptop:

- **Python 3.8 or higher**
- **Docker Desktop** (for running Airflow locally)
- **Astro CLI** (install via Homebrew: `brew install astro` or winget: `winget install Astronomer.Astro`)
- **Git 2.25 or higher**
- **(Optional) GitHub CLI** for repository management

### Verify Your Setup
Run these commands to confirm everything is installed correctly:
```

python --version    # Should show 3.8+
docker --version    # Should show Docker version
astro version       # Should show Astro CLI version
git --version       # Should show 2.25+

```

### Quick Start for Attendees
1. Clone this repository: `git clone https://github.com/amandajcrawford/collaborative-data-engineering.git`
2. Navigate to project: `cd collaborative-data-engineering`
3. Start Airflow: `astro dev start`
4. Access Airflow UI: http://localhost:8080 (admin/admin)

## Git Commit Message Structure for Data Engineers

To maintain clear communication between data engineers, analysts, and stakeholders, you can use this commit message format:

```
<type>(<scope>): <short description>

<body>

- Data impact: <describe effect on downstream systems>
- Breaking changes: <yes/no and details>
- References: <JIRA ticket, GitHub issue, or relevant links>

```

### Commit Types
- **feat(pipeline)**: New features or pipeline additions
- **fix(ingestion)**: Bug fixes in data ingestion
- **perf(transform)**: Performance improvements in transformations
- **schema**: Database schema changes
- **docs**: Documentation updates
- **test**: Adding or updating tests

### Example Commit Messages
```
# Adding new pipeline feature

feat(pipeline): add discount calculation logic

- Data impact: Adds 'discount_pct' column to sales_facts table
- Breaking changes: No
- References: JIRA-123


# Fixing data quality issue

fix(ingestion): resolve null handling in customer data

- Data impact: Prevents null customer_id records in warehouse.
- Breaking changes: No
- References: GitHub issue #45

```

### Project Structure
```
collaborative-data-engineering/
├── dags/              # Data engineering pipelines
├── analysis/          # Data analyst workspace
├── data/samples/      # Sample data for testing
├── config/            # Configuration files
└── scripts/           # Utility scripts

```

### Learning Objectives
- ✅ Advanced Git branching for data teams
- ✅ Semantic commit messages as documentation
- ✅ Conflict resolution in collaborative environments
- ✅ Git history as living project documentation

### Key Commands We'll Use
```
# Engineer workflow

git checkout -b feature/discount-calculation
git commit -m "feat(pipeline): add discount calculation logic"

# Analyst workflow

git checkout -b analysis/q3-report
git commit -m "feat(analysis): add Q3 discount impact analysis"

# Collaboration

git merge --no-ff feature/discount-calculation
git tag -a v1.1.0 -m "Release: Discount Analysis Features"

```

### Next Steps
- Practice with your own team
- Implement these patterns in your team or development
- Explore [Advanced Git](https://app.datacamp.com/learn/courses/advanced-git) features for data workflows

## Troubleshooting

### Common Setup Issues
- **Docker not starting**: Ensure Docker Desktop is running before executing `astro dev start`
- **Port conflicts**: If port 8080 is in use, stop other services or modify Airflow configuration
- **Permission errors**: On macOS/Linux, you may need to run Docker commands with appropriate permissions

### Getting Help
- Check Astro CLI documentation: https://docs.astronomer.io/astro/cli/overview
- Airflow documentation: https://airflow.apache.org/docs/

Happy collaborating! 🤝

## Take My Course Here on [Advanced Git](https://app.datacamp.com/learn/courses/advanced-git)