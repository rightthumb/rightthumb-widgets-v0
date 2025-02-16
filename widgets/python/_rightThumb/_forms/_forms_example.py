# from _rightThumb._forms._forms_example import example_forms1, example_forms2, checkboxes
# results = _.Form(form)
example_forms1 = [
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Event Registration Form with Example Values": [
			{"label": "Event Name", "type": "text", "value": "Annual Conference"},
			{"label": "First Name", "type": "text", "value": "Alice"},
			{"label": "Last Name", "type": "text", "value": "Johnson"},
			{"label": "Email", "type": "text", "value": "alice.johnson@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-5678"}
		],
		"Attendance Preferences Form with Example Values": [
			{"label": "Attendance Mode", "type": "radio", "options": ["In-person", "Virtual"], "value": "In-person"},
			{"label": "Venue", "type": "checkbox", "options": ["Convention Center", "Grand Ballroom"], "value": "Convention Center"},
			{"label": "Meal Preference", "type": "dropdown", "options": ["Vegetarian", "Non-Vegetarian", "Vegan"], "value": "Vegetarian"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Personal Information Form with Example Values": [
			{"label": "First Name", "type": "text", "value": "John"},
			{"label": "Last Name", "type": "text", "value": "Doe"},
			{"label": "Email", "type": "text", "value": "john.doe@example.com"},
			{"label": "Password", "type": "password", "value": "password123"},
			{"label": "Gender", "type": "radio", "options": ["Male", "Female", "Other"], "value": "Male"}
		],
		"Address Form with Example Values": [
			{"label": "Street", "type": "text", "value": "123 Main St"},
			{"label": "City", "type": "text", "value": "Anytown"},
			{"label": "State", "type": "text", "value": "CA"},
			{"label": "Zip Code", "type": "text", "value": "90210"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Job Application Form with Example Values": [
			{"label": "Position Applied For", "type": "text", "value": "Software Engineer"},
			{"label": "First Name", "type": "text", "value": "Jane"},
			{"label": "Last Name", "type": "text", "value": "Smith"},
			{"label": "Email", "type": "text", "value": "jane.smith@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-1234"}
		],
		"Work Experience Form with Example Values": [
			{"label": "Company", "type": "text", "value": "Tech Corp"},
			{"label": "Position", "type": "text", "value": "Developer"},
			{"label": "Start Date", "type": "text", "value": "01/01/2020"},
			{"label": "End Date", "type": "text", "value": "Present"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Survey Form with Example Values": [
			{"label": "Age Group", "type": "dropdown", "options": ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], "value": "26-35"},
			{"label": "Favorite Color", "type": "text", "value": "Blue"},
			{"label": "Feedback", "type": "text_area", "value": "Great service!"}
		],
		"Rating Form with Example Values": [
			{"label": "Satisfaction Level", "type": "radio", "options": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], "value": "Satisfied"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Product Order Form with Example Values": [
			{"label": "Product Name", "type": "text", "value": "Widget"},
			{"label": "Quantity", "type": "text", "value": "10"},
			{"label": "Price per Unit", "type": "text", "value": "9.99"}
		],
		"Shipping Information Form with Example Values": [
			{"label": "Recipient Name", "type": "text", "value": "Bob Brown"},
			{"label": "Street Address", "type": "text", "value": "456 Elm St"},
			{"label": "City", "type": "text", "value": "Othertown"},
			{"label": "State", "type": "text", "value": "TX"},
			{"label": "Zip Code", "type": "text", "value": "75001"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Contact Us Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Charlie Davis"},
			{"label": "Email", "type": "text", "value": "charlie.davis@example.com"},
			{"label": "Subject", "type": "text", "value": "Inquiry"},
			{"label": "Message", "type": "text_area", "value": "I would like more information about your services."}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Feedback Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Daniel Evans"},
			{"label": "Email", "type": "text", "value": "daniel.evans@example.com"},
			{"label": "Comments", "type": "text_area", "value": "I really enjoyed using your product."},
			{"label": "Rating", "type": "radio", "options": ["1", "2", "3", "4", "5"], "value": "5"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Newsletter Signup Form with Example Values": [
			{"label": "First Name", "type": "text", "value": "Emily"},
			{"label": "Last Name", "type": "text", "value": "Foster"},
			{"label": "Email", "type": "text", "value": "emily.foster@example.com"},
			{"label": "Preferences", "type": "checkbox", "options": ["Daily Updates", "Weekly Summary", "Monthly Newsletter"], "value": "Weekly Summary"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Customer Support Ticket Form with Example Values": [
			{"label": "Name", "type": "text", "value": "George Harris"},
			{"label": "Email", "type": "text", "value": "george.harris@example.com"},
			{"label": "Issue Type", "type": "dropdown", "options": ["Technical", "Billing", "General"], "value": "Technical"},
			{"label": "Description", "type": "text_area", "value": "I am experiencing a technical issue with your software."}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Reservation Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Helen Johnson"},
			{"label": "Email", "type": "text", "value": "helen.johnson@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-7890"},
			{"label": "Reservation Date", "type": "text", "value": "2024-12-25"},
			{"label": "Number of Guests", "type": "text", "value": "4"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Conference Registration Form with Example Values": [
			{"label": "Conference Name", "type": "text", "value": "Tech Innovators Conference"},
			{"label": "First Name", "type": "text", "value": "Ian Kelly"},
			{"label": "Last Name", "type": "text", "value": "Kelly"},
			{"label": "Email", "type": "text", "value": "ian.kelly@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-1234"},
			{"label": "Job Title", "type": "text", "value": "CTO"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Loan Application Form with Example Values": [
			{"label": "Applicant Name", "type": "text", "value": "Jack Lee"},
			{"label": "Email", "type": "text", "value": "jack.lee@example.com"},
			{"label": "Loan Amount", "type": "text", "value": "100000"},
			{"label": "Loan Purpose", "type": "text", "value": "Home Renovation"},
			{"label": "Annual Income", "type": "text", "value": "75000"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Membership Application Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Karen Martinez"},
			{"label": "Email", "type": "text", "value": "karen.martinez@example.com"},
			{"label": "Membership Type", "type": "dropdown", "options": ["Basic", "Premium", "VIP"], "value": "Premium"},
			{"label": "Payment Method", "type": "dropdown", "options": ["Credit Card", "PayPal", "Bank Transfer"], "value": "Credit Card"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Appointment Booking Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Larry Nelson"},
			{"label": "Email", "type": "text", "value": "larry.nelson@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-3456"},
			{"label": "Preferred Date", "type": "text", "value": "2024-07-30"},
			{"label": "Preferred Time", "type": "text", "value": "10:00 AM"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Volunteer Signup Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Maria O'Connor"},
			{"label": "Email", "type": "text", "value": "maria.oconnor@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-6789"},
			{"label": "Availability", "type": "text_area", "value": "Weekends and evenings"},
			{"label": "Skills", "type": "text_area", "value": "Event planning, fundraising"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Travel Booking Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Nathan Parker"},
			{"label": "Email", "type": "text", "value": "nathan.parker@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-4321"},
			{"label": "Destination", "type": "text", "value": "Paris, France"},
			{"label": "Travel Dates", "type": "text", "value": "2024-08-01 to 2024-08-15"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Event Feedback Form with Example Values": [
			{"label": "Name", "type": "text", "value": "Olivia Quinn"},
			{"label": "Email", "type": "text", "value": "olivia.quinn@example.com"},
			{"label": "Event Attended", "type": "text", "value": "Annual Tech Summit"},
			{"label": "Feedback", "type": "text_area", "value": "The event was very informative and well-organized."},
			{"label": "Rating", "type": "radio", "options": ["1", "2", "3", "4", "5"], "value": "4"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Class Registration Form with Example Values": [
			{"label": "Class Name", "type": "text", "value": "Introduction to Python"},
			{"label": "Student Name", "type": "text", "value": "Paul Roberts"},
			{"label": "Email", "type": "text", "value": "paul.roberts@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-9876"},
			{"label": "Preferred Time Slot", "type": "dropdown", "options": ["Morning", "Afternoon", "Evening"], "value": "Morning"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Medical History Form with Example Values": [
			{"label": "Patient Name", "type": "text", "value": "Rachel Scott"},
			{"label": "Email", "type": "text", "value": "rachel.scott@example.com"},
			{"label": "Phone Number", "type": "text", "value": "555-6543"},
			{"label": "Date of Birth", "type": "text", "value": "1980-05-15"},
			{"label": "Known Allergies", "type": "text_area", "value": "Peanuts, Penicillin"},
			{"label": "Current Medications", "type": "text_area", "value": "Metformin, Lisinopril"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Research Survey Form with Example Values": [
			{"label": "Participant Name", "type": "text", "value": "Steven Turner"},
			{"label": "Email", "type": "text", "value": "steven.turner@example.com"},
			{"label": "Age Group", "type": "dropdown", "options": ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], "value": "36-45"},
			{"label": "Survey Questions", "type": "text_area", "value": "What is your primary source of news?"},
			{"label": "Additional Comments", "type": "text_area", "value": "I prefer online news sources over print media."}
		]
	}
]
example_forms2 = [
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a JavaScript file."
		},
		"JavaScript File Notes Form": [
			{"label": "File Name", "type": "text", "value": "main.js"},
			{"label": "File Path", "type": "text", "value": "/path/to/main.js"},
			{"label": "Description", "type": "text_area", "value": "This file contains the main logic for the application."},
			{"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Integrated with backend API."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with async function."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a CSS file."
		},
		"CSS File Notes Form": [
			{"label": "File Name", "type": "text", "value": "styles.css"},
			{"label": "File Path", "type": "text", "value": "/path/to/styles.css"},
			{"label": "Description", "type": "text_area", "value": "This file contains the styling for the application."},
			{"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Styled the main layout."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with responsive design."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a PHP file."
		},
		"PHP File Notes Form": [
			{"label": "File Name", "type": "text", "value": "index.php"},
			{"label": "File Path", "type": "text", "value": "/path/to/index.php"},
			{"label": "Description", "type": "text_area", "value": "This file handles the main backend logic for the application."},
			{"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Connected with MySQL database."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed SQL injection vulnerability."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a documentation file."
		},
		"Documentation File Notes Form": [
			{"label": "File Name", "type": "text", "value": "README.md"},
			{"label": "File Path", "type": "text", "value": "/path/to/README.md"},
			{"label": "Description", "type": "text_area", "value": "This file contains the documentation for the project."},
			{"label": "Revision Notes", "type": "text_area", "value": "Updated with installation instructions."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Added API documentation."},
			{"label": "Bug Notes", "type": "text_area", "value": "Corrected typos in usage examples."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a specified URL."
		},
		"URL Notes Form": [
			{"label": "URL", "type": "text", "value": "https://example.com"},
			{"label": "Description", "type": "text_area", "value": "This URL points to the main website of the project."},
			{"label": "Revision Notes", "type": "text_area", "value": "Updated website layout."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Integrated with new API."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed broken links."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a Python file."
		},
		"Python File Notes Form": [
			{"label": "File Name", "type": "text", "value": "script.py"},
			{"label": "File Path", "type": "text", "value": "/path/to/script.py"},
			{"label": "Description", "type": "text_area", "value": "This file contains the main script logic for the application."},
			{"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Integrated with data processing module."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with data parsing."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	},
	{
		"Config": {
			"html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40},
			"description": "Form for taking notes on a SQL file."
		},
		"SQL File Notes Form": [
			{"label": "File Name", "type": "text", "value": "database.sql"},
			{"label": "File Path", "type": "text", "value": "/path/to/database.sql"},
			{"label": "Description", "type": "text_area", "value": "This file contains the SQL script for database setup."},
			{"label": "Revision Notes", "type": "text_area", "value": "Added new tables."},
			{"label": "Implementation Notes", "type": "text_area", "value": "Optimized queries for performance."},
			{"label": "Bug Notes", "type": "text_area", "value": "Fixed syntax errors in SQL script."},
			{"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
			{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
		]
	}
]
checkboxes = {
	"Config": {
		# "html": True,
		"column": {"width": 2},
		"font": {"type": "Arial", "size": 12},
		"color": {"text": "black", "bg": "white"},
		"field": {"width": 40},
		"description": "Form for taking notes on a project with multiple tags using checkboxes."
	},
	"Project Notes Form": [
		{"label": "Project Name", "type": "text", "value": "Example Project"},
		{"label": "Project Path", "type": "text", "value": "/path/to/project"},
		{"label": "Description", "type": "text_area", "value": "This project is an example to demonstrate checkboxes."},
		{"label": "Tags", "type": "checkbox", "options": ["frontend", "backend", "terminal", "api", "database", "development", "production"], "values": ["frontend", "development"]},
		{"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
		{"label": "Implementation Notes", "type": "text_area", "value": "Set up project structure and initial configurations."},
		{"label": "Bug Notes", "type": "text_area", "value": "Fixed initial setup issues."},
		{"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
	]
}