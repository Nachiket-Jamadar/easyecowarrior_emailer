
# Easy Eco Warrior Email Helper

Welcome to the Easy Eco Warrior Email Helper! This tool is designed to make reaching out to potential partners for sustainability initiatives much easier. It helps you create personalized and effective outreach emails to companies, suggesting specific ways they can become more eco-friendly.

### What Does It Do?

This helper automates the creation and sending of emails to companies you want to partner with for the Easy Eco Warrior campaign. It intelligently figures out what makes a company tick and suggests the most relevant ways they can join the sustainability movement.

**Key features:**

* **Smart Email Writing:** Automatically generates email subjects and body text that are tailored to the company you're contacting.
* **Customized Eco-Suggestions:** Identifies and suggests practical, actionable steps a company can take to improve its environmental impact. These aren't just generic tips; they're chosen specifically for that company's type of business.
* **Automated Sending:** Once the email is ready, the tool can send it directly from your Gmail account.

### How It Works (Simply!)

You provide the name of a company and its email address. The helper then:

1.  **Learns about the Company:** It quickly gathers some public information about the company to understand what they do.
2.  **Picks Eco-Actions:** Based on what it learns, it selects the 3 most suitable "Easy Eco Warrior" actions from a list of possibilities — actions the company can realistically put into practice.
3.  **Writes the Email:** It then crafts a friendly and clear email, introducing Easy Eco Warrior, explaining the benefits of partnering, and including those specific eco-actions tailored for them.
4.  **Sends It Off:** Finally, it sends the email directly from your linked Gmail account to the company.

---

### Getting Started (Setup)

To use this tool, you'll need to do a one-time setup:

1.  **Get the Files:** First, you'll need to download all the project files. If you're familiar with Git, you can "clone" the repository. Otherwise, download the project as a ZIP file and extract it.

2.  **Install Necessary Tools:** Open your computer's command prompt or terminal and navigate to the folder where you saved the project. Then, you'll run a command to get everything ready. This command installs a few small programs that your helper needs to run.

3.  **Important Keys (for security):**
    For security reasons, the tool needs two special "keys" to work properly. Think of these as secret passwords that let the tool access the powerful "brain" that writes the emails and send emails through your Gmail. **Never share these keys with anyone or put them directly into the code.**

    You'll need to set them up on your computer as "environment variables." Here's how:

    * **Google Gemini API Key (`GEMINI_API_KEY`):** This key lets the tool use Google's smart AI to generate emails and suggestions. You can get yours by visiting Google AI Studio. Follow their instructions to create an API key.

    * **Gmail App Password (`EMAIL_APP_PASSWORD`):** This is a special password for your Gmail account that allows the tool to send emails without needing your main Gmail password.
        * **To get one:** Go to your Google Account > Security > How you sign in to Google > App passwords. If you don't see "App passwords," you might need to enable "2-Step Verification" first for security.

    **How to set these keys (this varies slightly by your computer's operating system):**
    You'll use specific commands in your terminal or command prompt to tell your computer about these keys. The exact command depends on whether you're using a Mac/Linux, Windows Command Prompt, or Windows PowerShell. Instructions for each are typically found when you search for "how to set environment variables" for your specific system. The goal is to set the `GEMINI_API_KEY` and `EMAIL_APP_PASSWORD` with the values you obtained.

---

### How to Use

Once setup is complete, you can run the email helper!

1.  **Open your terminal or command prompt** and navigate to the project folder.
2.  **Run the main script.** You'll execute a command that starts the helper. The script will then generate and attempt to send the email based on the company information you've set up within the code.

---

### Important Things to Remember

* **Email Sending Limits:** Be aware that Gmail has limits on how many emails you can send in a day. Don't send too many too quickly, or your account might be temporarily blocked.
* **Security:** Always keep your API keys and app passwords private!
* **Check Your Emails:** After running, it's a good idea to check your sent folder in Gmail to confirm the email went out.
