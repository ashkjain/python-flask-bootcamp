param(
    [string]$Cmsg
)

# Check if Cmsg is provided
if (-not $Cmsg) {
    Write-Host "Usage: ./git_script.ps1 -Cmsg <commit message>"
    exit 1
}

# Add all files
git add .

# Commit with the provided message
git commit -m "$Cmsg"

# Push changes to remote repository
git push
