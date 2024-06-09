param(
    [string]$CommitMessage
)

# Check if CommitMessage is provided
if (-not $CommitMessage) {
    Write-Host "Usage: ./git_script.ps1 -CommitMessage <commit message>"
    exit 1
}

# Add all files
git add .

# Commit with the provided message
git commit -m "$CommitMessage"

# Push changes to remote repository
git push
