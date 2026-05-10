Team Members: Marissa Malosh, Jackie _______, Eesha Shahi
Project Name: Polished to Perfection Salon Management System
Role: UI Design, Dashboard Refactoring, Appointment Management Features, Streamlit Layout Improvements

## Phase 1 Contributions

During Phase 1 of the project, I contributed to the development of the customer appointment system and dashboard structure for our Streamlit application. I helped implement the customer and employee navigation system using Streamlit session state variables and sidebar navigation buttons. I also contributed to the dashboard KPI card system, appointment booking workflow, and overall page organization.

In the original version of the application, much of the code was contained directly inside `app.py`, which caused the file to become extremely large and repetitive. Many UI sections reused nearly identical layouts, and appointment management functionality was tightly coupled with dashboard rendering logic. This made the project difficult to maintain and harder for multiple team members to work on simultaneously.

I also helped implement the login and registration system using JSON file persistence. The system stored user accounts, appointments, and inventory information inside local JSON files and loaded them dynamically when the application started.

## Phase 1 Issues Identified

One major issue identified during Phase 1 was poor modularization. Nearly all logic existed in one file, including authentication, dashboard rendering, rewards, inventory management, appointment workflows, and chatbot functionality. This caused merge conflicts and made debugging more difficult.

Another issue was repetitive UI code. For example, many dashboard sections reused similar `st.container(border=True)` and `st.columns()` structures multiple times throughout the application. The application also lacked visual consistency across pages, with different layouts and spacing used in different sections.

Additionally, the original dashboard design was visually plain and difficult to scan quickly. Important information such as upcoming appointments, canceled appointments, and reward points did not stand out clearly to the user.

## Refactoring Example

One major refactoring improvement involved separating appointment functionality into its own UI module.

### Original Code

Originally, all appointment page logic existed directly inside `app.py`:

```python
elif st.session_state["page"] == "my_appointments":
    st.header("My Appointments")
    st.divider()

    history_search = st.text_input("Search by service")

    upcoming_tab, old_tab, canceled_tab = st.tabs(
        ["Upcoming", "Old", "Canceled"]
    )

    # appointment logic continued here...
```

This approach caused the main application file to become extremely large and difficult to navigate.

### Refactored Code

The appointment page was later modularized into a separate UI component:

```python
elif st.session_state["page"] == "my_appointments":
    appointments_ui.show_appointments(
        user_appts,
        appointments,
        save_appointments,
        save_inventory,
        is_past_appointment,
        update_inventory_for_service
    )
```

This refactoring significantly improved readability and organization by separating appointment management logic into its own reusable module. It also reduced duplication and made collaboration easier because different team members could work on separate files simultaneously without constantly editing the same large file.

## OOP and Modular Design Examples

Although the project primarily used functional programming rather than full object-oriented classes, we still applied modular software engineering principles throughout the application. Separate UI modules such as `appointments_ui`, `Rewards`, `Penny`, `Stock`, and `employee` helped isolate functionality into independent components.

Functions such as:

```python
get_user_appointments()
update_inventory_for_service()
redeem_reward_for_customer()
```

helped encapsulate reusable business logic instead of duplicating code throughout the application.

I also helped improve the visual structure of the dashboard using reusable Streamlit layout patterns such as bordered containers, KPI cards, centered column layouts, tabs, and sidebar navigation.

## Design, AI, and Testing Reflections

One of my major contributions during Phase 2 involved improving the visual design and usability of the application. I redesigned the customer dashboard using centered layouts, color-coded KPI cards, bordered containers, and more consistent spacing throughout the application. I also improved sidebar navigation by converting many buttons into full-width primary buttons for better usability and visual consistency.

AI tools were occasionally used to help troubleshoot Streamlit layout issues, debug date/time parsing problems, and assist with certain formatting functions. However, all project logic, integration, and implementation decisions were reviewed and modified manually by the team.

Testing involved repeatedly verifying appointment creation, cancellation workflows, inventory updates, rewards calculations, and session state navigation. I specifically tested whether canceled appointments correctly restored inventory quantities and whether past appointments displayed properly in the “Old” appointment section.

Overall, this project helped strengthen my understanding of modular software design, Streamlit UI development, state management, JSON persistence, and collaborative software engineering workflows.


