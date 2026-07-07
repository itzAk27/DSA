"""
DSA Practice Tracker - Add Python solutions with automatic tracking and git integration.
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration constants
SRC_FOLDER = "src"
README_FILE = "README.md"
ENCODING = "utf-8"
README_HEADER = "#  DSA Solutions\n\n| # | Problem | Link | Topic | Code |\n|--|---------|------|--------|------|\n"


def get_user_input(prompt: str, default: str = None) -> str:
    """
    Get validated user input.
    
    Args:
        prompt: Input prompt message
        default: Default value if input is empty
        
    Returns:
        User input or default value
    """
    user_input = input(prompt).strip()
    if not user_input and default:
        return default
    if not user_input:
        raise ValueError(f"{prompt} cannot be empty!")
    return user_input


def get_code_input() -> str:
    """
    Get multi-line code input from user.
    
    Returns:
        Code input as string
    """
    print("Paste your Python solution below (end input with 'END' on a new line):")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)
    
    code = "\n".join(code_lines).strip()
    if not code:
        raise ValueError("Code cannot be empty!")
    return code


def create_solution_file(problem_title: str, topic: str, url: str, code: str) -> str:
    """
    Create and save the solution file.
    
    Args:
        problem_title: Title of the problem
        topic: Topic/category of the problem
        url: URL/link to the problem
        code: Solution code
        
    Returns:
        Path to created file
    """
    file_name = problem_title.replace(" ", "") + ".py"
    folder_path = os.path.join(SRC_FOLDER, topic.lower())
    
    # Create directory if it doesn't exist
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    
    # Write solution file with metadata
    with open(file_path, "w", encoding=ENCODING) as f:
        f.write(f"# Problem: {problem_title}\n")
        f.write(f"# URL: {url}\n")
        f.write(f"# Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(code)
    
    return file_path


def has_header(lines: list) -> bool:
    """
    Check if README has the proper header row.
    
    Args:
        lines: List of lines from README
        
    Returns:
        True if header row exists, False otherwise
    """
    if len(lines) < 3:
        return False
    # Check if the header row contains column names
    header_line = lines[2].strip()
    return "Problem" in header_line and "Link" in header_line and "Topic" in header_line


def initialize_readme() -> None:
    """
    Initialize README.md with headers if it doesn't exist or is missing headers.
    """
    if not os.path.exists(README_FILE):
        with open(README_FILE, "w", encoding=ENCODING) as f:
            f.write(README_HEADER)
    else:
        # Check if existing README has the header
        with open(README_FILE, "r", encoding=ENCODING) as f:
            lines = f.readlines()
        
        # If file doesn't have proper headers, add them
        if not has_header(lines):
            # Reconstruct file with header
            with open(README_FILE, "w", encoding=ENCODING) as f:
                # Write the header
                f.write(README_HEADER)
                # Write back existing content if any (skip empty lines)
                for line in lines:
                    if line.strip() and not line.startswith("#  DSA Solutions"):
                        f.write(line)


def get_problem_count() -> int:
    """
    Get the current count of problems in README.
    
    Returns:
        Number of problems tracked
    """
    with open(README_FILE, "r", encoding=ENCODING) as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) >= 5 and parts[1].strip().isdigit():
                try:
                    count = max(count, int(parts[1].strip()))
                except ValueError:
                    continue
    return count


def update_readme(problem_title: str, url: str, topic: str, file_path: str) -> None:
    """
    Update README.md with the new problem entry.
    
    Args:
        problem_title: Title of the problem
        url: URL/link to the problem
        topic: Topic/category of the problem
        file_path: Path to solution file
    """
    initialize_readme()
    
    count = get_problem_count()
    file_name = os.path.basename(file_path)
    
    # Normalize path for markdown link
    file_path_md = file_path.replace("\\", "/")
    
    # Append new entry to README
    with open(README_FILE, "a", encoding=ENCODING) as f:
        f.write(f"| {count + 1} | {problem_title} | [Link]({url}) | {topic.capitalize()} | [{file_name}]({file_path_md}) |\n")


def execute_git_commands(problem_title: str) -> None:
    """
    Execute git add, commit, and push commands.
    
    Args:
        problem_title: Title of the problem for commit message
    """
    try:
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"Added {problem_title}"],
            check=True,
            capture_output=True
        )
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("✓ Successfully pushed to git")
    except subprocess.CalledProcessError as e:
        print(f"⚠ Git operation failed: {e.stderr.decode() if e.stderr else str(e)}")
    except FileNotFoundError:
        print("⚠ Git not found. Skipping git operations.")


def main() -> None:
    """Main function to run the DSA problem tracker."""
    try:
        print("\n" + "="*50)
        print("  DSA SOLUTION TRACKER")
        print("="*50 + "\n")
        
        # Get user inputs
        problem_title = get_user_input("Enter problem title (e.g., Two Sum): ")
        topic = get_user_input("Enter topic (e.g., arrays, strings, dp): ")
        url = get_user_input("Enter URL: ")
        code = get_code_input()
        
        # Create solution file
        file_path = create_solution_file(problem_title, topic, url, code)
        print(f"\n✓ Solution saved to: {file_path}")
        
        # Update README
        update_readme(problem_title, url, topic, file_path)
        print("✓ README.md updated")
        
        # Git operations
        execute_git_commands(problem_title)
        
        print("\n" + "="*50)
        print("✓ Problem added successfully!")
        print("="*50 + "\n")
        
    except ValueError as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

