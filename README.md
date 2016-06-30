## CourseCatalog

A simple python script to save sample course catalog data to MongoDB.

The script pulls data from the public [Coursera API](https://building.coursera.org/app-platform/catalog/) and uses the Python [faker](https://github.com/joke2k/faker) library to generate fake student profile information, courses taken, and grades.


### MongoDB Schema

The script creates several MongoDB collections, such as `course`, `student`, and `course_taken`. 

#### `course` collection

Documents in the `course` collection represent an individual course being offered.

Example:

~~~
{
	"_id" : ObjectId("577483b14c3b8252e9902a91"),
	"faq" : "",
	"categories" : [
		{
			"id" : 4,
			"description" : "Our wide range of courses allows students to explore topics from many different fields of study. Sign up for a class today and join our global community of students and scholars!",
			"category_id" : "category4",
			"name" : "Information, Tech & Design",
			"shortName" : "infotech"
		},
		{
			"id" : 15,
			"description" : "Our wide range of courses allows students to explore topics from many different fields of study. Sign up for a class today and join our global community of students and scholars!",
			"category_id" : "category15",
			"name" : "Engineering",
			"shortName" : "ee"
		}
	],
	"instructors" : [ ],
	"videoId" : "",
	"isTranslate" : false,
	"targetAudience" : 0,
	"largeIcon" : "https://d15cw65ipctsrr.cloudfront.net/a1/8ba870f35d11e4a662cf761ac1ff65/Designing-Technology-for-Learning-Icon600x340.jpg",
	"subtitleLanguagesCsv" : "",
	"language" : "en",
	"aboutTheCourse" : "This course is currently under development and is expected to be offered October 2015.",
	"universityLogo" : "",
	"courseFormat" : "",
	"universities" : [
		{
			"website" : "http://www.gatech.edu/",
			"id" : 9,
			"description" : "The Georgia Institute of Technology is one of the nation's top research universities, distinguished by its commitment to improving the human condition through advanced science and technology.\n\nGeorgia Tech's campus occupies 400 acres in the heart of the city of Atlanta, where more than 20,000 undergraduate and graduate students receive a focused, technologically based education.",
			"logo" : "https://coursera-university-assets.s3.amazonaws.com/30/4b35cef753fcd6f13494279b65dc84/Georgia-Tech.png",
			"location" : "Georgia Institute of Technology, Atlanta, GA",
			"university_id" : "university9",
			"websiteTwitter" : "georgiatech",
			"shortName" : "gatech"
		}
	],
	"shortName" : "designtech4learning",
	"estimatedClassWorkload" : "4-7 hours/week",
	"video" : "",
	"id" : 2377,
	"shortDescription" : "Designing technologies that facilitate learning. Beyond usability, technology for learning has to engage, trigger prior knowledge, prompt for reflection, maintain a balance between too much cognitive load and too little challenge, and scaffold the development of skills.\n\n",
	"suggestedReadings" : "",
	"courseSyllabus" : "Designing technologies that facilitate learning. Beyond usability, technology for learning has to engage, trigger prior knowledge, prompt for reflection, maintain a balance between too much cognitive load and too little challenge, and scaffold the development of skills.<br><ul>\n<li><strong>Week 1</strong>: How People Learn</li>\n</ul>\n<ul>\n<ul>\n<li>How memory works and how learning works</li>\n<li>Differences between experts and novices.</li>\n<li>Scaffolding learning.</li>\n</ul>\n</ul>\n<ul>\n<li><strong>Week 2</strong>: Designing for Learning</li>\n</ul>\n<ul>\n<ul>\n<li>Know thy students</li>\n<li>Identifying learning objectives</li>\n<li>Creating learning activities</li>\n</ul>\n</ul>\n<ul>\n<li><strong>Week 3</strong>: Examples</li>\n</ul>\n<ul>\n<ul>\n<li>Science education</li>\n<li>Computer science education</li>\n<li>Mathematics education</li>\n</ul>\n</ul>\n<ul>\n<li><strong>Week 4</strong>: Evaluation</li>\n</ul>\n<ul>\n<ul>\n<li>How do you know if you got there? Testing your design decisions.</li>\n<li>Factors to measure: retention, completion, learning, attitudes.</li>\n<li>What makes a good evaluation? Validation and reliability</li>\n</ul>\n</ul>",
	"photo" : "https://d15cw65ipctsrr.cloudfront.net/9e/76c750f35d11e48234f783515c7395/Designing-Technology-for-Learning-Icon600x340.jpg",
	"smallIcon" : "https://d15cw65ipctsrr.cloudfront.net/a1/a76dd0f35d11e4a0f02b5e65ee01a5/Designing-Technology-for-Learning-Icon600x340.jpg",
	"name" : "Designing Technology for Learning"
}
~~~

#### `student` collection

Documents in this collection represent an individual student. Note that all information is randomly generated.

Example:

~~~
{
	"_id" : "44521640-3e6a-11e6-8fbe-acbc327f8c19",
	"phone" : "(981)155-1619x24427",
	"bio" : "Alias architecto cum assumenda quisquam quidem. Consectetur explicabo nihil libero unde. Magni omnis provident repellat quidem omnis ab. Veniam expedita ipsa fugit beatae eveniet voluptatum.",
	"company" : "Jaskolski Inc",
	"address" : "5286 Nolan Valleys Apt. 660\nWest Stacy, CT 18301-6577",
	"name" : "Mr. Eric Rohan II",
	"job" : "Financial trader"
}
~~~

#### `course_taken` collection

Documents in this collection correspond to a single session of a course taken by a student. This includes the date the course was taken and the grade the student received.

Example:

~~~
{
	"_id" : ObjectId("577483b54c3b8252e9902ba3"),
	"student_id" : "44521640-3e6a-11e6-8fbe-acbc327f8c19",
	"grade" : "praesentium",
	"course_id" : ObjectId("577483b14c3b8252e9902a93"),
	"date_completed" : ISODate("1984-03-16T17:09:50Z")
}
~~~

## Note

All data from the Coursera API is owned by the original copyright holders.
