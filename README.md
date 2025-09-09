# github-md-fetcher

### Generate the GITHUB_TOKEN and export it below the line, run it in the terminal

export GITHUB_TOKEN=ghp_uEP8hN0GRRsFowdJuine5cLaNJs0TXsz1sZAUGsample

## And after running the below command

python gh_md_fetch.py \                                     
  --repo https://github.com/owner/repo \
  --branch main \
  --repo-dir docs \
  --out-dir ./local_docs

### Example: I will run my repo, then check the .md files

python gh_md_fetch.py \
  --repo https://github.com/Nirodhachathuri/github-md-fetcher \
  --branch main \
  --repo-dir docs \
  --out-dir ./local_docs

### Then, after the below success message is displayed 

Saved docs/guide/usage.md -> ./local_docs/docs/guide/usage.md
