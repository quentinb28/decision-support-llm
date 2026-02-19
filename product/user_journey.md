# ALIGNMENT — PROTOTYPE USER JOURNEY (v0)

This prototype is designed to help users align their actions with the person they want to become by converting avoided decisions into real-world commitments and measuring execution over time.

---

# ONBOARDING (ONE-TIME SETUP)

## Phase 1 — Identity Anchor

### Prompt

Ask the user:

**“If you had no fear, who would you choose to become in difficult situations?”**

Clarify:

Describe how this version of you behaves when:

- there is conflict  
- something is uncomfortable  
- there is risk  
- you could avoid responsibility  
- or when action is costly  

---

### Example (shown to user)

> “I communicate directly even when it risks disapproval.  
> I take action on important things without waiting to feel ready.  
> I prioritize long-term growth over short-term comfort.  
> I maintain discipline with my health even when I’m busy.  
> I tell the truth even when it would be easier not to.”

User submits free-text description.

This becomes the:

**Identity Anchor**

---

## Phase 2 — AI Value Extraction

System parses the Identity Anchor and extracts:

Top 5 inferred values from the following set:

- Security  
- Belonging  
- Autonomy  
- Achievement  
- Status  
- Integrity  
- Growth  
- Contribution  
- Pleasure  
- Meaning  

Output example:

Your Identity Anchor suggests these core values:

- Integrity  
- Growth  
- Autonomy  
- Contribution  
- Achievement  

---

## Phase 3 — Value Ranking (Contextual Pairwise)

System ranks the extracted 5 values using contextual pairwise questions.

Questions must be situational.

---

### Example Question

In a situation where telling the truth may create conflict:

Would you prioritize:

Integrity  
Acting in accordance with your principles

or

Belonging  
Maintaining harmony and acceptance with others

---

Repeat contextual pairwise tradeoffs until a clear priority order is established.

Output:

**Value Hierarchy**

Example:

1. Integrity  
2. Growth  
3. Autonomy  
4. Contribution  
5. Achievement  

This becomes the user’s:

**Alignment Framework**

---

# DAILY LOOP (CORE PRODUCT)

## Phase 4 — Decision Capture

Ask:

**“What decision are you currently avoiding?”**

User inputs situation.

---

## Phase 5 — Option Generation

User can:

- enter their own options  
OR  
- request AI-generated options (Top 3)

AI generates:

- Comfort Option  
- Avoidance Option  
- Aligned Option  

(based on Identity Anchor + Value Hierarchy)

---

## Phase 6 — Alignment Selection

Ask:

**“Which option best reflects who you want to become and your top values?”**

User selects chosen course of action.

---

## Phase 7 — Commitment

User defines:

Smallest executable step that can realistically be completed within:

**48 hours**

User commits.

---

# 48 HOURS LATER

## Phase 8 — Follow Through Report

Ask:

Did you complete the action?

- Yes  
- No  

---

## Phase 9 — Alignment Report

Ask:

How aligned did this action feel with who you want to become?

Scale:

1 = Not aligned  
5 = Fully aligned  

---

# METRICS

## Follow Through Rate (FTR)

Measures execution.

**FTR = Actions Completed / Actions Committed**

---

## Self-Leadership Rate (SLR)

Measures autonomy in decision-making.

**SLR = User-Generated Options / Total Decisions Logged**

Higher SLR indicates reduced reliance on AI-generated options.

---

## Alignment Score (AS)

Measures perceived identity alignment.

**AS = Average user-reported alignment rating (1–5) across completed actions**

---

## Integrity Score (IS)

Measures knowledge-action consistency.

**IS = Completed Aligned Actions / Total Aligned Actions Chosen**

This is the primary outcome metric.

---

# PRODUCT LOOP

Identity Anchor  
↓  
Value Hierarchy  
↓  
Decision Logged  
↓  
Options Generated  
↓  
Aligned Action Chosen  
↓  
48h Commitment  
↓  
Execution Report  
↓  
Alignment Rating  
↓  
Integrity Score Updated  
