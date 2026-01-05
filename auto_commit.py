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

def auto_commit():
    """Make an automatic commit to keep GitHub streak alive"""
    
    # Get current directory (should be your repo)
    repo_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(repo_path)
    
    print(f"Working in: {repo_path}")
    
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
    print("\n1. Checking git status...")
    run_command("git status")
    
    # Add changes
    print("\n2. Adding changes...")
    if not run_command(f"git add {activity_file}"):
        print("❌ Failed to add changes")
        return False
    
    # Commit
    commit_message = f"Daily update: {date_only}"
    print(f"\n3. Creating commit: '{commit_message}'...")
    if not run_command(f'git commit -m "{commit_message}"'):
        print("❌ Failed to commit (maybe no changes?)")
        return False
    
    # Push to GitHub
    print("\n4. Pushing to GitHub...")
    if not run_command("git push origin main"):
        # Try 'master' if 'main' fails
        print("Trying 'master' branch...")
        if not run_command("git push origin master"):
            print("❌ Failed to push changes")
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