pwd && cd /e/notes
echo "Uploading notes data"
git add . && git commit -m "Update" && git push
echo "Finish! Cheers!"