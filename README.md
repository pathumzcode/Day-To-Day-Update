# Day-To-Day-Update 📅

Automated daily activity tracker to maintain consistent GitHub contributions and keep my coding streak alive.

## 📊 Purpose

This repository uses **GitHub Actions** to automatically log daily activity and maintain my GitHub contribution graph. It helps me:

- Keep my GitHub streak alive 🔥
- Track daily coding consistency
- Maintain an active GitHub profile
- Practice automation and CI/CD workflows

## 🛠️ How It Works

The repository contains **two methods** for maintaining the streak:

### 1. **Automated (Recommended)** - GitHub Actions
- Runs automatically **every day at 00:00 UTC** (5:30 AM IST)
- No manual intervention required
- Uses GitHub's built-in automation
- Works even when you're offline

### 2. **Manual** - Python Script
- Run `auto_commit.py` manually when needed
- Use `run_auto_commit.bat` on Windows for quick execution
- Useful for testing or backup

## 🚀 Features

- ✅ **Fully automated** daily commits via GitHub Actions
- ✅ **Manual trigger** option from GitHub Actions tab
- ✅ Timestamp logging in `daily_activity.log`
- ✅ Maintains GitHub streak without manual intervention
- ✅ Smart branch detection (main/master)
- ✅ Conflict prevention with automatic pulls
- ✅ Simple and lightweight

## ⚙️ Setup

### GitHub Actions (Automatic)

The workflow is already configured in `.github/workflows/daily-commit.yml`. It runs automatically:

1. **Scheduled**: Every day at 00:00 UTC
2. **Manual**: Go to **Actions** → **Daily GitHub Streak** → **Run workflow**

No additional setup required! Just push the workflow file to GitHub.

### Manual Execution (Python Script)

If you want to run manually:

```bash
# Clone the repository
git clone https://github.com/pathumzcode/Day-To-Day-Update.git
cd Day-To-Day-Update

# Run the script
python auto_commit.py

# Or on Windows, double-click:
run_auto_commit.bat
```

## 📝 Activity Log

All daily activities are tracked in `daily_activity.log` with timestamps

## 🔧 Technology Stack

- **Language:** Python 3
- **Version Control:** Git
- **Automation:** GitHub Actions
- **CI/CD:** YAML workflow

## 🐛 Troubleshooting

### Workflow not running?
- Check **Actions** tab on GitHub for errors
- Ensure **Actions** are enabled in repository settings
- Verify the workflow file is in `.github/workflows/`

### Manual script not working?
- Make sure you have Python 3 installed
- Verify git is configured: `git config --global user.name "Your Name"`
- Check internet connection
- Ensure you have push access to the repository

## 📌 Note

This is an automated activity tracker. For my actual coding projects and contributions, check out my other repositories.

---

**Profile:** [@pathumzcode](https://github.com/pathumzcode)