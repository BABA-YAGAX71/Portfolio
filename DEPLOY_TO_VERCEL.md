# Deploying to Vercel

Follow these steps to deploy your portfolio to Vercel:

## Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

## Step 2: Connect to Vercel

1. Go to [Vercel](https://vercel.com)
2. Sign up/Login with your GitHub account
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will auto-detect it's a Python project

## Step 3: Configure Build Settings

The `vercel.json` file is already configured. Make sure:
- **Framework Preset**: Python
- **Build Command**: (leave empty - Vercel handles it)
- **Output Directory**: (leave empty)

## Step 4: Deploy

Click "Deploy" and wait for the build to complete!

Your portfolio will be live at: `https://your-username.vercel.app`

## File Structure for Vercel

```
Portfolio/
├── api/
│   └── index.py           (Main Flask app for Vercel)
├── templates/             (HTML templates)
├── static/                (Images, CSS, JS)
├── app.py                 (Local development)
├── requirements.txt       (Python dependencies)
├── vercel.json           (Vercel configuration)
├── .vercelignore         (Files to ignore in deployment)
└── ...
```

## Important Notes

- The `api/index.py` is used for Vercel deployment
- The `app.py` is for local development
- All dependencies are listed in `requirements.txt`
- Your profile image is included in the static folder

## Troubleshooting

If deployment fails:
1. Check that `requirements.txt` has Flask
2. Ensure `api/index.py` exists
3. Verify `vercel.json` is properly formatted
4. Check Vercel logs for detailed error messages

## Custom Domain (Optional)

After successful deployment:
1. Go to Vercel Project Settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

---

Happy deploying! Your portfolio will be live shortly! 🚀
