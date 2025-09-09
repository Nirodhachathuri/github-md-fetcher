## Welcome to the project! 

## This is the main README for the docs folder.

#### Prerequisites

<comment-tag id="1"> Python 3.6 or higher.</comment-tag id="1" text="Reword this bullet point to be more instructional and direct. It's a requirement, so phrasing it as such is more effective. Suggestion: 'You must have Python 3.6 or higher installed.'" type="suggestion">

<comment-tag id="2">* A GitHub Personal Access Token with repo scope. For more information, see GitHub's documentation on creating a PAT.</comment-tag id="2" text="The wording can be made more concise while providing more context. It's helpful to explain why the token is needed in the prerequisites list. Suggestion: 'A GitHub Personal Access Token (PAT) with repo scope is required for authentication. For instructions on how to create one, refer to GitHub's documentation on creating a PAT.'" type="suggestion">


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
