# sqlalchemy-challenge

![alchemy](https://github.com/s0uravk/sqlalchemy-challenge/assets/144293972/e10e7142-5304-45a2-936b-4d78f841192d)

**Accessing data**

In climate_starter.ipynb, engine instances are created using the local path of the SQLite file, which can be changed according to the database being accessed in the following format: "\<protocol\>\:\/\/\<username\>:\<password\>\@\<server\>\:\<port\>\/\<file-path\>". This script can work with any dialect of SQL with just a changing the protcol accordingly. In this case, the protocol is SQLite, with no need for a username or password to access the local SQLite file; the server or host is localhost; no port is required; and then the file path to the file to be accessed, which is in the Resources folder and named hawaii.sqlite, is created to reflect the tables in the SQLite file to be used in Python code. An instance of each table is saved to fetch the data, and a session object is created to link Python to the database. Then data is accessed using session.query and put into the Pandas dataframe, which is then visualized using the Matplotlib library. Data visualization represents precipitation in inches for one year from the most recent observation. Then the minimum, average, and maximum temperature elevations are calculated for the station with the most observations. For the next visualization, data is represented in a histogram for the frequency of different temperatures for one year from the most recent observation for the station with the most observations. Then the session is closed once we are done with the analysis.

**Creating an API**

For the app.py file, at first, the same method is used to reflect the database structure and then create instances of the tables to be accessed. Then, we create an instance of Flask named App, and then the homepage and other routes are created for the app. Here, we can access the data in a sqlite file using these routes in JSON format. Homepage lists the different routes we have in this app, and the second route returns the precipitation data for a year from the most recent observation. Going forward, the next route will return a list of stations. Third route here: return dates and temperatures for one year from the most recent observation for the station with the most observations. These three routes were static routes, where there was a fixed route. The next two are dynamic routes, where we can make some changes to the route to get the desired output. For this first dynamic route, a start date can be customized in the route where the minimum, maximum, and average of temperature observations across all the dates after the start date. And an end date is added for our next dynamic route, which performs the same function as the previous route, but the end date is also included and make calculations from start to end date, including the start and end dates. Then there is a command to run the app.



Below is the **clear and concise cheat sheet content** for your Condominium Manager Final Exam, as requested. This content is based on the provided notes, the previous data, and your specific requirements to include the roles of the CAO, CMSA, CMRAO, Land Registry Office, the three types of Reserve Fund Studies (RFS), and other relevant information. It is structured for quick reference during your open-book exam and can be copied into a word processor (e.g., Microsoft Word, Google Docs) to format and save as a PDF.
 
---
 
### Condominium Manager Final Exam Cheat Sheet
 
**Exam Date: Assumed for preparation in 2025**  
**Source: Condominium Act, 1998; Condominium Management Services Act, 2015 (CMSA); Provided Notes**
 
---
 
#### 1. Key Organizations and Their Roles
| **Entity** | **Role** |
|------------|----------|
| **Condominium Authority of Ontario (CAO)** | - Provides **directors’ training** (mandatory within 6 months of election/appointment).<br>- Maintains **public registry** of condominium directors.<br>- Offers resources for owners and corporations.<br>- Oversees the Condominium Authority Tribunal (CAT) for dispute resolution (e.g., records, pets, noise). |
| **Condominium Management Services Act, 2015 (CMSA)** | - Legislation enabling **licensing of condominium managers** in Ontario.<br>- Contains regulations with the **Code of Ethics** for licensed managers.<br>- Outlines **what** managers must do (regulations specify **how**). |
| **Condominium Management Regulatory Authority of Ontario (CMRAO)** | - **Regulates condominium managers** and management providers.<br>- Ensures **proper licensing** of Limited and General Licensees.<br>- Enforces compliance with CMSA and its regulations. |
| **Land Registry Office** | - **Registers documents** that create a condominium corporation (Declaration, Description, Bylaws).<br>- Assigns the **corporation name** upon registration.<br>- Registers **new bylaws** for them to become effective.<br>- Does **not** register rules. |
 
---
 
#### 2. Condominium Corporation Formation
- **Created When**: Declaration and Description are **registered at the Land Registry Office**, and **units are transferred to purchasers**.
- **Registered Documents**: Declaration, Description, Bylaws.
- **Non-Registered**: Rules, Annual Operating Plan.
- **Corporation Name**: Assigned by the Land Registrar at registration.
 
---
 
#### 3. Bylaws and Rules
| **Aspect** | **Bylaws** | **Rules** |
|------------|------------|-----------|
| **Creation** | Approved by **owners** and **registered at Land Registry Office**. | Created by **Board of Directors** at any time. |
| **Effective** | Only after **registration**. | After **30 days** if no owner objection. |
| **Challenge** | Requires owner approval to amend/repeal. | Owners can **requisition a meeting** (signed by **15% of unit owners**) to discuss/challenge. |
 
---
 
#### 4. Reserve Fund Studies (RFS)
| **Type** | **Description** | **Frequency** |
|----------|----------------|---------------|
| **Comprehensive Study** | Includes a **site inspection**; full assessment of reserve fund needs. | **Every 6 years**. |
| **Update with Site Inspection** | Updates the comprehensive study; includes a new site visit. | As part of the 6-year cycle, if needed. |
| **Update without Site Inspection** | Updates the reserve fund plan based on existing data, no site visit. | **Every 3 years**. |
 
- **Who Conducts**: Typically an **Engineer** or qualified professional.
- **Purpose**: Ensures adequate funds for major repairs/replacements.
 
---
 
#### 5. Licensing for Condominium Managers
| **License Type** | **Details** |
|------------------|-------------|
| **Limited Licensee** | - Must be employed by a **Condominium Management Provider**.<br>- Supervised by a **General Licensee**.<br>- Can **reply to residents’ emails**.<br>- Cannot spend >**$500** of client’s money without **prior approval** from Supervising General Licensee.<br>- Must obtain before applying for a General License. |
| **General Licensee** | - Supervises Limited Licensees.<br>- Has broader authority to manage condominium operations. |
 
- **Regulated By**: **CMRAO**.
- **Code of Ethics**: Found in **regulations under CMSA, 2015**.
 
---
 
#### 6. Key Documents
| **Document** | **Purpose** | **Registered?** |
|--------------|-------------|-----------------|
| **Declaration** | Specifies **unit boundaries**, **common expenses** (Schedule D: % share), and ownership rules. | Yes, on title. |
| **Description** | Details the **physical layout** of the condominium. | Yes, on title. |
| **Bylaws** | Govern **corporation operations**; include additional **director qualifications/disqualifications**. | Yes, on title. |
| **Rules** | Regulate **owner/tenant behavior**; created by the Board. | No. |
| **Annual Operating Plan** | Outlines **manager’s tasks** for the year; prepared by **Condominium Manager**. | No, not prescribed. |
| **Management Agreement** | Defines **manager’s responsibilities**. | No. |
| **Reserve Fund Study** | Plans for **major repairs/replacements**; conducted by an Engineer. | No. |
 
- **Prescribed Forms**: Found in **regulations** (e.g., Notice of Meeting, Proxy Form); Annual Operating Plan is **not** prescribed.
 
---
 
#### 7. Common Expenses
- **Calculated Based On**:
 - **Annual Budget**: Approved by the **Board of Directors**.
 - **Schedule D** in the Declaration: Specifies each unit’s **% share** of common expenses.
 
---
 
#### 8. Annual General Meeting (AGM)
- **Frequency**: At least **once a year**, within **6 months** of the fiscal year-end.
- **Quorum**: **25%** of owners for the first attempt.
- **Purpose**: Discuss budget, elect directors, review corporation matters.
 
---
 
#### 9. Board of Directors
- **Qualifications (Condominium Act, 1998)**:
 - **18+ years old**.
 - **Mentally capable**.
 - **Not bankrupt**.
 - **Mandatory CAO education** within **6 months** of election/appointment.
- **Additional Qualifications/Disqualifications**: Found in **corporation’s bylaws**.
- **Elected or Appointed**: By owners or the Board (for vacancies).
- **Role**: Approves **annual budget**, creates/amends/repeals **rules**, oversees corporation operations.
 
---
 
#### 10. Legislative Hierarchy
- **Human Rights Code**: **Supersedes all** (Condo Act, Declaration, Bylaws, Rules).
- **Condominium Act, 1998**: Overrides Declaration/Bylaws if conflicts.
- **Declaration/Bylaws/Rules**: Must comply with higher legislation.
- **CMSA, 2015**: Governs **manager licensing**, not condominium governance.
 
- **Legislation**: Tells **what** to do.
- **Regulations**: Tell **how** to do it.
 
---
 
#### 11. Key Legislation
| **Legislation** | **Purpose** |
|-----------------|-------------|
| **Condominium Act, 1998** | Governs **condominium corporations**, operations, and governance. Includes regulations with **prescribed forms** (e.g., Notice of Meeting). |
| **Condominium Management Services Act, 2015 (CMSA)** | Enables **licensing of managers**; includes **Code of Ethics** in regulations. |
 
---
 
#### 12. Handling Challenging Situations
- **Best Practice**: **All of the following**:
 - Act **professionally**.
 - **Empathize** with the individual.
 - **Acknowledge** the issue and **respond** appropriately.
- **Ethics**: Guided by the **Code of Ethics** in CMSA regulations; focus on what is **right and wrong** in decision-making.
 
---
 
#### 13. Exam Tips
- **Read Carefully**: Questions are **not tricky**; only **one correct answer**.
- **Focus on**: Protecting **owners’ rights**, following **legislation/regulations**.
- **Key Areas**:
 - Licensing requirements (Limited vs. General).
 - Document registration (Declaration, Bylaws vs. Rules).
 - Reserve Fund Studies (3 types, frequency).
 - Roles of CAO, CMRAO, Land Registry.
 - Legislative hierarchy (Human Rights Code > Condo Act > Declaration).
- **Check Email**: CMRAO provides exam details (format, rules).
