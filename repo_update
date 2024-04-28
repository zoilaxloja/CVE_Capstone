#!/bin/bash

# This script is  to update local cve repo clone with latest updates

# Here you set the path to your local clone
REPO_PATH="/Users/zoilaloja/Documents/cvelistV5-main"

# Here set the URL of the original repository
ORIGINAL_REPO_URL="https://github.com/CVEProject/cvelistV5.git"

# Here we replace existing local clone with empty directory
if [ -d "$REPO_PATH" ]; then
	rm -rf $REPO_PATH
fi
mkdir $REPO_PATH

# Here we pull the latest changes from the original repository
git clone $ORIGINAL_REPO_URL $REPO_PATH

# Display a message indicating the update status
echo "Repository updated successfully!"
