import os
import webbrowser
import tkinter as tk
from tkinter import messagebox, ttk

def generate_resume_html():
    # 1. Retrieve data from the GUI fields
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    summary = text_summary.get("1.0", tk.END).strip()
    degree = entry_degree.get().strip()
    school = entry_school.get().strip()
    year = entry_year.get().strip()
    job_title = entry_job.get().strip()
    company = entry_company.get().strip()
    job_desc = text_job.get("1.0", tk.END).strip()
    skills_raw = entry_skills.get().strip()

    # Validation: Ensure critical fields aren't empty
    if not name or not email or not phone:
        messagebox.showerror("Error", "Name, Email, and Phone are required fields!")
        return

    # Process skills into a clean list
    skills_list = [s.strip() for s in skills_raw.split(",") if s.strip()]
    skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills_list])

    # 2. Modern HTML/CSS Template for the Resume
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} - Resume</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #f0f2f5; color: #333; margin: 0; padding: 40px 0; }}
        .resume-card {{ max-width: 800px; background: white; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 10px solid #0056b3; display: flex; flex-direction: column; }}
        .header {{ padding: 40px; background: #f8f9fa; border-bottom: 1px solid #e9ecef; }}
        .header h1 {{ margin: 0; color: #0056b3; font-size: 32px; text-transform: uppercase; letter-spacing: 1px; }}
        .contact-info {{ margin-top: 10px; color: #666; font-size: 14px; }}
        .contact-info span {{ margin-right: 20px; }}
        .content {{ padding: 40px; }}
        .section {{ margin-bottom: 30px; }}
        .section-title {{ font-size: 18px; color: #0056b3; text-transform: uppercase; border-bottom: 2px solid #0056b3; padding-bottom: 5px; margin-bottom: 15px; font-weight: bold; }}
        .item {{ margin-bottom: 15px; }}
        .item-header {{ display: flex; justify-content: space-between; font-weight: bold; color: #444; }}
        .item-sub {{ color: #777; font-style: italic; margin-bottom: 5px; }}
        .skills-container {{ display: flex; flex-wrap: wrap; gap: 10px; }}
        .skill-badge {{ background: #e3f2fd; color: #0056b3; padding: 6px 12px; border-radius: 20px; font-size: 13px; font-weight: 500; }}
        .btn-print {{ text-align: center; margin-bottom: 20px; }}
        .btn-print button {{ background: #28a745; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 4px; cursor: pointer; font-weight: bold; }}
        @media print {{
            body {{ background: white; padding: 0; }}
            .resume-card {{ box-shadow: none; border-top: none; }}
            .btn-print {{ display: none; }}
        }}
    </style>
</head>
<body>

    <div class="btn-print">
        <button onclick="window.print()">Print / Save as PDF</button>
    </div>

    <div class="resume-card">
        <div class="header">
            <h1>{name}</h1>
            <div class="contact-info">
                <span><strong>Email:</strong> {email}</span>
                <span><strong>Phone:</strong> {phone}</span>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <div class="section-title">Professional Summary</div>
                <p style="margin: 0; line-height: 1.6; color: #555;">{summary}</p>
            </div>

            <div class="section">
                <div class="section-title">Work Experience</div>
                <div class="item">
                    <div class="item-header">
                        <span>{job_title}</span>
                    </div>
                    <div class="item-sub">{company}</div>
                    <p style="margin: 5px 0 0 0; line-height: 1.5; color: #555;">{job_desc}</p>
                </div>
            </div>

            <div class="section">
                <div class="section-title">Education</div>
                <div class="item">
                    <div class="item-header">
                        <span>{degree}</span>
                        <span>{year}</span>
                    </div>
                    <div class="item-sub">{school}</div>
                </div>
            </div>

            <div class="section">
                <div class="section-title">Skills</div>
                <div class="skills-container">
                    {skills_html}
                </div>
            </div>
        </div>
    </div>

</body>
</html>
"""

    # 3. Save the HTML file locally and open it in the default browser
    filename = f"{name.replace(' ', '_')}_resume.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_template)

    # Success Alert and auto-open
    messagebox.showinfo("Success", f"Resume successfully generated!\nSaved as: {filename}")
    webbrowser.open('file://' + os.path.realpath(filename))


# --- BUILDING THE GUI APPLICATION Window ---
root = tk.Tk()
root.title("Interactive Resume Creator")
root.geometry("500x650")
root.resizable(False, False)

# Main Container with Scrollbar feel
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Title
title_lbl = ttk.Label(main_frame, text="Enter Your Resume Details", font=("Helvetica", 14, "bold"), foreground="#0056b3")
title_lbl.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Helper layout function for form inputs
def create_field(label_text, row, is_textbox=False, height=3):
    lbl = ttk.Label(main_frame, text=label_text, font=("Helvetica", 10, "bold"))
    lbl.grid(row=row, column=0, sticky=tk.W, pady=4)
    if is_textbox:
        txt = tk.Text(main_frame, height=height, width=40, font=("Helvetica", 10), bd=1, relief=tk.SOLID)
        txt.grid(row=row, column=1, pady=4, sticky=tk.W)
        return txt
    else:
        ent = ttk.Entry(main_frame, width=43, font=("Helvetica", 10))
        ent.grid(row=row, column=1, pady=4, sticky=tk.W)
        return ent

# Generating the fields line by line
entry_name = create_field("Full Name:", 1)
entry_email = create_field("Email Address:", 2)
entry_phone = create_field("Phone Number:", 3)
text_summary = create_field("Bio/Summary:", 4, is_textbox=True, height=3)

entry_degree = create_field("Degree/Major:", 5)
entry_school = create_field("University Name:", 6)
entry_year = create_field("Graduation Year:", 7)

entry_job = create_field("Job Title:", 8)
entry_company = create_field("Company Name:", 9)
text_job = create_field("Job Duties:", 10, is_textbox=True, height=3)

entry_skills = create_field("Skills (use commas):", 11)

# Generate Button Style & Placement
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 11, "bold"), background="#28a745")

btn_submit = ttk.Button(main_frame, text="GENERATE RESUME", command=generate_resume_html)
btn_submit.grid(row=12, column=0, columnspan=2, pady=25, ipady=5)

# Run Tkinter app loop
root.mainloop()
