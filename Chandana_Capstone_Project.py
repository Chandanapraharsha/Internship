from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
path = "Week12_College_Format.pdf"
doc = SimpleDocTemplate(
    path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=18,
    spaceAfter=14
)

heading = ParagraphStyle(
    "Heading",
    parent=styles["Heading2"],
    spaceBefore=12,
    spaceAfter=8
)

text = styles["Normal"]
elements = []
elements.append(Paragraph("WEEK 12 REPORT", title_style))
elements.append(Paragraph("Final Capstone & Career Preparation", styles["Heading3"]))
elements.append(Paragraph("Due Date: March 3, 2026", text))
elements.append(Spacer(1, 12))
def section(title, content):
    elements.append(Paragraph(title, heading))
    for line in content:
        elements.append(Paragraph("• " + line, text))
    elements.append(Spacer(1, 6))
section("Theory Concepts", [
"End-to-end machine learning workflow",
"Model deployment basics",
"Data science portfolio creation",
"Interview preparation",
"Continuous learning roadmap",
"Industry trends and opportunities"
])

section("Hands-On Practice", [
"Complete ML project",
"Documentation and presentation",
"Professional GitHub portfolio",
"Interview question practice",
"Resume creation",
"Professional networking"
])

section("Project Description", [
"Comprehensive Data Science Project",
"Solve real business problem using full data science lifecycle",
"Provide business recommendations"
])

section("Technical Requirements", [
"Complete workflow implementation",
"Professional documentation",
"Organized GitHub repository",
"Business presentation",
"Deployment demo"
])
elements.append(Paragraph("Project Phases", heading))

phase_data = [
["Phase", "Duration", "Description"],
["1", "Days 1–2", "Project setup, problem selection, metrics"],
["2", "Days 3–4", "Data collection and validation"],
["3", "Days 5–6", "EDA and visualization"],
["4", "Days 7–9", "Model development and tuning"],
["5", "Days 10–11", "Deployment preparation"],
["6", "Days 12–13", "Documentation and presentation"],
["7", "Day 14", "Career preparation"]
]

table = Table(phase_data, colWidths=[60,100,280])
table.setStyle(TableStyle([
("GRID",(0,0),(-1,-1),1,colors.black),
("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")
]))

elements.append(table)
elements.append(Spacer(1,12))


section("Deliverables", [
"Technical documentation",
"Business report",
"Presentation slides",
"Deployed application",
"GitHub repository"
])

section("GitHub Structure", [
"README.md",
"capstone_project.ipynb",
"src/",
"data/",
"reports/",
"deployment/",
"presentation/"
])

section("Quality Checklist", [
"Clear objective",
"Setup instructions",
"Organized code",
"Screenshots",
"Algorithm explanation",
"Testing proof"
])

section("Datasets", [
"sales_data.csv – 100 rows, 5 columns",
"house_prices.csv – 300 rows, 5 columns",
"customer_churn.csv – 500 rows, 4 columns"
])

section("Tips", [
"Focus on storytelling",
"Explain concepts simply",
"Apply for internships",
"Celebrate your learning journey"
])
doc.build(elements)
print("PDF Generated Successfully!")