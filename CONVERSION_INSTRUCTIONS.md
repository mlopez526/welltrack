# How to Convert SPRINT_1_SUBMISSION.md to PDF or DOCX

## 📄 Main Submission File
**File:** `SPRINT_1_SUBMISSION.md`

This is your complete submission document containing all required sections.

---

## Option 1: Convert to PDF (Recommended)

### Method A: Using Visual Studio Code
1. Install "Markdown PDF" extension in VS Code
2. Open `SPRINT_1_SUBMISSION.md`
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
4. Type "Markdown PDF: Export (pdf)"
5. Select PDF option
6. File will be saved as `SPRINT_1_SUBMISSION.pdf`

### Method B: Using Pandoc (Command Line)
```bash
# Install pandoc first: https://pandoc.org/installing.html

# Convert to PDF
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.pdf

# With better formatting
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

### Method C: Using Online Converter
1. Go to https://www.markdowntopdf.com/
2. Upload `SPRINT_1_SUBMISSION.md`
3. Click "Convert"
4. Download the PDF

### Method D: Using GitHub
1. Push the file to GitHub
2. View the file on GitHub (it renders markdown)
3. Use browser's "Print to PDF" function

---

## Option 2: Convert to DOCX (Microsoft Word)

### Method A: Using Pandoc (Command Line)
```bash
# Install pandoc first: https://pandoc.org/installing.html

# Convert to DOCX
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.docx

# With reference document for styling
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.docx --reference-doc=template.docx
```

### Method B: Using Online Converter
1. Go to https://www.convertio.co/md-docx/
2. Upload `SPRINT_1_SUBMISSION.md`
3. Click "Convert"
4. Download the DOCX file

### Method C: Manual Copy-Paste
1. Open `SPRINT_1_SUBMISSION.md` in VS Code or any text editor
2. Copy all content
3. Open Microsoft Word
4. Paste content
5. Word will preserve most formatting
6. Adjust formatting as needed
7. Save as DOCX

---

## Option 3: Keep as Markdown (.md)

**Good news:** Most modern systems can read Markdown files!

- GitHub/GitLab render markdown beautifully
- VS Code has built-in markdown preview
- Many assignment submission systems accept .md files
- Markdown is plain text, so it's universally readable

**To preview in VS Code:**
1. Open `SPRINT_1_SUBMISSION.md`
2. Press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac)
3. See formatted preview

---

## Recommended Submission Format

### If instructor accepts .md files:
✅ **Submit:** `SPRINT_1_SUBMISSION.md` (as is)
- Easiest option
- No conversion needed
- Preserves all formatting

### If instructor requires PDF:
✅ **Submit:** `SPRINT_1_SUBMISSION.pdf` (converted)
- Professional appearance
- Universal compatibility
- Cannot be accidentally edited

### If instructor requires DOCX:
✅ **Submit:** `SPRINT_1_SUBMISSION.docx` (converted)
- Editable if needed
- Compatible with Microsoft Office
- Can add comments/feedback

---

## What to Submit

### Minimum Required:
1. **SPRINT_1_SUBMISSION.md** (or PDF/DOCX version)
   - Contains all 4 required sections
   - End-user documentation
   - Technical documentation
   - Updated user stories
   - Agile artifacts

### Recommended to Include:
2. **Code files:**
   - `backend/app.py`
   - `frontend/index.html`
   - `backend/requirements.txt`

3. **Supporting docs:**
   - `README.md` (quick start)
   - `START_HERE.md` (entry point)

### Optional (if allowed):
4. **Complete project folder** (welltrack.zip)
   - All code
   - All documentation
   - Ready to run

---

## Quick Conversion Commands

### Install Pandoc (if needed)

**Windows:**
```bash
# Using Chocolatey
choco install pandoc

# Or download from: https://pandoc.org/installing.html
```

**Linux/WSL:**
```bash
sudo apt-get install pandoc
```

**Mac:**
```bash
brew install pandoc
```

### Convert Commands

```bash
# Navigate to project folder
cd /mnt/c/Users/Dennis\ Akinbogun/Downloads/welltrack

# Convert to PDF
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.pdf

# Convert to DOCX
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.docx

# Convert with better formatting
pandoc SPRINT_1_SUBMISSION.md -o SPRINT_1_SUBMISSION.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt
```

---

## Verification Checklist

Before submitting, verify your document contains:

- [ ] Section 1: End-User Documentation
- [ ] Section 2: Technical Documentation
- [ ] Section 3: Updated User Stories (US-01 and US-02)
- [ ] Section 4: Agile Artifacts
  - [ ] Sprint Backlog
  - [ ] Product Backlog
  - [ ] Working Agreement
- [ ] All sections are complete and readable
- [ ] Code examples are properly formatted
- [ ] Tables are properly formatted
- [ ] File is properly named

---

## File Naming

**Recommended names:**
- `SPRINT_1_SUBMISSION.md` (markdown)
- `SPRINT_1_SUBMISSION.pdf` (PDF)
- `SPRINT_1_SUBMISSION.docx` (Word)

Or follow your instructor's naming convention:
- `[YourName]_Sprint1_Submission.pdf`
- `WellTrack_Sprint1_Documentation.pdf`
- etc.

---

## Need Help?

If conversion doesn't work:
1. Check if pandoc is installed: `pandoc --version`
2. Try online converters (no installation needed)
3. Use VS Code with Markdown PDF extension
4. Submit as .md file (if allowed)

---

**Your submission document is ready!**

Choose your preferred format and convert using the methods above.

**Main file:** `SPRINT_1_SUBMISSION.md`  
**Status:** ✅ Complete and ready to submit
