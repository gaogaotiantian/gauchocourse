QUnit.test( "hello test", function( assert ) {
	assert.ok( 1 == "1", "Passed!" );
    });

var addedCourses = [] //list of all inputed courses as a object of course and semester

var schedule = [] //sorted schedule, index represent the semester. ex: schedule[0] is the array of all input courses in freshman summer quarter

var totalUnit = 0 // totoal units of the current courses add up

var quarterUnit = [] // unit for each quarter, ex: quarterUnit[0] represent the unit of the freshman summer quarter

var apData = []

var courseData = []

var validCourses = []
    
var invalidData = []

courseData  =[
{
    label : "CMPSC 8 Introduction to Computer Science",
    id : "0",
    sub: "CMPSC",
    number : "8",
    prereq : [[{id : "2", concur : "y"}]],
    units : "4",
    gearea :["D", "WOR", "WRT"],
    semester : ["spring", "summer", "fall", "winter"],
    //gearea :["D", "EUR", "WRT"]
},

{
	label :"CMPSC 16 Problem Solving with Computers I",
	id : "1",
	sub : "CMPSC",
	number : "16",
	units : "4",
	prereq : [[{id : "2",  concur : "y"}, {id: "3",  concur : "y"}],
	  		  [{id :"0", concur :"n"}]],
	gearea :["E", "QUR", "WRT"],
	semester : ["spring", "summer", "fall", "winter"],

},

{
	label :"Math 3A, Introduction to Calclus",
	id: "2",
	sub : "MATH",
	number : "3A",
	units : "4",
	prereq : [],
	gearea :["F", "EUR", "WRT"],
	semester : ["spring", "summer", "fall", "winter"],
	

},

{
	label :"MATH 34A, CALC FOR SOCIAL SCI",
	id : "3",
	sub : "MATH",
	number : "34A",
	units : "4",
	prereq : [],
	gearea :["G", "EUR", "WRT"],
	semester : ["spring", "summer", "fall", "winter"],
	

},

{
    label :"Writing 2, intro to College Writing",
    id : "4",
    sub : "WRIT",
    number : "2",
    units : "4",
    prereq : [],
    gearea :["A","WRT"],
    semester : ["spring", "summer", "fall", "winter"]
    

},

{
    label :"History 2A, World History",
    id : "5",
    sub : "HIST",
    number : "2A",
    units : "4",
    prereq : [],
    gearea :["E","WRT","EUR"],
    semester : ["spring", "summer", "fall", "winter"]
},

{
    label :"History 2B, World History",
    id : "6",
    sub : "HIST",
    number : "2B",
    units : "4",
    prereq : [],
    gearea :["E","WRT","EUR"],
    semester : ["spring", "summer", "fall", "winter"]
},

{
    label :"History 2C, World History",
    id : "7",
    sub : "HIST",
    number : "4C",
    units : "4",
    prereq : [],
    gearea :["E","WRT","EUR"],
    semester : ["spring", "summer", "fall", "winter"]
},

{
    label :"History 200B, Post World History",
    id : "8",
    sub : "HIST",
    number : "200B",
    units : "4",
    prereq : [],
    gearea :["E","WRT","EUR"],
    semester : ["spring", "summer", "fall", "winter"]
},

{
    label :"Philophy 173, World History",
    id : "9",
    sub : "PHIL",
    number : "173",
    units : "4",
    prereq : [],
    gearea :["D","WRT"],
    semester : ["spring", "summer", "fall", "winter"]
},
]



QUnit.module("Is Valid", {
	beforeEach: function(){
	    var CS8={
		"label":"CMPSC 8 Introduction to Computer Science",
		"id":"0",
		"sub":"CMPSC",
		"number":"8",
		"units":"4",
		"prereq":[],
		"semester":{"spring":"y", "summer":"y", "fall":"y", "winter":"y"}
	    }
	    validCourses.push(CS8);
	},
	afterEach: function(){
	    validCourses = [];
	}
    });
QUnit.test("empty string", function(){
	equal(IsValid(""), true, "empty string");
    });
QUnit.test("sth is good", function(){
	equal(IsValid("CMPSC 8 Introduction to Computer Science"), true, "CS8 is good");
    });
QUnit.test("sth is not good", function(){
	equal(IsValid("CMPSC 16 Problem Solving wid Computerrs I"), false, "CS16 is good");
    });



QUnit.module("Add All Courses", {
	afterEach: function(){
	    addedCourses = [];
	}
    });
QUnit.test("zero input", function(){
	deepEqual(addedCourses, [], "zero input is fine");	
    });
QUnit.test("input something that's good", function(){
	QUnit.dump.maxDepth = 100;
var inputCourses = [
                    {course : "CMPSC 8 Introduction to Computer Science", semester : "freshman_fall"},
                    {course : "Philophy 173, World History", semester : "freshman_fall"}
] //input courses name with semester that should be provied for the function, this is just a example


    var expectedAddedCourses = [
				{course:
				 {
				     label : "CMPSC 8 Introduction to Computer Science",
				     id : "0",
				     sub: "CMPSC",
				     number : "8",
				     prereq : [[{id : "2", concur : "y"}]],
				     units : "4",
				     gearea :["D", "WOR", "WRT"],
				     semester : ["spring", "summer", "fall", "winter"],
				     //gearea :["D", "EUR", "WRT"]
				 }, 
				 semester: 1
				},
				
				{course:
				 {
				     label :"Philophy 173, World History",
				     id : "9",
				     sub : "PHIL",
				     number : "173",
				     units : "4",
				     prereq : [],
				     gearea :["D","WRT"],
				     semester : ["spring", "summer", "fall", "winter"]
				 },
				 semester: 1
				},
				];

AddAllCourses(inputCourses);
deepEqual(addedCourses, expectedAddedCourses, "CS8 and Phil173 are good");
    });




QUnit.module("Sort All Courses By Semester", {
	afterEach: function(){
	    addedCourses = [];
	    schedule = [];
	}
    });
QUnit.test("empty schedule", function(){
	deepEqual(schedule, [], "empty schedule is good");
    });
QUnit.test("data sorted", function(){
	var inputCourses = [
			    {course : "CMPSC 8 Introduction to Computer Science", semester : "freshman_fall"},
			    {course : "CMPSC 16 Problem Solving with Computers I", semester : "freshman_winter"},
			    {course : "Math 3A, Introduction to Calclus", semester : "freshman_summer"},
			    {course : "MATH 34A, CALC FOR SOCIAL SCI", semester : "freshman_summer"},
			    {course : "Writing 2, intro to College Writing", semester : "freshman_summer"},
			    {course : "History 2A, World History",semester :"freshman_winter"},
			    {course : "History 2B, World History",semester :"freshman_spring"},
			    {course : "History 2C, World History",semester :"freshman_summer"},
			    {course : "History 200B, Post World History", semester :"freshman_winter"},
			    {course : "Philophy 173, World History", semester : "freshman_fall"}
			    ] //input courses name with semester that should be provied for the function, this is just a example 
	    AddAllCourses(inputCourses);	
	SortAllCourseBySemester();
	var expectedSchedule = 
	    deepEqual(schedule, [], "all course data is sorted (intentionally fail to check the format of the schedule");
    });




QUnit.module("get course by name");
QUnit.test("empty name", function(){
	equal(GetCourseByName(""), undefined, "get nothing");
    });
QUnit.test("get a name that's not there", function(){
	equal(GetCourseByName("haha"), undefined, "get nothing");
    });
QUnit.test("get a correct name", function(){
	var CS8 = {
	    label : "CMPSC 8 Introduction to Computer Science",
	    id : "0",
	    sub: "CMPSC",
	    number : "8",
	    prereq : [[{id : "2", concur : "y"}]],
	    units : "4",
	    gearea :["D", "WOR", "WRT"],
	    semester : ["spring", "summer", "fall", "winter"],
	    //gearea :["D", "EUR", "WRT"]
	};
	deepEqual(GetCourseByName("CMPSC 8 Introduction to Computer Science"), CS8, "CS8 get!");
    });




QUnit.module("check this course", {
    afterEach: function(){
	validCourses = [];
	invalidData = [];
    }
    });
QUnit.test("valid course invalid semester", function(){
	var CS8 = {
	    label : "CMPSC 8 Introduction to Computer Science",
	    id : "0",
	    sub: "CMPSC",
	    number : "8",
	    prereq : [],
	    units : "4",
	    gearea :["D", "WOR", "WRT"],
	    semester : ["winter"],
	    //gearea :["D", "EUR", "WRT"]
	};
	var result = [
		      {
			  "message": "course not offer in this quarter",
			  "name": "CMPSC 16 Problem Solving with Computers I",
			  "semester": undefined
		      }
		      ];
	CheckThisCourse(CS8, "senior_fall");

	deepEqual(invalidData, [CS8], "CS8 is not valid in senior spring");
    });
QUnit.test("valid course invalid prerequisite", function(){
	var CS16 = {
	    label :"CMPSC 16 Problem Solving with Computers I",
	    id : "1",
	    sub : "CMPSC",
	    number : "16",
	    units : "4",
	    prereq : [[{id : "2",  concur : "y"}, {id: "3",  concur : "y"}],
		      [{id :"0", concur :"n"}]],
	    gearea :["E", "QUR", "WRT"],
	    semester : ["spring", "summer", "fall", "winter"],
	};
	var resultForCS16 = [
		      {
			  "message": "course's prerequisites are not fulfilled",
			  "name": "CMPSC 16 Problem Solving with Computers I",
			  "semester": undefined
		      }
		      ];
	CheckThisCourse(CS16, "senior_fall");
	deepEqual(invalidData, resultForCS16, "pre-req of CS16 is not fulfilled");
    });