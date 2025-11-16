#!/bin/bash
# Quick Deploy Commands

echo "=== AI Doctor Assistant - Deployment Quick Start ==="

# Step 1: Commit changes
echo "Step 1: Committing changes..."
git commit -m "Deploy: Clean repo and prepare for production

- Remove all generated audio files, cache, and .env
- Add .gitignore to prevent future commits of temporary files
- Fix API integration issues and add error handling
- Add comprehensive deployment documentation for Hugging Face Spaces
- Optimize Docker configuration
- Update dependencies and documentation"

# Step 2: Push to GitHub
echo -e "\nStep 2: Pushing to GitHub..."
git push origin deploy

echo -e "\n=== Next Steps ==="
echo "1. Go to: https://huggingface.co/new-space"
echo "2. Choose SDK: Docker"
echo "3. Connect to your GitHub repository"
echo "4. Add Secret: GROQ_API_KEY = your_actual_key"
echo "5. Space will auto-deploy!"
echo ""
echo "Your Space URL will be:"
echo "https://huggingface.co/spaces/YOUR_USERNAME/ai-doctor-assistant"
echo ""
echo "=== Documentation ==="
echo "- README.md - Main documentation"
echo "- DEPLOYMENT.md - Detailed deployment guide"
echo "- SETUP_COMPLETE.md - What was completed"
