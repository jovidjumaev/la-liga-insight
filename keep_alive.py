#!/usr/bin/env python3
"""
Keep Alive Script for La Liga Insight Dashboard

This script creates an empty commit to keep the Streamlit app active.
It can be run manually or scheduled locally if needed.
"""

import subprocess
import datetime
import sys
import os

def run_command(command, description):
    """Run a git command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main function to create and push an empty commit."""
    print("🤖 La Liga Insight - Keep Alive Script")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a git repository. Please run this script from the project root.")
        sys.exit(1)
    
    # Get current timestamp
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    commit_message = f"🤖 Keep app alive - {timestamp}"
    
    print(f"📅 Creating empty commit at {timestamp}")
    print("-" * 50)
    
    # Configure git (if not already configured)
    run_command('git config --local user.email "action@github.com"', "Configure git email")
    run_command('git config --local user.name "Keep Alive Script"', "Configure git username")
    
    # Create empty commit
    if run_command(f'git commit --allow-empty -m "{commit_message}"', "Create empty commit"):
        print(f"📝 Commit message: {commit_message}")
        
        # Push to remote
        if run_command('git push origin main', "Push to remote repository"):
            print("\n🎉 Successfully pushed empty commit!")
            print("Your Streamlit app should remain active.")
        else:
            print("\n⚠️  Failed to push commit. Please check your git remote configuration.")
    else:
        print("\n⚠️  Failed to create commit. Please check your git status.")

if __name__ == "__main__":
    main() 