import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Function to create a table for a specific course
def create_table(course_code):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {course_code} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL
        )
    ''')
    conn.commit()

# Function to add questions to a specific course table
def add_question(course_code, question_text, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute(f'''
        INSERT INTO {course_code} (question_text, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question_text, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Create tables for each course
course_codes = ["DS3850", "DS3860", "DS3620", "DS4125", "BIOL3920"]
for course_code in course_codes:
    create_table(course_code)

# Questions for DS3850: Business Application Development (Python)
ds3850_questions = [
    ("What is the correct file extension for Python files?", ".py", ".pyt", ".python", ".pt", ".py"),
    ("Which of these is a correct way to create a function in Python?", "def myFunction()", "create function myFunction()", "func myFunction()", "define myFunction()", "def myFunction()"),
     ("What is the correct file extension for Python files?", ".py", ".pyt", ".python", ".pt", ".py"),
    ("Which of these is a correct way to create a function in Python?", "def myFunction()", "create function myFunction()", "func myFunction()", "define myFunction()", "def myFunction()"),
    ("Which operator is used for exponentiation in Python?", "^", "**", "//", "*", "**"),
    ("How do you insert comments in Python?", "// this is a comment", "# this is a comment", "/* this is a comment */", "<!-- this is a comment -->", "# this is a comment"),
    ("What data type is the result of '5 / 2' in Python 3?", "Integer", "Float", "String", "Complex", "Float"),
    ("Which method is used to add an item to the end of a list?", "append()", "insert()", "add()", "push()", "append()"),
    ("What keyword is used to create a class in Python?", "class", "define", "object", "structure", "class"),
    ("What does the 'len()' function do?", "Returns length of list", "Returns number of methods in a class", "Returns length of a string", "Both A and C", "Both A and C"),
    ("Which keyword is used to define an anonymous function?", "lambda", "function", "def", "anonymous", "lambda"),
    ("What type of loop runs indefinitely if no break condition is specified?", "while", "for", "do-while", "if-else", "while")
]
    # Add more questions as needed...


# Questions for DS3860: Database Management
ds3860_questions = [
    ("Which SQL statement is used to retrieve data?", "SELECT", "FETCH", "GET", "SHOW", "SELECT"),
    ("What does SQL stand for?", "Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language", "Structured Query Language"),
    ("What is the correct file extension for Python files?", ".py", ".pyt", ".python", ".pt", ".py"),
    ("Which of these is a correct way to create a function in Python?", "def myFunction()", "create function myFunction()", "func myFunction()", "define myFunction()", "def myFunction()"),
    ("Which operator is used for exponentiation in Python?", "^", "**", "//", "*", "**"),
    ("How do you insert comments in Python?", "// this is a comment", "# this is a comment", "/* this is a comment */", "<!-- this is a comment -->", "# this is a comment"),
    ("What data type is the result of '5 / 2' in Python 3?", "Integer", "Float", "String", "Complex", "Float"),
    ("Which method is used to add an item to the end of a list?", "append()", "insert()", "add()", "push()", "append()"),
    ("What keyword is used to create a class in Python?", "class", "define", "object", "structure", "class"),
    ("What does the 'len()' function do?", "Returns length of list", "Returns number of methods in a class", "Returns length of a string", "Both A and C", "Both A and C"),
    ("Which keyword is used to define an anonymous function?", "lambda", "function", "def", "anonymous", "lambda"),
    ("What type of loop runs indefinitely if no break condition is specified?", "while", "for", "do-while", "if-else", "while")
]
    # Add more questions as needed...


# Questions for DS3620: Business Analytics
ds3620_questions = [
    ("Which of these is a data visualization tool?", "PowerPoint", "Excel", "Power BI", "Word", "Power BI"),
    ("What is the main purpose of business analytics?", "Create advertisements", "Analyze data for insights", "Manage employees", "Develop software", "Analyze data for insights"),
    ("Which of these is a data visualization tool?", "PowerPoint", "Excel", "Power BI", "Word", "Power BI"),
    ("What is the main purpose of business analytics?", "Create advertisements", "Analyze data for insights", "Manage employees", "Develop software", "Analyze data for insights"),
    ("Which chart shows the distribution of data?", "Bar chart", "Histogram", "Pie chart", "Line chart", "Histogram"),
    ("What does KPI stand for?", "Key Performance Indicator", "Knowledge Performance Index", "Key Process Indicator", "Known Process Indicator", "Key Performance Indicator"),
    ("Which tool is commonly used for data analysis?", "Photoshop", "Excel", "Illustrator", "Blender", "Excel"),
    ("What type of data is qualitative?", "Continuous data", "Numerical data", "Categorical data", "Integer data", "Categorical data"),
    ("What is a dashboard in analytics?", "A control panel", "A data report summary", "A statistical tool", "A presentation", "A data report summary"),
    ("What is a predictive model?", "Forecasts future events", "Represents past data", "Calculates sums", "Generates reports", "Forecasts future events"),
    ("What does ETL stand for?", "Extract, Transform, Load", "Encode, Translate, Log", "Examine, Test, Log", "Enter, Track, Learn", "Extract, Transform, Load"),
    ("What is regression used for in analytics?", "Summarizing data", "Predicting relationships", "Classifying data", "Transforming data", "Predicting relationships")
    # Add more questions as needed...
]

# Questions for DS4125: Computer Forensics
ds4125_questions = [
    ("Which of these is a task in computer forensics?", "Analyzing digital evidence", "Writing software", "Managing servers", "Networking", "Analyzing digital evidence"),
    ("What does 'chain of custody' refer to?", "Securing network connections", "Tracking evidence handling", "Creating new evidence", "Encrypting data", "Tracking evidence handling"),
    ("Which of these is a task in computer forensics?", "Analyzing digital evidence", "Writing software", "Managing servers", "Networking", "Analyzing digital evidence"),
    ("What does 'chain of custody' refer to?", "Securing network connections", "Tracking evidence handling", "Creating new evidence", "Encrypting data", "Tracking evidence handling"),
    ("What is a forensic image?", "An exact copy of digital data", "A blurred image", "Encrypted data", "Network data", "An exact copy of digital data"),
    ("What is the role of a hash function in forensics?", "Encrypt data", "Identify duplicates", "Verify integrity", "Compress data", "Verify integrity"),
    ("Which organization offers certifications for forensics?", "CompTIA", "ISACA", "EC-Council", "All of the above", "All of the above"),
    ("What is metadata?", "Data about data", "Encrypted data", "Deleted data", "Hidden data", "Data about data"),
    ("What does 'write blocker' do?", "Prevents data modification", "Encrypts data", "Deletes data", "Copies data", "Prevents data modification"),
    ("What is the first step in forensic investigation?", "Data acquisition", "Data deletion", "Reporting", "Data analysis", "Data acquisition"),
    ("What does RAM stand for?", "Random Access Memory", "Read Access Memory", "Recent Access Memory", "Real Access Memory", "Random Access Memory"),
    ("What is 'steganography'?", "Hiding information in files", "Encrypting files", "Deleting files", "Copying files", "Hiding information in files")
    # Add more questions as needed...
]

# Questions for BIOL3920: Biological Communication
biol3920_questions = [
    ("What is science communication?", "Sharing science with the public", "Classifying species", "Publishing in journals", "Researching cells", "Sharing science with the public"),
    ("What is peer review?", "Evaluating scientific work", "Marketing research", "Studying animals", "Public speaking", "Evaluating scientific work"),
    ("What is science communication?", "Sharing science with the public", "Classifying species", "Publishing in journals", "Researching cells", "Sharing science with the public"),
    ("What is peer review?", "Evaluating scientific work", "Marketing research", "Studying animals", "Public speaking", "Evaluating scientific work"),
    ("Which of these is a scientific journal?", "Nature", "Forbes", "National Geographic", "People", "Nature"),
    ("What is the impact factor of a journal?", "Measure of importance", "Printing frequency", "Number of pages", "Cost of subscription", "Measure of importance"),
    ("What is an abstract in scientific papers?", "Summary of research", "Table of contents", "List of authors", "Literature review", "Summary of research"),
    ("Why is citation important in science?", "Credit original work", "Shows reading level", "Increases paper length", "Awards points", "Credit original work"),
    ("Which of these is a type of scientific paper?", "Review article", "Fantasy novel", "Cookbook", "Biography", "Review article"),
    ("What is a hypothesis?", "Testable prediction", "Result", "Discussion", "Observation", "Testable prediction"),
    ("What does DOI stand for?", "Digital Object Identifier", "Document Online Information", "Digital Online Image", "Data Organization Index", "Digital Object Identifier"),
    ("What is open-access publishing?", "Free access to research", "Paid research papers", "Secret documents", "Government documents", "Free access to research")
]
    # Add more questions as needed...


# Adding questions to each table
for question in ds3850_questions:
    add_question("DS3850", *question)

for question in ds3860_questions:
    add_question("DS3860", *question)

for question in ds3620_questions:
    add_question("DS3620", *question)

for question in ds4125_questions:
    add_question("DS4125", *question)

for question in biol3920_questions:
    add_question("BIOL3920", *question)

print("Questions have been inserted into the database.")

# Close the connection
conn.close()
