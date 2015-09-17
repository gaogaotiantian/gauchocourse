//This is the test cases for the back-end functions
//and the database.
//To use the test, please provide your user info, input courses, 
//and expected depth-requirement-status accordingly! 
//All other variables are default! DO NOT CHANGE THEM!!


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

//example major
var majorReq = [
    {
        "major" : "CMPSC",

        "getype" : "ENGR",

        "requiredCourses" :[{"sub" : "CMPSC", "number": "16"},
                            {"sub" : "CMPSC", "number": "24"},
                            {"sub" : "CMPSC", "number": "32"},
                            {"sub" : "CMPSC", "number": "40"},
                            {"sub" : "CMPSC", "number": "48"},
                            {"sub" : "CMPSC", "number": "56"},
                            {"sub" : "CMPSC", "number": "64"},
                            {"sub" : "MATH", "number": "3A"},
                            {"sub" : "MATH", "number": "3B"},
                            {"sub" : "MATH", "number": "4A"},
                            {"sub" : "MATH", "number": "4B"},
                            {"sub" : "MATH", "number": "6A"},
                            {"sub" : "PSTAT", "number": "120A"},
                            {"sub" : "CMPSC", "number": "130A"},
                            {"sub" : "CMPSC", "number": "130B"},
                            {"sub" : "CMPSC", "number": "138"},
                            {"sub" : "CMPSC", "number": "154"},
                            {"sub" : "CMPSC", "number": "160"},
                            {"sub" : "CMPSC", "number": "162"},
                            {"sub" : "CMPSC", "number": "170"},
                            {"sub" : "ECE", "number": "152A"},
                            {"sub" : "ENGR", "number": "101"},
                            {"sub" : "PSTAT", "number": "120B"},
                            {"sub" : "PHYS", "number": "1"},
                            {"sub" : "PHYS", "number": "2"},
                            {"sub" : "PHYS", "number": "3"},
                            {"sub" : "PHYS", "number": "3L"}
        ],

        "choiceCourses" : [{"courses" : [{"sub" : "CMPSC", "number": "111"},{"sub" : "CMPSC", "number": "140"},], "units" : "4"},
                           {"courses" : [{"sub" : "CMPSC", "number": "178"},
                                         {"sub" : "CMPSC", "number": "140"},
                                         {"sub" : "CMPSC", "number": "111"},
                                         {"courses" : [{"sub" : "CMPSC", "number": "153A"},{"sub" : "ECE", "number": "153A"}], "units" : "4"},
                                         {"sub" : "CMPSC", "number": "165A"},
                                         {"sub" : "CMPSC", "number": "165B"},
                                         {"sub" : "CMPSC", "number": "167"},
                                         {"courses" : [{"sub" : "CMPSC", "number": "171"},{"sub" : "ECE", "number": "151"}], "units" : "4"},
                                         {"sub" : "CMPSC", "number": "172"},
                                         {"sub" : "CMPSC", "number": "174A"},
                                         {"sub" : "CMPSC", "number": "174B"},
                                         {"sub" : "CMPSC", "number": "176A"},
                                         {"sub" : "CMPSC", "number": "176B"},
                                         {"sub" : "CMPSC", "number": "176C"},
                                         {"sub" : "CMPSC", "number": "177"},
                                         {"sub" : "ECE", "number": "130A"},
                                         {"sub" : "ECE", "number": "130B"},
                                         {"sub" : "ECE", "number": "130C"},
                                         {"sub" : "CMPSC", "number": "180"},
                                         {"courses" : [{"sub" : "CMPSC", "number": "181B"},{"sub" : "ECE", "number": "181B"}], "units" : "4"},
                                         {"courses" : [{"sub" : "CMPSC", "number": "182"},{"sub" : "ECE", "number": "160"}], "units" : "4"},
                                         {"sub" : "CMPSC", "number": "185"},
                                         {"sub" : "CMPSC", "number": "186"},
                                         {"sub" : "CMPSC", "number": "189A"},
                                         {"sub" : "CMPSC", "number": "189B"},
                                         {"sub" : "CMPSC", "number": "190"},
                                         {"sub" : "CMPSC", "number": "192"},
                                         {"sub" : "CMPSC", "number": "196"},
                                         {"sub" : "ECE", "number": "140"},
                                         {"sub" : "ECE", "number": "152B"},
                                         {"sub" : "ECE", "number": "153B"},
                                         {"sub" : "MATH", "number": "108A"},
                                         {"sub" : "MATH", "number": "108B"},
                                         {"sub" : "MATH", "number": "119A"},
                                         {"sub" : "MATH", "number": "119B"},
                                         {"sub" : "MATH", "number": "124A"},
                                         {"sub" : "MATH", "number": "124B"},
                                         {"sub" : "PSTAT", "number": "122"},
                                         {"sub" : "PSTAT", "number": "130"},
                                         {"sub" : "PSTAT", "number": "160A"},
                                         {"sub" : "PSTAT", "number": "160B"},

                                    ], 
                           "units":"20"},

                           {"courses" : [{"sub" : "ANTH", "number" : "5"},
                                         {"sub" : "ASTRO", "number" : "1"},
                                         {"sub" : "ASTRO", "number" : "2"},
                                         {"sub" : "CHEM", "number" : "1A"},
                                         {"sub" : "CHEM", "number" : "1AL"},
                                         {"sub" : "CHEM", "number" : "1B"},
                                         {"sub" : "CHEM", "number" : "1BL"},
                                         {"sub" : "CHEM", "number" : "1C"},
                                         {"sub" : "CHEM", "number" : "1CL"},
                                         {"sub" : "CHEM", "number" : "2A"},
                                         {"sub" : "CHEM", "number" : "2AL"},
                                         {"sub" : "CHEM", "number" : "2B"},
                                         {"sub" : "CHEM", "number" : "2BL"},
                                         {"sub" : "CHEM", "number" : "2C"},
                                         {"sub" : "CHEM", "number" : "2CL"},
                                         {"sub" : "EARTH", "number" : "2"},
                                         {"courses" : [{"sub" : "EARTH", "number": "4"},{"sub" : "EARTH", "number": "4W"}], "units" : "4"},
                                         {"sub" : "EARTH", "number" : "6"},
                                         {"sub" : "EARTH", "number" : "7"},
                                         {"sub" : "EARTH", "number" : "8"},
                                         {"sub" : "EARTH", "number" : "9"},
                                         {"sub" : "EARTH", "number" : "10"},
                                         {"courses" : [{"sub" : "EARTH", "number": "20"},{"sub" : "EARTH", "number": "20W"}], "units" : "4"},
                                         {"sub" : "EARTH", "number" : "30"},
                                         {"sub" : "EARTH", "number" : "111"},
                                         {"sub" : "EARTH", "number" : "123"},
                                         {"sub" : "EARTH", "number" : "130"},
                                         {"sub" : "EEMB", "number" : "21"},
                                         {"sub" : "EEMB", "number" : "22"},
                                         {"sub" : "EEMB", "number" : "40"},
                                         {"sub" : "EEMB", "number" : "50"},
                                         {"sub" : "ENV S", "number" : "2"},
                                         {"sub" : "GEOG", "number" : "3A"},
                                         {"sub" : "GEOG", "number" : "3B"},
                                         {"sub" : "GEOG", "number" : "8"},
                                         {"sub" : "GEOG", "number" : "12"},
                                         {"sub" : "GEOG", "number" : "115A"},
                                         {"sub" : "GEOG", "number" : "115B"},
                                         {"sub" : "GEOG", "number" : "115BL"},
                                         {"sub" : "MCDB", "number" : "1A"},
                                         {"sub" : "MCDB", "number" : "1AL"},
                                         {"courses" : [{"sub" : "MCDB", "number": "1B"},{"sub" : "EEMB", "number": "2"}], "units" : "3"},
                                         {"courses" : [{"sub" : "MCDB", "number": "1BL"},{"sub" : "EEMB", "number": "2L"}], "units" : "1"},
                                         {"sub" : "MCDB", "number" : "20"},
                                         {"sub" : "MCDB", "number" : "21"},
                                         {"sub" : "MCDB", "number" : "23"},
                                         {"sub" : "MCDB", "number" : "26"},
                                         {"sub" : "MCDB", "number" : "27"},
                                         {"sub" : "MCDB", "number" : "29"},
                                         {"sub" : "PHIL", "number" : "183"},
                                         {"sub" : "PHYS", "number" : "4"},
                                         {"sub" : "PHYS", "number" : "4L"},
                                         {"sub" : "PHYS", "number" : "5"},
                                         {"sub" : "PHYS", "number" : "5L"},
                                         {"sub" : "PSY", "number" : "107"},
                                         {"sub" : "PSY", "number" : "108"},
                           ], "units" : "8"}

                           ], 

        "units" : "184"
    }
]

var user = {
    major : "CMPSC",
    majorType : "ENGR"
}

    var geFullFillment

var depth = false
   
var reqNumber = [
            [2,2,6,1,4,1,1],
            [3,3,3,2,2,1,6,1,1,1],
            [3,2,2,1,1,1,6,1,1],
            [2,2,2,1,1,6,1,1]
 ]

var depthSequence = [
    {sub : "CH ST", number : ["1A",  "1B",  "1C" ]},
    {sub : "C LIT", number : ["30A", "30B", "30C"]},
    {sub : "FR",    number : ["50AX", "50BX", "50CX"]},
    {sub : "HIST",  number : ["2A",  "2B",  "2C" ]},
    {sub : "HIST",  number : ["2AH", "2BH", "2CH"]},
    {sub : "HIST",  number : ["4A",  "4B",  "4C" ]},
    {sub : "HIST",  number : ["4AH", "4BH", "4CH"]},
    {sub : "HIST",  number : ["17A", "17B", "17C"]},
    {sub : "HIST",  number : ["17AH","17BH","17CH"]},
    {sub : "PHIL",  number : ["20A" , "20B", "20C"]},
    {sub : "RG ST", number : ["80A",  "80B", "80C"]},
    {sub : "ARTHI", number : ["6A", "6B", "6C", "6D", "6DS", "6DW", "6E", "6F", "6G", "6H", "6K"]}
]


var foreignLanguage = ["GREEK","LATIN","CHIN","JAPAN","GER","HEB","SLAV","FR","ITAL","SPAN","PORT"]

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

//change the expected depth value accordingly
var expectedDepth = false    

//only for test purpose
var count = 0




QUnit.module("Validate All Input", {
	beforeEach: function(){
	    ValidateAllInput(inputCourses);
	},
	afterEach: function(){
	    addedCourses = []; 
	    schedule = [];
	    totalUnit = 0;
	    quarterUnit = []; 
	    invalidData = [];
	    validCourses = [];
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




QUnit.module("check GE", {
	beforeEach: function(){
	    ValidateAllInput(inputCourses);
	},
	afterEach: function(){
	    addedCourses = []; 
	    schedule = [];
	    totalUnit = 0;
	    quarterUnit = []; 
	    invalidData = [];
	    validCourses = [];
	    count = 0;
	}	    
    });
QUnit.test("check fullfillment", function(){
	var geFulfillment = ValidGE();
	var countC = 0;
	var countD = 0;
	var countE = 0;
	var countF = 0;
	var countG = 0;
	var countH = 0;
	var countWRT = 0;
	var countETH = 0;
	var countEUR = 0;
	var countW2 = 0;
	var countW50 = 0;
	var countWOR = 0;
	var countQUR = 0;
	for(var c of inputCourses){
	    for(var ge of GetCourseByName(c.course).gearea){
		if(ge =="C")
		    countC++;
		if(ge == "D")
		    countD++;
		if(ge == "E")
		    countE++;
		if(ge == "F") 
		    countF++;
		if(ge == "G")
		    countG++;
		if(ge == "H")
		    countH++;
		if(ge == "WRT")
		    countWRT++;
		if(ge == "ETH")
		    countETH++;
		if(ge == "EUR")
		    countEUR++;
		if(ge == "WOR")
		    countWOR++;
		if(ge == "QUR")
		    countQUR++;
		if(c.course == "WRIT 2 Academic Writing" || c.course == "WRIT 2E Academic Writing for Engineers")
		    countW2++;
		if(c.course == "WRIT 50 Writing and the Research Process")
		    countW50++;
	    }
	}
	
	if(user.majorType == "ENGR"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");
	    
	    equal(countD + countE >= 2, geFulfillment[0].status, "fulfillment of area D,E is as expected");
	    
	    equal(countF + countG >= 2, geFulfillment[1].status, "fulfillment of area F,G is as expected");
	    
	    equal(countD + countE + countF + countG + countH >= 6, geFulfillment[2].status, "fulfillment of area D,E,F,G,H is as expected");
	    
	    equal(countETH >= 1, geFulfillment[3].status, "fulfillment of area ETH is as expected");
	    
	    equal(countWRT >= 4, geFulfillment[4].status, "fulfillment of area WRIT is as expected");
	    
	    equal(countEUR >= 1, geFulfillment[5].status, "fulfillment of area EUR is as expected");

	    equal(expectedDepth, geFulfillment[6].status, "fulfillment of depth is as expected");

	    equal(countW2 >= 1, geFulfillment[7].status, "fulfillment of writing 2(E) is as expected");
	    
	    equal(countW50 >= 1, geFulfillment[8].status, "fulfillment of writing 50 is as expected");
	    
	}
	else if(user.majorType == "LSBA"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");

	    equal(countW2 >= 1, geFulfillment[0].status, "fulfillment of writing 2(E) is as expected");
	    
	    equal(countW50 >= 1, geFulfillment[1].status, "fulfillment of writing 50 is as expected");
	    
	    /*
	    function of checking area B is not working
	     */

	    equal(countC >= 3, geFulfillment[3].status, "fulfillment of area C is as expected");
	    
	    equal(countD >= 3, geFulfillment[4].status, "fulfillment of area D is as expected");
	    
	    equal(countE >= 3, geFulfillment[5].status, "fulfillment of area E is as expected");
	    
	    equal(countF >= 2, geFulfillment[6].status, "fulfillment of area F is as expected");
	    
	    equal(countG >= 2, geFulfillment[7].status, "fulfillment of area G is as expected");
	    
	    equal(countWOR >= 1, geFulfillment[8].status, "fulfillment of area WOR is as expected");
	    
	    equal(countWRT >= 6, geFulfillment[9].status, "fulfillment of area WRT is as expected");
	    
	    equal(countEUR >= 1, geFulfillment[10].status, "fulfillment of area EUR is as expected");
	    
	    equal(countQUR >= 1, geFulfillment[11].status, "fulfillment of area QUR is as expected");
	    
	    equal(countETH >= 1, geFulfillment[12].status, "fulfillment of area ETH is as expected");
	    
	}
	else if(user.majorType == "LSBS"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");

	    equal(countW2 >= 1, geFulfillment[0].status, "fulfillment of writing 2(E) is as expected");
	    
	    equal(countW50 >= 1, geFulfillment[1].status, "fulfillment of writing 50 is as expected");
	    
	    /*
	    function of checking area B is not working
	     */

	    equal(countC >= 3, geFulfillment[3].status, "fulfillment of area C is as expected");
	    
	    equal(countD >= 2, geFulfillment[4].status, "fulfillment of area D is as expected");
	    
	    equal(countE >= 2, geFulfillment[5].status, "fulfillment of area E is as expected");
	    
	    equal(countF >= 1, geFulfillment[6].status, "fulfillment of area F is as expected");
	    
	    equal(countG >= 1, geFulfillment[7].status, "fulfillment of area G is as expected");
	    
	    equal(countWOR >= 1, geFulfillment[8].status, "fulfillment of area WOR is as expected");
	    
	    equal(countWRT >= 6, geFulfillment[9].status, "fulfillment of area WRT is as expected");
	    
	    equal(countQUR >= 1, geFulfillment[10].status, "fulfillment of area QUR is as expected");
	    
	    equal(countETH >= 1, geFulfillment[11].status, "fulfillment of area ETH is as expected");

	}
	else if(user.majorType == "BMFA"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");

	    equal(countW2 >= 1, geFulfillment[0].status, "fulfillment of writing 2(E) is as expected");
	    
	    equal(countW50 >= 1, geFulfillment[1].status, "fulfillment of writing 50 is as expected");
	    
	    /*
	    function of checking area B is not working
	     */

	    equal(countC >= 2, geFulfillment[3].status, "fulfillment of area C is as expected");
	    
	    equal(countD >= 2, geFulfillment[4].status, "fulfillment of area D is as expected");
	    
	    equal(countE >= 2, geFulfillment[5].status, "fulfillment of area E is as expected");
	    
	    equal(countG >= 1, geFulfillment[6].status, "fulfillment of area G is as expected");
	    
	    equal(countWOR >= 1, geFulfillment[7].status, "fulfillment of area WOR is as expected");
	    
	    equal(countWRT >= 6, geFulfillment[8].status, "fulfillment of area WRT is as expected");
	    
	    equal(countQUR >= 1, geFulfillment[9].status, "fulfillment of area QUR is as expected");
	    
	    equal(countETH >= 1, geFulfillment[10].status, "fulfillment of area ETH is as expected");

	}
    });

/*
QUnit.test("check invalid data", function(){
	deepEqual(invalidData, [], "invalid data is as expected");
    });
QUnit.test("check valid courses", function(){
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




