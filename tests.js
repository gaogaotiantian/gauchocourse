QUnit.test( "hello test", function( assert ) {
	assert.ok( 1 == "1", "Passed!" );
    });

var addedCourses = []; //list of all inputed courses as a object of course and semester

var schedule = []; //sorted schedule, index represent the semester. ex: schedule[0] is the array of all input courses in freshman summer quarter

var totalUnit = 0; // totoal units of the current courses add up

    var quarterUnit = []; // unit for each quarter, ex: quarterUnit[0] represent the unit of the freshman summer quarter

    var apData = [];

    var courseData = [];
  
    var invalidData = [];

    var validCourses = [];

var user = {
    major : "CMPSC",
    majorType : "LSBS"
}

    var geFullFillment

var geStatus =new Array() 
    geStatus["A"] = 0,
    geStatus["B"] = 0,
    geStatus["C"] = 0,
    geStatus["D"] = 0,
    geStatus["E"] = 0,
    geStatus["F"] = 0,
    geStatus["G"] = 0,
    geStatus["H"] = 0,
    
    geStatus["EUR"] = 0,
    geStatus["WRT"] = 0,
    geStatus["WOR"] = 0,
    geStatus["ETH"] = 0,
    geStatus["DEP"] = 0,
    geStatus["QUR"] = 0

var inputCourses = [
		    {course : "HIST 115R Undergraduate Research Seminar in Medieval European History", semester : "senior_winter"},
		    {course : "PHIL 124B Philosophy of Physics", semester : "freshman_summer"},
		    //		    {course : "CMPSCCS 1B Computer Programming and Organization II", semester : "freshman_fall"},
		    {course : "PSY 3 The Biological Basis of Psychology", semester : "freshman_spring"},
		    {course : "PSY 1 Introduction to Psychology | Area D", semester : "junior_fall"},
		    {course : "HIST 17A The American People | Area D, WRT", semester : "sophomore_fall"}
		    ]; //test cases example; add whatever you want

var count = 0;



QUnit.module("Validate All Input", {
	beforeEach: function(){
	    ValidateAllInput(inputCourses);
	},
	afterEach: function(){
	    count = 0;
	}
    });

QUnit.test("check addedCourses", function(){
	for(var c of addedCourses){
	    equal(c.course.label, inputCourses[count].course, "added courses are as expected");
	    count ++;
	}
    });

QUnit.test("check schedule", function(){
	while(count < inputCourses.length){
	    for(var course of schedule[SemToNum(inputCourses[count].semester)]){
		equal(inputCourses[count].course, course.label, "schedule is as expected");
	    }		      
	    count ++;
	}
    });

QUnit.test("check total unit", function(){
	var expectedTotalUnit = 0;
	while(count < inputCourses.length){
	    expectedTotalUnit += parseInt(GetCourseByName(inputCourses[count].course).units);
	    count ++;
	}
	equal(totalUnit, expectedTotalUnit, "total unit is as expected");
    });

/*
QUnit.test("check quarter unit", function(){
	
    });
*/


//following functions need further improvements
/*
QUnit.test("check invalid data", function(){
	deepEqual(invalidData, [], "invalid data is as expected");
    });
QUnit. test("check valid courses", function(){
	deepEqual(validCourses, [], "valid courses are as expected");
    });





QUnit.module("Is Valid", {
	beforeEach: function(){
	    var hist17A = {
		"sub":"HIST",
		"majorlimit":[],
		"prereq":[],
		"levellimit":"",
		"number":"17A",
		"semester":[
			    "summer",
			    "fall"
			    ],
		"gearea":[
			  "D",
			  "WRT"
			  ],
		"units":"4",
		"label":"HIST 17A The American People | Area D, WRT",
		"id":"1564"
	    }
	    ValidateAllInput(inputCourses);
	}
    });
QUnit.test("empty string", function(){
	equal(IsValid(""), true, "empty string");
    });
QUnit.test("sth is good", function(){
	equal(IsValid("HIST 17A The American People | Area D, WRT"), true, "Hist17A is good");
    });
QUnit.test("sth is not good", function(){
	equal(IsValid("HIST 18A The American People | Area D, WRT"), false, "hist18A not good");
    });
*/




