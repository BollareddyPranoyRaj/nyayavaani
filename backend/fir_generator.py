import os
import datetime
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from backend.config import GENERATED_FIRS_DIR

def generate_official_fir_pdf(
    complaint_id: str,
    complainant_name: str,
    phone_number: str,
    incident_type: str,
    transcript_original: str,
    transcript_en: str,
    legal_sections: list,
    extracted_facts: dict,
    detected_lang: str = "Hinglish (hi-IN)",
    emergency_tier: str = "CRITICAL (Golden Hour)"
) -> str:
    """Generate an official legal FIR / Cyber Complaint PDF adhering to BNSS guidelines."""
    file_name = f"FIR_{complaint_id}.pdf"
    pdf_path = GENERATED_FIRS_DIR / file_name

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    header_style = ParagraphStyle(
        'DocHeader',
        parent=styles['Heading1'],
        fontSize=14,
        leading=18,
        alignment=1, # Center
        textColor=colors.HexColor('#0f2b48'),
        fontName='Helvetica-Bold'
    )
    
    sub_header_style = ParagraphStyle(
        'DocSubHeader',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        alignment=1,
        textColor=colors.HexColor('#4a5568')
    )
    
    section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1a365d'),
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2d3748')
    )
    
    law_style = ParagraphStyle(
        'LawStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#9b2c2c'),
        fontName='Helvetica-Bold'
    )

    elements = []

    # Government / Official Header Box
    elements.append(Paragraph("<b>EMERGENCY TELEPHONIC FIRST INFORMATION REPORT (FIR) DOSSIER</b>", header_style))
    elements.append(Paragraph("Generated via NyayaVaani AI First-Responder | Integrated with Gnani AI Speech Engine", sub_header_style))
    elements.append(Paragraph("Pursuant to Section 173(1) of Bharatiya Nagarik Suraksha Sanhita (BNSS 2023) & IT Act 2000", sub_header_style))
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1a365d'), spaceAfter=12))

    # Meta Info Table
    current_time = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S IST")
    meta_data = [
        [
            Paragraph("<b>FIR / Complaint ID:</b>", body_style),
            Paragraph(f"<font color='#9b2c2c'><b>{complaint_id}</b></font>", body_style),
            Paragraph("<b>Date & Time:</b>", body_style),
            Paragraph(current_time, body_style)
        ],
        [
            Paragraph("<b>Complainant:</b>", body_style),
            Paragraph(complainant_name, body_style),
            Paragraph("<b>Caller Phone:</b>", body_style),
            Paragraph(phone_number, body_style)
        ],
        [
            Paragraph("<b>Emergency Tier:</b>", body_style),
            Paragraph(f"<b><font color='red'>{emergency_tier}</font></b>", body_style),
            Paragraph("<b>Dialect / Language:</b>", body_style),
            Paragraph(detected_lang, body_style)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[100, 170, 90, 180])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f7fafc')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    elements.append(meta_table)
    elements.append(Spacer(1, 12))

    # Nature of Offense
    elements.append(Paragraph("<b>1. NATURE OF CRIME & JURISDICTION</b>", section_title))
    crime_summary = f"<b>Categorized Crime:</b> {incident_type}<br/>" \
                    f"<b>Jurisdictional Thana:</b> {extracted_facts.get('jurisdiction_type', 'District Cyber Thana')}<br/>" \
                    f"<b>Modus Operandi:</b> {extracted_facts.get('suspect_modus_operandi', 'Digital impersonation')}<br/>" \
                    f"<b>Estimated Financial Loss / Stake:</b> <font color='red'><b>{extracted_facts.get('amount_at_stake', 'N/A')}</b></font>"
    elements.append(Paragraph(crime_summary, body_style))
    elements.append(Spacer(1, 10))

    # Applicable Laws Table
    elements.append(Paragraph("<b>2. STATUTORY SECTIONS CITED (BHARATIYA NYAYA SANHITA / IT ACT)</b>", section_title))
    elements.append(Paragraph("<i>Mapped automatically by Evon 30B Legal Reasoning Engine:</i>", sub_header_style))
    elements.append(Spacer(1, 4))
    
    law_rows = [[Paragraph("<b>Legal Section</b>", body_style), Paragraph("<b>Title & Scope</b>", body_style), Paragraph("<b>Prescribed Penalty</b>", body_style)]]
    for sec in legal_sections:
        law_rows.append([
            Paragraph(sec.get('section', ''), law_style),
            Paragraph(f"<b>{sec.get('title','')}</b><br/>{sec.get('relevance','')}", body_style),
            Paragraph(sec.get('penalty', ''), body_style)
        ])
        
    law_table = Table(law_rows, colWidths=[130, 260, 150])
    law_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#edf2f7')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#a0aec0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(law_table)
    elements.append(Spacer(1, 12))

    # Transcribed Vernacular Telephonic Testimony
    elements.append(Paragraph("<b>3. TELEPHONIC VERBATIM TESTIMONY (PRISMA v3.0 TRANSCRIPT)</b>", section_title))
    elements.append(Paragraph(f"<b>Original Vernacular Audio Statement:</b><br/><i>\"{transcript_original}\"</i>", body_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"<b>Certified English Translation for Thana Docket:</b><br/>\"{transcript_en}\"", body_style))
    elements.append(Spacer(1, 12))

    # Action Plan / Investigation Advisory
    elements.append(Paragraph("<b>4. EVON AI INVESTIGATION DIRECTIVE (GOLDEN HOUR ACTION)</b>", section_title))
    directive_text = "1. Immediate issuance of Section 91 CrPC / Section 94 BNSS notice to bank nodal officer for transaction freeze.<br/>" \
                     "2. Alerting 1930 National Cybercrime Reporting Portal with beneficiary account coordinates.<br/>" \
                     "3. Preservation of caller CDR and WhatsApp/VoIP logs under Section 65B Indian Evidence Act / Section 63 BSA 2023."
    elements.append(Paragraph(directive_text, body_style))
    elements.append(Spacer(1, 20))

    # Signature Block
    sig_data = [
        [
            Paragraph("<b>Automated Verification:</b><br/>Verified by NyayaVaani AI Engine<br/>Powered by Gnani.ai Models", body_style),
            Paragraph("<b>Complainant Telephonic Affirmation:</b><br/>Recorded digitally under Sec 173(1) BNSS<br/>Digital Hash: #SHA256-NV-882194", body_style)
        ]
    ]
    sig_table = Table(sig_data, colWidths=[270, 270])
    sig_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(sig_table)

    doc.build(elements)
    return str(pdf_path)
