#!/usr/bin/env python3
"""Regenerate the downloadable CV from verified facts and current paper/talk lists.

Run: python3 scripts/update_cv.py
Requires: reportlab, PyYAML (local maintenance only; not part of Jekyll).
"""
from pathlib import Path
from xml.sax.saxutils import escape
import yaml
import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak

ROOT = Path(__file__).resolve().parents[1]
# Embed portable fonts shipped with ReportLab to keep spacing consistent.
fonts = Path(reportlab.__file__).resolve().parent / 'fonts'
for name, filename in [('CVSans','Vera.ttf'),('CVSans-Bold','VeraBd.ttf'),('CVSans-Oblique','VeraIt.ttf'),('CVSans-BoldOblique','VeraBI.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(fonts/filename)))
pdfmetrics.registerFontFamily('CVSans',normal='CVSans',bold='CVSans-Bold',italic='CVSans-Oblique',boldItalic='CVSans-BoldOblique')
STYLES = {
 'name': ParagraphStyle('name',fontName='CVSans-Bold',fontSize=17,leading=21,alignment=TA_CENTER,spaceAfter=8),
 'contact': ParagraphStyle('contact',fontName='CVSans',fontSize=9,leading=13,alignment=TA_CENTER,spaceAfter=13),
 'section': ParagraphStyle('section',fontName='CVSans-Bold',fontSize=11,leading=15,spaceBefore=12,spaceAfter=6,textColor=colors.HexColor('#26384d')),
 'body': ParagraphStyle('body',fontName='CVSans',fontSize=9.3,leading=13,spaceAfter=5),
 'small': ParagraphStyle('small',fontName='CVSans',fontSize=8.9,leading=12,spaceAfter=5),
}
items=[]
def para(text,kind='body'):
 return Paragraph(text,STYLES[kind])
def section(name): items.append(para(escape(name),'section'))
def line(text,kind='body'): items.append(para(text,kind))
def paper_records():
 records=[]
 for p in (ROOT/'_research').glob('*.md'):
  records.append(yaml.safe_load(p.read_text().split('---',2)[1]))
 return sorted(records,key=lambda r:r['working_paper_order'])

def talks():
 data=yaml.safe_load((ROOT/'_data/presentations.yml').read_text())
 presentations=[]
 for event in data['presentations']:
  label=event['name']+('*' if event['by_coauthor'] else '')+', '+str(event['year'])
  if event.get('location'): label+=', '+event['location']
  presentations.append(label)
 discussions=[(event['title'],event['conference']+', '+str(event['year']),event['authors']) for event in data['discussions']]
 return presentations,discussions

line('Ruijing (Chandler) Yang','name')
line('Faculty of Business Administration, University of Macau<br/>Taipa, Macau, China | +(853) 8822-8385<br/><link href="mailto:ruijingyang@um.edu.mo">ruijingyang@um.edu.mo</link> | <link href="https://ruijingyang.github.io/">ruijingyang.github.io</link>','contact')
section('Employment')
line('<b>University of Macau</b> | Assistant Professor in Finance | 2025-Present')
line('<b>The Hong Kong Polytechnic University</b> | Postdoctoral Research Fellow | 2024-2025<br/>Supervisor: Jie (Jay) Cao')
section('Education')
line('<b>The Chinese University of Hong Kong</b> | Ph.D. in Finance | 2019-2024')
line('<b>Nanyang Technological University</b> | M.Sc. in Finance (First Class Honors) | 2017-2019')
line('<b>Southeast University</b> | B.Eng. in Civil Engineering | 2013-2017')
section('Research Interests')
line('Empirical asset pricing; derivatives; fixed income; investments; return predictability; machine learning in finance; textual analysis.')
section('Working Papers')
for i,p in enumerate(paper_records(),1):
 block=[para(f"<b>{i}. {escape(p['title'])}</b><br/>({escape(p['authors'])})")]
 if p['title']=='Forecasting Option Returns with News':
  block.append(para('<i>Revise and Resubmit, Journal of Finance</i>','small'))
  block.append(para('Presented at AFA (2025), CICF (2022), and SFS Cavalcade Asia-Pacific (2022).','small'))
 items.append(KeepTogether(block))
section('Teaching Experience')
line('<b>Instructor, Faculty of Business Administration, University of Macau</b>')
for p in sorted((ROOT/'_teaching').glob('*.md')):
 d=yaml.safe_load(p.read_text().split('---',2)[1])
 title=d['title'].replace('INTRODUCTION TO MODERN FINANCIAL TECHNOLOGY','Introduction to Modern Financial Technology').replace('–','-')
 line(f"{escape(title)} ({escape(d['type'])}), {str(d['date'])[:4]}",'small')
section('Honors and Awards')
for text in [
 'Best Paper Award, Hong Kong Conference for Fintech, AI, and Big Data in Business | 2024',
 'Outstanding Paper Award, 4th International Conference on Financial Technology | 2024',
 'Postgraduate Fellowship, The Chinese University of Hong Kong | 2019-2024',
 'Book Prize - First Prize (GPA ranked 1st in M.Sc. in Finance), Nanyang Business School | 2019',
 "Dean's List, Nanyang Business School | 2018",
]:line(escape(text),'small')
items.append(PageBreak())
section('Presentations and Discussions')
line('Selected presentations (* by coauthor)','small')
presentations,discussions=talks()
for text in presentations:line(escape(text),'small')
line('<b>Discussions</b>')
for title,meeting,authors in discussions:line(f"<b>{escape(title)}</b><br/>by {escape(authors)} | {escape(meeting)}",'small')
section('Academic Service')
line('<b>Journal Referee:</b> International Review of Finance; Journal of Behavioral and Experimental Finance; Journal of Empirical Finance; Management Science.')
line('Member of the Management Science Reproducibility Collaboration.')
line('Fisar, M., Greiner, B., Huber, C., Katok, E., Ozkes, A., and the Management Science Reproducibility Collaboration. 2024. Reproducibility in Management Science. <i>Management Science</i>.','small')
section('Other Information')
line('<b>Computer skills:</b> Python, SAS, R, Matlab, SQL, LaTeX.','small')
line('<b>Databases:</b> CRSP, Compustat, OptionMetrics, Bloomberg, IBES, Markit, TRACE, Refinitiv.','small')
line('<b>Languages:</b> Chinese (native); English (fluent).','small')
items.append(PageBreak())
section('References')
for name,position,affiliation,email in [
 ('Jie (Jay) Cao','Professor of Finance','School of Accounting and Finance, The Hong Kong Polytechnic University','jie.cao@polyu.edu.hk'),
 ('Bing Han','Chair Professor of Finance','Rotman School of Management, University of Toronto','bing.han@rotman.utoronto.ca'),
 ('Xintong Zhan','Li-Dasan Chair Professor of Finance','School of Management, Fudan University','xintongzhan@fudan.edu.cn'),
 ('Gang Li','Assistant Professor of Finance','Department of Finance, CUHK Business School, The Chinese University of Hong Kong','gang.li@cuhk.edu.hk'),
]:
 items.append(KeepTogether([para(f'<b>{escape(name)}</b> | {escape(position)}'),para(escape(affiliation)),para(f'<link href="mailto:{email}">{email}</link>')]))
 items.append(Spacer(1,5*mm))

def footer(canvas,doc):
 canvas.saveState();canvas.setFont('CVSans',8);canvas.setFillColor(colors.HexColor('#66717d'))
 canvas.drawString(18*mm,12*mm,'Ruijing (Chandler) Yang | Curriculum Vitae')
 canvas.drawRightString(A4[0]-18*mm,12*mm,str(doc.page));canvas.restoreState()

doc=SimpleDocTemplate(str(ROOT/'files/Ruijing_Yang_CV.pdf'),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=16*mm,bottomMargin=20*mm,title='Ruijing (Chandler) Yang - Curriculum Vitae',author='Ruijing Yang')
doc.build(items,onFirstPage=footer,onLaterPages=footer)
print('Updated files/Ruijing_Yang_CV.pdf')
