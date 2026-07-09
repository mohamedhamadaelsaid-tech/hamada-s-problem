#!/usr/bin/env python3
"""
Convert plain-text tables in GreenLab book chapters to proper LaTeX longtable environments.
Fixed version - handles ligatures and special characters properly.
"""
import os

ROOT = "/home/mohamedhamada/book/BookV3/greenlab-book"

# =========================================================
# TABLE 1.1 - GreenLab Monthly Project Timeline (Oct-June)
# =========================================================
TABLE_1_1 = r"""\begin{longtable}{|L{1.5cm}|L{1.8cm}|L{3.8cm}|L{5cm}|}
\caption{GreenLab Monthly Project Timeline (October--June)} \label{tab:1-1} \\
\hline
\rowcolor{gray!25}
\textbf{Month} & \textbf{Phase} & \textbf{Focus} & \textbf{Core Deliverable} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{Month} & \textbf{Phase} & \textbf{Focus} & \textbf{Core Deliverable} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
October & Phase 1 & Literature Review \& Requirements Foundation & Literature review document; draft requirements specification \\
\hline
November & Phase 2 & Use Cases \& Feature Definition & Use case diagram; feature definition document \\
\hline
December & Phase 3 & Architecture \& Database Schema & Four-tier architecture diagram; 11-table database schema; API specification \\
\hline
January & Phase 4 & ESP32 Firmware Development & Working firmware with sensor polling and relay control \\
\hline
February & Phase 5 & ASP.NET Core Backend Development & Functional REST API with automation engine and audit middleware \\
\hline
March & Phase 6 & Python YOLO Occupancy Service & Working YOLO service integrated with backend \\
\hline
April & Phase 7 & Angular Dashboard \& Full-System Integration & Working dashboard; end-to-end integration test log \\
\hline
May & Phase 8a & Report Writing \& Consolidation & Draft Chapters 3--6 of the LaTeX report \\
\hline
June & Phase 8b & Final Compilation \& Submission & Compiled seven-chapter PDF and submission package \\
\hline
\end{longtable}

"""

# =========================================================
# TABLE 2.1 - Comprehensive Feature Comparison Matrix
# =========================================================
TABLE_2_1 = r"""\begin{longtable}{|L{2.3cm}|L{1.8cm}|L{1.9cm}|L{1.9cm}|L{1.8cm}|L{1.8cm}|L{1.7cm}|L{2cm}|}
\caption{Comprehensive Feature Comparison Matrix} \label{tab:2-1} \\
\hline
\rowcolor{gray!25}
\textbf{Dimension} & \textbf{Challa et al. (2025)} & \textbf{Waghchoure et al. (2025)} & \textbf{Wibowo et al. (2023)} & \textbf{Ahmed et al. (2020)} & \textbf{Ingole et al. (2024)} & \textbf{SmartHaus} & \textbf{GreenLab} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{Dimension} & \textbf{Challa et al. (2025)} & \textbf{Waghchoure et al. (2025)} & \textbf{Wibowo et al. (2023)} & \textbf{Ahmed et al. (2020)} & \textbf{Ingole et al. (2024)} & \textbf{SmartHaus} & \textbf{GreenLab} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
Target environment & Classroom & Classroom & University laboratory & Classroom & Classroom & Generic home/IoT & Faculty laboratory \\
\hline
Sensing (multi-modal) & \checkmark\ Camera + gas sensor & \checkmark\ PIR + camera & \checkmark\ IoT sensor network & \checkmark\ Motion + environmental & \checkmark\ LDR + temperature & \ding{55}\ No environmental sensing & \checkmark\ LDR + DHT11 + HC-SR04 \\
\hline
AI / Computer vision & \checkmark\ YOLOv4 (face-based) & Partial (camera verification, no count) & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \checkmark\ YOLO-based person counting \\
\hline
Automated lighting control & \ding{55} & \checkmark & \checkmark & \checkmark & \checkmark & Partial (manual pin write) & \checkmark\ Decision-matrix driven \\
\hline
Automated ventilation / HVAC control & \checkmark\ HVAC-linked & \checkmark\ Fans & Partial & \checkmark\ Fans & \checkmark\ Fans & Partial (manual pin write) & \checkmark\ Fan activation table \\
\hline
Web dashboard & \ding{55} & \ding{55} & \checkmark\ Monitoring only & \checkmark\ Monitoring + basic override & Partial (Wi-Fi command only, no UI) & \checkmark\ Angular dashboard & \checkmark\ Angular SPA dashboard \\
\hline
Role-based access control (Governance) & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \checkmark\ Instructor / Administrator / Service roles \\
\hline
Manual override with expiry & \ding{55} & \ding{55} & Basic, no expiry & Basic, no expiry & \checkmark\ Wi-Fi only, unauthenticated & \ding{55} & \checkmark\ Time-limited, authenticated, auditable \\
\hline
Audit logging / accountability & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \checkmark\ Tamper-resistant audit log \\
\hline
Laboratory transfer workflow & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \ding{55} & \checkmark\ Request and approval workflow \\
\hline
Backend persistence layer & Partial (local processing only) & \ding{55} & \checkmark\ Centralised monitoring & Partial & \ding{55} & \checkmark\ Node.js server & \checkmark\ ASP.NET Core + SQL Server \\
\hline
\end{longtable}

{\small \textit{Sources: Challa et al. [?]; Waghchoure et al. [?]; Wibowo et al. [?]; Ahmed et al. [?]; Ingole et al. [?]; SmartHaus [?].}}

"""

# =========================================================
# TABLE 3.1 - Four-Tier Architecture
# =========================================================
TABLE_3_1 = r"""\begin{longtable}{|L{1.5cm}|L{3.5cm}|L{3.5cm}|L{5cm}|}
\caption{GreenLab four-tier architecture and tier responsibilities.} \label{tab:3-1} \\
\hline
\rowcolor{gray!25}
\textbf{Tier} & \textbf{Exact Term} & \textbf{Technology} & \textbf{Responsibility} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{Tier} & \textbf{Exact Term} & \textbf{Technology} & \textbf{Responsibility} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
Tier 1 & the hardware layer & ESP32 + Sensors + Relay & Sensing, relay control, entry/exit counting \\
\hline
Tier 2 & the Python AI service & Python + YOLOv11n & Visual occupancy detection, person counting \\
\hline
Tier 3 & the ASP.NET Core backend & ASP.NET Core 8 + SQL Server & Automation engine, API, RBAC, audit logging \\
\hline
Tier 4 & the Angular dashboard & Angular SPA & Real-time monitoring, override, admin governance \\
\hline
\end{longtable}

"""

# =========================================================
# TABLE 3.2 - Feature Dependency Chain
# =========================================================
TABLE_3_2 = r"""\begin{longtable}{|L{4cm}|L{3cm}|L{5.5cm}|}
\caption{Feature dependency chain across the four-tier architecture.} \label{tab:3-2} \\
\hline
\rowcolor{gray!25}
\textbf{Feature(s)} & \textbf{Depends On} & \textbf{Reason} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{Feature(s)} & \textbf{Depends On} & \textbf{Reason} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
FE-01, FE-02, FE-03, FE-04 & BE-03 & All frontend features require authentication (JWT) \\
\hline
BE-01 & HW-01, AI-01, AI-02 & Automation engine needs live sensor + occupancy data \\
\hline
HW-02 & BE-01, BE-02 & Relay control driven by automation engine or override \\
\hline
BE-02 & BE-03, BE-04 & Override requires auth and generates audit log entries \\
\hline
\end{longtable}

"""

# =========================================================
# TABLE 3.3 - Business Model Canvas blocks
# =========================================================
TABLE_3_3 = r"""\begin{longtable}{|L{4cm}|L{8.5cm}|}
\caption{Business Model Canvas blocks traced to their chapter basis.} \label{tab:3-3} \\
\hline
\rowcolor{gray!25}
\textbf{BMC Block} & \textbf{Chapter Basis} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{BMC Block} & \textbf{Chapter Basis} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
Value Propositions & FR-LC, FR-VC, FR-OD, FR-MO, FR-MD, NFR-SCAL \\
\hline
Customer Segments & Table 3.4 (Stakeholder Analysis); Faculty Management (primary), IT Department / Laboratory Staff / Administrator (secondary) \\
\hline
Customer Relationships & NFR-USA-01, NFR-MAIN-01 \\
\hline
Key Partners & Table 3.1 (four-tier architecture); Section 3.2.2 \\
\hline
Key Activities & UC-09--UC-13 (Section 3.5.3) \\
\hline
Key Resources & Section 3.2 (tier responsibilities) \\
\hline
Channels & Section 3.7.6 (Scalability) \\
\hline
Cost Structure & Table 3.1 tier technologies \\
\hline
Revenue Streams & Section 3.7.2 (Reliability) \\
\hline
\end{longtable}

"""

# =========================================================
# TABLE 3.4 - Stakeholder analysis
# =========================================================
TABLE_3_4 = r"""\begin{longtable}{|L{2.5cm}|L{3cm}|L{3.5cm}|L{3.5cm}|}
\caption{Stakeholder analysis summary.} \label{tab:3-4} \\
\hline
\rowcolor{gray!25}
\textbf{Stakeholder} & \textbf{Role} & \textbf{Primary Concern} & \textbf{System Features} \\
\hline
\endfirsthead
\hline
\rowcolor{gray!25}
\textbf{Stakeholder} & \textbf{Role} & \textbf{Primary Concern} & \textbf{System Features} \\
\hline
\endhead
\hline
\endfoot
\hline
\endlastfoot
Instructor & Conducts sessions, monitors assigned labs, overrides automation when teaching needs it, requests transfers & Automatic control must not interfere with teaching & Real-time dashboard, manual override with timed expiry, transfer request form \\
\hline
Administrator & Manages users, schedules, transfers, and configuration; reviews audit logs and faults & Operational oversight, policy compliance, accountability & User management, schedule management, transfer approval, audit log, fault acknowledgement \\
\hline
Laboratory Staff & Monitors hardware integrity, responds to fault alerts, maintains equipment & Hardware faults detected and resolved before they compromise safety & Fault alert dashboard, sensor status display, relay feedback \\
\hline
Student & Occupies the laboratory; an indirect beneficiary & A comfortable environment without needing to interact with the system & Indirect benefit through occupancy-driven lighting and ventilation \\
\hline
IT Department & Maintains network, server, and security infrastructure & Reliable infrastructure, security compliance, updateable firmware & HTTPS, JWT, service accounts, firmware update support, network configuration \\
\hline
Faculty Management & Reviews energy trends and policy compliance; authorises budget & Energy cost reduction, environmental responsibility, auditability & Energy reports, audit log review, configuration oversight \\
\hline
\end{longtable}

"""


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Written: {path}")


def find_marker(content, marker, start=0):
    """Find a marker in content, returning position or -1."""
    idx = content.find(marker, start)
    if idx >= 0:
        print(f"    Found '{marker[:50]}...' at position {idx}")
    else:
        print(f"    NOT FOUND: '{marker[:50]}...'")
    return idx


def main():
    # 1. Fix main.tex - add pifont
    print("\n=== main.tex ===")
    main_path = os.path.join(ROOT, "main.tex")
    main_content = read_file(main_path)
    if '\\usepackage{pifont}' not in main_content:
        main_content = main_content.replace(
            '\\usepackage{amssymb}',
            '\\usepackage{amssymb}\n\\usepackage{pifont}'
        )
        print("  Added pifont package")
    write_file(main_path, main_content)
    
    # 2. Fix ch01.tex - Table 1.1
    print("\n=== ch01.tex (Table 1.1) ===")
    ch1_path = os.path.join(ROOT, "ch01", "ch01.tex")
    ch1 = read_file(ch1_path)
    
    start_marker = "Table 1.1: GreenLab Monthly Project Timeline (October--June)"
    end_marker = "\\section{Scope}"
    
    start_idx = find_marker(ch1, start_marker)
    end_idx = find_marker(ch1, end_marker)
    
    if start_idx >= 0 and end_idx > start_idx:
        ch1 = ch1[:start_idx] + TABLE_1_1 + ch1[end_idx:]
        print("  Replaced Table 1.1 OK")
    write_file(ch1_path, ch1)
    
    # 3. Fix ch02.tex - Table 2.1
    print("\n=== ch02.tex (Table 2.1) ===")
    ch2_path = os.path.join(ROOT, "ch02", "ch02.tex")
    ch2 = read_file(ch2_path)
    
    start_marker = "Table 2.1: Comprehensive Feature Comparison Matrix"
    # Use just "comparison table" and find the next occurrence (not the one in chapter summary)
    # Look for the paragraph that starts after the table
    start_idx = find_marker(ch2, start_marker)
    
    # Find the paragraph after the table - look for "The comparison table" (with ligature)
    # Let's search for just "comparison table con"
    end_marker = "comparison table"  # Use partial match
    search_start = start_idx + len(start_marker)
    end_idx = ch2.find(end_marker, search_start)
    
    if end_idx >= 0:
        # Walk back to find the start of this paragraph (after a blank line)
        print(f"    Found 'comparison table...' at position {end_idx}")
        # We want to go back to right after the "Sources: ..." line + blank line
        sources_idx = ch2.rfind("Sources:", start_idx, end_idx)
        if sources_idx >= 0:
            # Find the next newline after Sources:
            end_of_sources = ch2.find("\n\n", sources_idx)
            if end_of_sources >= 0:
                end_idx = end_of_sources + 2
            else:
                end_idx = ch2.find("\n", sources_idx) + 1
        
        if start_idx >= 0 and end_idx > start_idx:
            ch2 = ch2[:start_idx] + TABLE_2_1 + "\n" + ch2[end_idx:]
            print("  Replaced Table 2.1 OK")
    else:
        print(f"  ERROR: Could not mark end of Table 2.1")
    
    write_file(ch2_path, ch2)
    
    # 4. Fix ch03.tex - Tables 3.1, 3.2, 3.3, 3.4
    print("\n=== ch03.tex ===")
    ch3_path = os.path.join(ROOT, "ch03", "ch03.tex")
    ch3 = read_file(ch3_path)
    
    # Table 3.1
    print("\n--- Table 3.1 ---")
    start_marker = "Table 3.1: GreenLab four-tier architecture and tier responsibilities."
    # Use the actual comment marker exactly as it appears in the file
    end_marker = "% --- FIGURE PLACEHOLDER: Figure 3.1 ---"
    
    start_idx = find_marker(ch3, start_marker)
    end_idx = find_marker(ch3, end_marker, start_idx)
    
    if start_idx >= 0 and end_idx > start_idx:
        ch3 = ch3[:start_idx] + TABLE_3_1 + ch3[end_idx:]
        print("  Replaced Table 3.1 OK")
    else:
        print(f"  ERROR: Cannot replace Table 3.1")
    
    # Table 3.2
    print("\n--- Table 3.2 ---")
    start_marker = "Table 3.2: Feature dependency chain across the four-tier architecture."
    end_marker = "\\subsection{Temporal Dimension}"
    
    start_idx = find_marker(ch3, start_marker)
    end_idx = find_marker(ch3, end_marker, start_idx)
    
    if start_idx >= 0 and end_idx > start_idx:
        ch3 = ch3[:start_idx] + TABLE_3_2 + ch3[end_idx:]
        print("  Replaced Table 3.2 OK")
    else:
        print(f"  ERROR: Cannot replace Table 3.2")
    
    # Table 3.3
    print("\n--- Table 3.3 ---")
    start_marker = "Table 3.3: Business Model Canvas blocks traced to their chapter basis."
    # Find the third occurrence of Figure 3.2 placeholder (the one AFTER the BMC table content)
    # Looking at the data: occurrence #5 is at 19525 which is AFTER Table 3.3 at 18856
    # That's "% --- FIGURE PLACEHOLDER: Figure 3.2 ---"
    end_marker = "% --- FIGURE PLACEHOLDER: Figure 3.2 ---"
    
    start_idx = find_marker(ch3, start_marker)
    
    if start_idx >= 0:
        # Find the LAST occurrence of the figure 3.2 placeholder before "Read alongside the rest"
        fig32_placeholders = []
        pos = 0
        while True:
            pos = ch3.find(end_marker, pos)
            if pos < 0:
                break
            fig32_placeholders.append(pos)
            pos += 1
        print(f"    Found {len(fig32_placeholders)} Figure 3.2 placeholders")
        
        # The placeholder we want is the one AFTER Table 3.3 (occurrence #5 at 19525)
        # But actually we want to replace the table + the placeholder + the sentence after it
        # Let me find the text "Read alongside the rest of this chapter" which follows
        read_alongside = ch3.find("Read alongside the rest of this chapter", start_idx)
        print(f"    'Read alongside...' at {read_alongside}")
        
        if read_alongside > start_idx:
            ch3 = ch3[:start_idx] + TABLE_3_3 + ch3[read_alongside:]
            print("  Replaced Table 3.3 OK")
        else:
            print(f"  ERROR finding end for Table 3.3")
    
    # Table 3.4
    print("\n--- Table 3.4 ---")
    start_marker = "Table 3.4: Stakeholder analysis summary."
    end_marker = "\\section{Use Case Analysis}"
    
    start_idx = find_marker(ch3, start_marker)
    end_idx = find_marker(ch3, end_marker, start_idx)
    
    if start_idx >= 0 and end_idx > start_idx:
        ch3 = ch3[:start_idx] + TABLE_3_4 + "\n" + ch3[end_idx:]
        print("  Replaced Table 3.4 OK")
    else:
        print(f"  ERROR: Cannot replace Table 3.4")
    
    write_file(ch3_path, ch3)
    
    print("\n=== All table replacements complete ===")


if __name__ == "__main__":
    main()
