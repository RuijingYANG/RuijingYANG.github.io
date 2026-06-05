# Syncing the website CV from Overleaf

This site publishes the CV PDF from `files/Ruijing_Yang_CV.pdf`. The sidebar CV link points at that site-hosted PDF, so replacing the PDF in this repository updates the CV that visitors download.

## Recommended workflow

1. Create or choose a separate GitHub repository for the Overleaf CV project, for example `RuijingYANG/cv`.
2. In Overleaf, enable GitHub synchronization for the CV project and push the Overleaf project to that GitHub repository.
3. In this website repository, run the **Sync CV from Overleaf GitHub repo** GitHub Actions workflow.
4. The workflow checks out the Overleaf-synced CV repository, builds the LaTeX file with XeLaTeX, copies the resulting PDF to `files/Ruijing_Yang_CV.pdf`, and commits the changed PDF back to the website repository.
5. GitHub Pages then republishes the website with the refreshed CV PDF.

## Manual run

Use **Actions → Sync CV from Overleaf GitHub repo → Run workflow** and fill in:

| Input | Default | Meaning |
| --- | --- | --- |
| `cv_repository` | `RuijingYANG/cv` | GitHub repository connected to the Overleaf CV project. |
| `cv_ref` | `main` | Branch, tag, or commit SHA to sync. |
| `cv_tex_path` | `main.tex` | Main `.tex` file in the CV repository. |
| `cv_pdf_path` | blank | Optional path to an already-built PDF in the CV repository. If set, the workflow copies this PDF instead of compiling LaTeX. |
| `output_pdf_path` | `files/Ruijing_Yang_CV.pdf` | Destination PDF in this website repository. |

If the CV repository is private, add a repository secret named `CV_REPO_TOKEN` in this website repository. The token must have read access to the CV repository and write access to this website repository.

## Optional automatic trigger from the CV repository

Overleaf's GitHub synchronization is manual: after editing the CV in Overleaf, push the Overleaf changes to the CV GitHub repository. If you also want the website sync workflow to start automatically after that push, add this workflow to the CV repository:

```yaml
name: Notify website to sync CV

on:
  push:
    branches:
      - main

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger website CV sync
        env:
          WEBSITE_REPO: RuijingYANG/RuijingYANG.github.io
          WEBSITE_SYNC_TOKEN: ${{ secrets.WEBSITE_SYNC_TOKEN }}
        run: |
          curl -fsSL \
            -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${WEBSITE_SYNC_TOKEN}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            "https://api.github.com/repos/${WEBSITE_REPO}/dispatches" \
            -d '{
              "event_type": "sync-cv",
              "client_payload": {
                "cv_repository": "RuijingYANG/cv",
                "cv_ref": "main",
                "cv_tex_path": "main.tex",
                "output_pdf_path": "files/Ruijing_Yang_CV.pdf"
              }
            }'
```

Create `WEBSITE_SYNC_TOKEN` in the CV repository secrets. The token must be allowed to trigger repository dispatch events on `RuijingYANG/RuijingYANG.github.io`.
