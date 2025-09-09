#!/usr/bin/env python3
import argparse
import base64
import os
import requests
from urllib.parse import urlparse

def parse_args():
    parser = argparse.ArgumentParser(description="Download Markdown files from a private GitHub repository.")
    parser.add_argument("--repo", required=True, help="Full GitHub repository URL (e.g. https://github.com/owner/repo)")
    parser.add_argument("--branch", required=True, help="Branch name to fetch from")
    parser.add_argument("--repo-dir", required=True, help="Directory path inside the repo to look for .md files")
    parser.add_argument("--out-dir", required=True, help="Local directory to save files")
    parser.add_argument("--token", help="GitHub personal access token (or use GITHUB_TOKEN env var)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be downloaded without saving")
    return parser.parse_args()

def authenticate(token):
    headers = {"Authorization": f"token {token}"}
    r = requests.get("https://api.github.com/user", headers=headers)
    if r.status_code != 200:
        raise SystemExit(f"Authentication failed: {r.json().get('message', r.text)}")
    return headers

def extract_owner_repo(repo_url):
    try:
        parsed = urlparse(repo_url)
        path_parts = parsed.path.strip("/").split("/")
        if len(path_parts) < 2:
            raise ValueError
        return path_parts[0], path_parts[1]
    except Exception:
        raise SystemExit("Invalid GitHub repository URL format. Use https://github.com/owner/repo")

def fetch_tree(owner, repo, branch, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise SystemExit(f"Error fetching repo tree: {r.json().get('message', r.text)}")
    return r.json()["tree"]

def download_file(owner, repo, path, headers, out_dir, branch, dry_run=False):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Failed to download {path}: {r.json().get('message', r.text)}")
        return
    data = r.json()
    if data.get("encoding") == "base64":
        content = base64.b64decode(data["content"])
    else:
        content = data.get("content", "").encode()

    local_path = os.path.join(out_dir, path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    if dry_run:
        print(f"[DRY RUN] Would save {path} -> {local_path}")
    else:
        with open(local_path, "wb") as f:
            f.write(content)
        print(f"Saved {path} -> {local_path}")

def main():
    args = parse_args()
    token = args.token or os.getenv("GITHUB_TOKEN")
    if not token:
        raise SystemExit("Error: GitHub token must be provided via --token or GITHUB_TOKEN env var")

    headers = authenticate(token)
    owner, repo = extract_owner_repo(args.repo)

    tree = fetch_tree(owner, repo, args.branch, headers)
    md_files = [item["path"] for item in tree if item["type"] == "blob"
                and item["path"].startswith(args.repo_dir.strip("/"))
                and (item["path"].endswith(".md") or item["path"].endswith(".markdown"))]

    if not md_files:
        print("No Markdown files found.")
        return

    for path in md_files:
        download_file(owner, repo, path, headers, args.out_dir, args.branch, args.dry_run)

if __name__ == "__main__":
    main()
