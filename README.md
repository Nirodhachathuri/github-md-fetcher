## Welcome to the project! 

## This is the main README for the docs folder.

#### Prerequisites

1. Python 3.6 or higher.

2. A GitHub Personal Access Token with repo scope. 

#### Installation

1. Clone this repository or download the files.

2. Install the required Python libraries using pip:

   pip install -r requirements.txt


### To set a GITHUB_TOKEN for the current Terminal session,

export GITHUB_TOKEN=ghp_uEP8hN0GRRsFowdJuine5cLaNJs0TXsz1sZAUGsample

### And after running the below command

python gh_md_fetch.py --repo-url <REPOSITORY_URL> --branch <BRANCH_NAME> --remote-path <REPOSITORY_DIRECTORY> --local-path <LOCAL_DIRECTORY>

--repo-url - The full URL of the private GitHub repository (e.g., https://github.com/user/my-private-repo).

--branch - The name of the branch to download files from (e.g., main or develop).

--remote-path - The path to the directory within the repository to download files from (e.g., docs/manuals).

--local-path - The local directory where the downloaded files will be saved. The script will create this directory if it doesn't exist.

### Example: I will run my repo, then check the .md files

python gh_md_fetch.py \
  --repo https://github.com/Nirodhachathuri/github-md-fetcher \
  --branch main \
  --repo-dir docs \
  --out-dir ./local_docs

### Then, after the below success message is displayed 

Saved docs/guide/usage.md -> ./local_docs/docs/guide/usage.md
