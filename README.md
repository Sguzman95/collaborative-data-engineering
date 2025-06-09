# Collaborative Data Engineering Demo

This repository demonstrates Git collaboration between data engineers and analysts.

## Webinar: "Data Camp: Collaborative Data Engineering with Git"
**Presenter:** Amanda Crawford-Adamo (ex-Dropbox, ex-Microsoft)

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

### Getting Started
1. Clone this repository
2. Create feature branches for changes
3. Use semantic commit messages
4. Collaborate through pull requests
5. Merge with `--no-ff` to preserve context

### Key Commands We'll Use
```bash
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
- Try the real Airflow setup (see setup guide)
- Practice with your own team
- Implement these patterns in production
