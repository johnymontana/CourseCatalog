import requests
from pprint import pprint
from faker import Faker
from pymongo import MongoClient
import uuid
import random


# constants for Coursera API
BASE_URL = "https://api.coursera.org/api/catalog.v1/courses"
FIELDS = 'shortName, name,language,largeIcon,photo,previewLink,shortDescription,smallIcon,subtitleLanguagesCsv,isTranslate,universityLogo,video,videoId,aboutTheCourse,targetAudience,faq,courseSyllabus,courseFormat,suggestedReadings,instructor,estimatedClassWorkload,aboutTheInstructor,sessions.fields(durationString,name,eligibleForCertificates,startDay,startMonth,startYear,active,status),instructors.fields(photo,bio,fullName,title,department,website,websiteTwitter),universities.fields(description,homeLink,location,website,websiteTwitter,logo),categories.fields(name,shortName,description)'
INCLUDES = 'universities,categories,instructors,sessions'
Q = 'search'
QUERY = 'computer science'

# MongoClient
db = MongoClient('mongodb://localhost:27017')['coursera']
db.drop_collection('course')
db.drop_collection('category')
db.drop_collection('session')
db.drop_collection('instructor')
db.drop_collection('university')
db.drop_collection('student')
db.drop_collection('course_taken')

fake = Faker()

def fetch_courses():

	params = {
		'fields': FIELDS,
		'includes': INCLUDES,
		#'q': Q,
		#'query': QUERY
	}

	r = requests.get(BASE_URL, params=params)
	print(r.url)

	data = r.json()

	courses = filter_english_courses(data['elements'])
	universities = data['linked']['universities']
	categories = data['linked']['categories']
	instructors = data['linked']['instructors']
	sessions = data['linked']['sessions']

	print("Fetched: ")
	print(str(len(courses)) + " courses")
	print(str(len(universities)) + " universities")
	print(str(len(categories)) + " categories")
	print(str(len(instructors)) + " instructors")
	#print(str(len(sessions)) + " sessions")

	for c in categories:
		c['_id'] = "category" + str(c['id'])
		#c['category_id'] = "category" + str(c['id'])

	for u in universities:
		u['_id'] = "university" + str(u['id'])
		#u['university_id'] = "university" + str(u['id'])

	for i in instructors:
		i['_id'] = "instructor" + str(i['id'])
		#i['instructor_id'] = "instructor" + str(i['id'])

	insert_mongo(categories, "category")
	insert_mongo(universities, "university")
	insert_mongo(instructors, "instructor")

	for c in categories:
		#c['_id'] = "category" + str(c['id'])
		c['category_id'] = "category" + str(c['id'])
		c.pop('_id', None)

	for u in universities:
		#u['_id'] = "university" + str(u['id'])
		u['university_id'] = "university" + str(u['id'])
		u.pop('_id', None)

	for i in instructors:
		#i['_id'] = "instructor" + str(i['id'])
		i['instructor_id'] = "instructor" + str(i['id'])
		i.pop('_id', None)

	for course in courses:
		new_categories = []
		new_universities = []
		new_instructors = []
		
		if 'categories' in course['links'].keys():
			for category_id in course['links']['categories']:
				category = find_by_id(categories, category_id)
				#category.pop('_id', None)
				new_categories.append(category)

		if 'universities' in course['links'].keys():
			for university_id in course['links']['universities']:
				univ = find_by_id(universities, university_id)
				#univ.pop('_id', None)
				new_universities.append(univ)

		if 'instructors' in course['links'].keys():
			for instructor_id in course['links']['instructors']:
				instructor = find_by_id(instructors, instructor_id)
				#instructor.pop('_id', None)
				new_instructors.append(instructor)


		course['categories'] = new_categories
		course['universities'] = new_universities
		course['instructors'] = new_instructors
		course.pop('links', None)

	return courses, categories, universities, instructors

def find_by_id(l, id):
	for el in l:
		if el['id'] == id:
			return el

def find_random_course_id():
	course = db.course.find().limit(1).skip( int(random.random() * db.course.count()) )[0]
	return course['_id']

def filter_english_courses(ls):
	c = []
	for l in ls:
		if l.get('language', None) == 'en':
			c.append(l)
	return c

def new_student():
	student = {}
	student['_id'] = str(uuid.uuid1())
	student['name'] = fake.name()
	student['address'] = fake.address()
	student['bio'] = fake.text()
	student['company'] = fake.company()
	student['job'] = fake.job()
	student['phone'] = fake.phone_number()
	return student

def generate_fake_students(num=500, d=17):
	students = []
	student_sessions = []

	print("Inserting " + str(num) + " students with up to " + str(d) + " courses taken per student.")
	for i in range(num):
		students.append(new_student())
	for s in students:
		for e in range(int(random.random() * d)):
			session = {}
			session['student_id'] = s['_id']
			session['course_id'] = find_random_course_id()
			session['date_completed'] = fake.date_time()
			session['grade'] = fake.word()
			student_sessions.append(session)
	return students, student_sessions

def insert_mongo(docs, collection_name):
	collection = db[collection_name]
	collection.insert_many(docs)

if __name__ == "__main__":
	courses, categories, universities, instructors = fetch_courses()
	insert_mongo(courses, "course")
	

	students, courses_taken = generate_fake_students()
	insert_mongo(students, "student")
	insert_mongo(courses_taken, "course_taken")











