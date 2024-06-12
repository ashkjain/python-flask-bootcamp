param(
    [string]$msg
)

# Check if msg is provided
if (-not $msg) {
    Write-Host "Usage: ./git_script.ps1 -msg <commit message>"
    exit 1
}

# Add all files
git add .

# Commit with the provided message
git commit -m "$msg"

# Push changes to remote repository
git push
