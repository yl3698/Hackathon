# AI-Powered Law Website
* This project was done as part of Cornell's LII Hackathon - only 22 people were selected overall to participate.
* Based on the website https://www.law.cornell.edu/wex

This repository contains the code and solutions developed during the LII Hackathon 2024, aiming to improve the Legal Information Institute's (LII) Wex legal dictionary and encyclopedia. The primary goals of this project are to address the issues related to taxonomy, tagging, search system, and context-providing within Wex. while leveraging cutting-edge AI technology and web automation. In order to address these problems, we integrated AI technology and web automation.

# Problems Addressed
1. **Tagging System**: The existing tagging system for legal definitions suffered from tags being either too specific, too broad, or containing duplicates, leading to an unruly mixture of unlike objects.
2. **Search and Filtering:** The search and filtering capabilities for legal definitions and court cases were limited, making it challenging for users to find relevant information efficiently.
3. **Context and Accessibility:** The tags lacked context and definitions, placing users in the dark, and the overall accessibility of Wex needed improvement.
4. **Court Case Integration:** Wex lacked a dedicated section for court cases, and the process of compiling and integrating these cases was manual and time-consuming.

# Innovative Solutions
_**Legal Definitions**_
1. **AI-powered Automatic Tagging:** We have implemented an AI-driven system that leverages OpenAI's vectorization technology to automatically tag legal definitions. This system calculates the numerical correlation between legal definitions and taxonomical labels, ensuring accurate and efficient tagging. The tagging process is entirely automated, and the taxonomy can be easily modified by adjusting a single line of code.
2. **Improved Search and Filtering:**
-  _Backend:_ **AI Recommender System** The vectorization system uses a similarity search that's not restricted by the previous tags set by the admin. In this way, the most to least relevant legal definitions/court cases will pop up based on their description and not just their tags. For example, a search of the word "robots" would originally bring definitions/cases that have the tag called "robots" (if it exists) or if "robots" existed in the title. With this improvement, any definition/case with robots in their description, title, and tag would first be brought up, followed by related definitions/cases such as "AI", then "technology". This also addresses the feasibility of transitioning to this new system as old tags don't need to be redone by professionals, but rather they can be used more as a category system for users to pick through to learn concepts by themselves (essentially making the searching system more optimized by seperating the need of tags to more of a user-side feature for easier accessibility)
- _Frontend:_ The landing page now features main tags/categories that lead users to all relevant definitions for that category. After selecting a category or using the search bar, users can access a more detailed filter with subcategories, allowing for precise or broad searches based on their needs. All searches are ranked by relevance, displaying the most pertinent results first.

3. **Context and Accessibility Enhancements:** Hovering over the categories on the main page or the definitions page now provides a short description, increasing the overall accessibility and understanding of Wex's functionalities.

_**Court Cases**_
1. **Automated Web Scraping and Integration:** We have developed an automated web scraping system that retrieves the latest court decisions from government websites, ensuring that Wex's case database remains perpetually synchronized with publicly available information. This system eliminates the need for manual curation and integration of court cases.
2. **AI-powered Tagging:** The same AI-powered tagging system used for legal definitions is employed for court cases, automatically sorting and categorizing them within Wex's database.
3. **Filtering and Search Integration:** Users can filter and search for both legal definitions and court cases seamlessly from the home page, enhancing the overall user experience and preventing confusion.

# Technical Implementation
Our solutions leverage cutting-edge AI technology from OpenAI, web automation, and Python libraries such as langchain, faiss, requests, and BeautifulSoup. The code is well-documented and adheres to ethical principles, ensuring that no private or copyrighted material is used, and all AI implementations are transparent and documented.

_**Benefits and Impact**_
- **Innovative AI Implementation:** Our project showcases a groundbreaking and ethical implementation of AI in legal education, paving the way for future advancements in the field.
- **Reduced Manual Labor:** By automating the tagging, compilation, and integration processes, our solutions significantly reduce the manual labor required, allowing the LII team to focus on more critical tasks.
- **Accessibility and User Experience:** The improved search, filtering, and context-providing features enhance the overall accessibility and user experience of Wex, making it easier for users to navigate and understand legal information.
- **Continuous Updates:** The automated web scraping system ensures that Wex's court case database remains perpetually synchronized with the latest legal information, providing users with access to up-to-date jurisprudence.

# Getting Started
To commence work with the project, follow these steps:

1. Clone the repository: git clone [https://github.com/your-repo/lii-hackathon-2024.git](https://github.com/yl3698/Hackathon.git)
2. Install the required dependencies: pip install langchain faiss-cpu [or -gpu] openai
3. Create abd apply the OPENAI API key to the code
4. Execute the appropriate scripts for legal definitions and court case integration.
5. For comprehensive instructions and documentation, please refer to the respective files and directories within the repository.

# Contributing
Contributions to this project are welcomed and encouraged. If you have any ideas, bug fixes, or improvements, please submit a pull request. Ensure that you adhere to the established coding guidelines and provide clear documentation for your changes.

# License
This project is licensed under the MIT License.

# Acknowledgments
We express our sincere gratitude to the Legal Information Institute (LII) and Cornell Law School for organizing the LII Hackathon 2024 and providing us with the opportunity to contribute to this invaluable resource. We also acknowledge the contributions of OpenAI and the developers of the Python libraries utilized in this project.

  
