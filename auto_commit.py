#!/usr/bin/env python3
"""
GitHub Auto-Commit Script for Day-To-Day-Update
Username: pathumzcode
"""

import os
import subprocess
from datetime import datetime

def run_command(cmd):
    """Execute shell command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def get_current_branch():
    """Get the current git branch name"""
    try:
        result = subprocess.run("git rev-parse --abbrev-ref HEAD", 
                              shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "main"  # Default to main if can't detect

def auto_commit():
    """Make an automatic commit to keep GitHub streak alive"""
    
    # Get current directory (should be your repo)
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)
    
    print(f"Working in: {repo_path}")
    
    # Get current branch
    current_branch = get_current_branch()
    print(f"Current branch: {current_branch}")
    
    # Pull latest changes first to avoid conflicts
    print("\n1. Pulling latest changes...")
    run_command(f"git pull origin {current_branch}")
    
    # Create/update activity file
    activity_file = "daily_activity.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_only = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n📝 Logging activity for {date_only}...")
    
    with open(activity_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Daily activity logged\n")
    
    # Git operations
    print("\n🔄 Starting git operations...")
    
    # Check git status
    print("\n2. Checking git status...")
    run_command("git status")
    
    # Add changes
    print("\n3. Adding changes...")
    if not run_command(f"git add {activity_file}"):
        print("❌ Failed to add changes")
        return False
    
    # Check if there are actual changes to commit
    result = subprocess.run("git diff --cached --quiet", 
                          shell=True, capture_output=True)
    if result.returncode == 0:
        print("ℹ️ No changes to commit (already up to date)")
        return True
    
    # Commit
    commit_message = f"Daily update: {date_only}"
    print(f"\n4. Creating commit: '{commit_message}'...")
    if not run_command(f'git commit -m "{commit_message}"'):
        print("❌ Failed to commit")
        return False
    
    # Push to GitHub
    print(f"\n5. Pushing to GitHub ({current_branch})...")
    if not run_command(f"git push origin {current_branch}"):
        print("❌ Failed to push changes")
        print("💡 Make sure you have:")
        print("   - Configured git credentials")
        print("   - Have push access to the repository")
        print("   - Internet connection is active")
        return False
    
    print("\n✅ Success! Your GitHub contribution has been logged.")
    print(f"🌟 Check your profile: https://github.com/pathumzcode")
    return True

if __name__ == "__main__":
    print("="*50)
    print("GitHub Auto-Commit Script")
    print("Repository: Day-To-Day-Update")
    print("User: pathumzcode")
    print("="*50)
    
    auto_commit()