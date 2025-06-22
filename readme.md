# Easy Eco Warrior Email Helper

Welcome to the Easy Eco Warrior Email Helper! This powerful tool is designed to make reaching out to potential partners for sustainability initiatives smoother and more effective. It helps you create personalized and impactful outreach emails to companies, suggesting specific ways they can become more eco-friendly and making collaboration simple.

### What Does It Do?

This helper automates the creation and sending of emails to companies you want to invite to join the "Easy Eco Warrior" campaign. It's smart enough to understand a company's business and then suggest highly relevant actions they can take to boost their sustainability efforts.

**Key features:**

* **Smart Email Writing:** Automatically generates compelling subject lines and email body text that are tailored to the specific company you're contacting.
* **Customized Eco-Suggestions:** Identifies and provides practical, actionable steps a company can take to improve its environmental footprint. These aren't just generic tips; they are chosen to be specifically relevant to that company's type of business and operations.
* **Automated Sending:** Once the email is perfectly crafted, the tool can send it directly from your linked Gmail account.
* **CC Option:** You can easily include an additional email address in the 'Carbon Copy' (CC) field if you need to keep another person informed.

### How It Works (Simply!)

You provide the name of a company and its main email address. The helper then:

1.  **Learns about the Company:** It quickly gathers some public information about the company to understand what they do and what their business is all about.
2.  **Picks Eco-Actions:** Based on what it learns, it thoughtfully selects the 3 most suitable "Easy Eco Warrior" actions from a list of possibilities – these are practical steps the company can realistically put into practice.
3.  **Writes the Email:** It then crafts a friendly, concise, and clear email. This includes an introduction to the Easy Eco Warrior campaign, explains the benefits of partnering, and seamlessly integrates those specific eco-actions tailored just for them.
4.  **Sends It Off:** Finally, it sends the email directly from your linked Gmail account to the company. If you've chosen to CC someone, they will also receive a copy.

---

### Getting Started (Setup)

To use this tool, you'll need to do a one-time setup:

1.  **Get the Files:** First, you'll need to download all the project files onto your computer. If you're familiar with Git, you can "clone" the repository. Otherwise, download the project as a ZIP file and extract it to a folder.

2.  **Install Necessary Tools:** Open your computer's command prompt or terminal and navigate to the folder where you saved the project. Then, you'll run a command to install all the necessary components. This command will get everything ready for the helper to run.

3.  **Important Keys (for security):**
    For security reasons, the tool needs two special "keys" to work properly. Think of these as secure passes that allow the tool to access the powerful "brain" that writes the emails (Google's AI) and to send emails through your Gmail account. **It's crucial that you never share these keys with anyone or include them directly in the project's files.**

    You'll need to set these up on your computer as "environment variables."

    * **Google Gemini API Key (`GEMINI_API_KEY`):** This key allows the tool to use Google's smart AI to generate the email content and suggest sustainability actions. You can obtain your own API key by visiting [Google AI Studio](https://aistudio.google.com/). Follow their instructions to create a new API key.

    * **Gmail App Password (`EMAIL_APP_PASSWORD`):** This is a special, secure password for your Gmail account that allows programs like this helper to send emails on your behalf without needing your main Gmail password.
        * **To get one:**
            * You **must** have 2-Step Verification enabled on your Google Account first. If you don't, you'll be prompted to set it up.
            * Once 2-Step Verification is active, go to: https://myaccount.google.com/apppasswords
            * Follow the on-screen prompts to generate a new 16-character app password.
            * **Important:** This password is shown only once. Make sure to copy it down immediately, as you won't be able to see it again after you close the window. If you lose it, you'll simply generate a new one.

    **How to set these keys (this varies slightly by your computer's operating system):**
    You'll use specific commands in your computer's terminal or command prompt to tell your system about these keys. The exact command depends on whether you're using a Mac/Linux computer or a Windows computer (either Command Prompt or PowerShell). You can find detailed instructions by searching online for "how to set environment variables" for your specific operating system. The goal is to make sure your computer knows the values for `GEMINI_API_KEY` and `EMAIL_APP_PASSWORD` before you run the helper.

---

### How to Use

Once the setup is complete, you can run the email helper!

1.  **Open your terminal or command prompt** and navigate to the project folder where you saved the files.
2.  **Run the main script.** You'll execute a command that starts the helper. The script will then handle generating and attempting to send the email based on the company information you've provided within the project's files.

### Important Things to Remember

* **Email Sending Limits:** Be aware that Gmail has limits on how many emails you can send in a day. Sending too many too quickly might lead to temporary blocks from Google.
* **Security:** Always keep your API keys and app passwords private! Never share them or commit them to version control.
* **Check Your Emails:** After running the helper, it's a good practice to check your sent folder in Gmail to confirm that the email went out successfully.
