//This is the test cases for the back-end functions
//and the database.
//To use the test, please provide your user info, input courses and AP, 
//and all the expected variables accordingly! 
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
		    {course : "PHIL 124B Philosophy of Physics", semester : "freshman_summer"},
		    {course : "PSY 3 The Biological Basis of Psychology", semester : "freshman_spring"},
		    {course : "HIST 17A The American People | Area D, WRT", semester : "sophomore_fall"},
		    {course : "PSY 1 Introduction to Psychology | Area D", semester : "junior_fall"},
		    {course : "HIST 115R Undergraduate Research Seminar in Medieval European History", semester : "senior_winter"}
		    //		    {course : "CMPSCCS 1B Computer Programming and Organization II", semester : "freshman_fall"},
		    ]; //test cases example; add whatever you want


var expectedValidData = [
		    {course : "PHIL 124B Philosophy of Physics", semester : "freshman_summer"},
		    {course : "PSY 3 The Biological Basis of Psychology", semester : "freshman_spring"},
		    {course : "HIST 17A The American People | Area D, WRT", semester : "sophomore_fall"},
		    {course : "PSY 1 Introduction to Psychology | Area D", semester : "junior_fall"},
		    {course : "HIST 115R Undergraduate Research Seminar in Medieval European History", semester : "senior_winter"}
		    //		    {course : "CMPSCCS 1B Computer Programming and Organization II", semester : "freshman_fall"},
		    ]; //test cases example; add whatever you want

var expectedInvalidCourses = [
		    {course : "PHIL 124B Philosophy of Physics", semester : "freshman_summer"},
		    {course : "PSY 3 The Biological Basis of Psychology", semester : "freshman_spring"},
		    {course : "HIST 17A The American People | Area D, WRT", semester : "sophomore_fall"},
		    {course : "PSY 1 Introduction to Psychology | Area D", semester : "junior_fall"},
		    {course : "HIST 115R Undergraduate Research Seminar in Medieval European History", semester : "senior_winter"}
		    //		    {course : "CMPSCCS 1B Computer Programming and Organization II", semester : "freshman_fall"},
		    ]; //test cases example; add whatever you want


//change the expected variables accordingly
var expectedDepth = false    
var expectedW2 = false
var expectedW50 = false
var expectedB = false
var expectedC = false
var expectedD = false
var expectedE = false
var expectedF = false
var expectedG = false
var expectedDE = true
var expectedFG = false
var expectedDEFGH = false
var expectedWOR = false
var expectedWRT = false
var expectedEUR = false
var expectedQUR = false
var expectedETH = false
//only for test purpose
var count = 0

    //ap score test cases
var inputAP = [

{"label":"European History","score":3}
,
{"label":"Physics  C (Electricity and Magnetism)","score":3}
,
{"label":"Music  Theory","score":5}
,
{"label":"English Language and Composition or Literature and Composition","score":3}
,
{"label":"Physics  C (Electricity and Magnetism)","score":5}
,
{"label":"European History","score":3}
,
{"label":"U.S. History","score":3}
,
{"label":"English Language and Composition or Literature and Composition","score":4}
,
{"label":"Physics  C (Mechanics)","score":4}
,
{"label":"French Language and Culture","score":3}
,
{"label":"U.S. Government and Politics","score":3}
,
{"label":"Statistics","score":5}
,
{"label":"German Language and Culture","score":3}
,
{"label":"Economics  Macroeconomics","score":4}
,
{"label":"Art Studio Drawing","score":3}
,
{"label":"Human Geography","score":4}
,
{"label":"Physics  B","score":4}
,
{"label":"World History","score":5}
,
{"label":"Economics  Microeconomics","score":4}
,
{"label":"English Language and Composition or Literature and Composition","score":5}
];


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
/*
QUnit.test("check invalid data", function(){
	for(var course of valid){}
	    
    });
QUnit.test("check valid courses", function(){
	deepEqual(validCourses, [], "valid courses are as expected");
    });
*/






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
	ValidGE();
	var geFulfillment = geFullFillment;
	if(user.majorType == "ENGR"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");
	    
	    equal(geFulfillment[0].status, expectedW2, "fulfillment of writing 2(E) is as expected");
	    
	    equal(geFulfillment[1].status, expectedW50, "fulfillment of writing 50 is as expected");
	    
	    equal(geFulfillment[2].status, expectedDE, "fulfillment of area D,E is as expected");
	    
	    equal(geFulfillment[3].status, expectedFG, "fulfillment of area F,G is as expected");
	    
	    equal(geFulfillment[4].status, expectedDEFGH, "fulfillment of area D,E,F,G,H is as expected");
	    
	    equal(geFulfillment[5].status, expectedETH, "fulfillment of area ETH is as expected");
	    
	    equal(geFulfillment[6].status, expectedWRT, "fulfillment of area WRIT is as expected");
	    
	    equal(geFulfillment[7].status, expectedEUR, "fulfillment of area EUR is as expected");

	    equal(geFulfillment[8].status, expectedDepth, "fulfillment of depth is as expected");

	}
	else if(user.majorType == "LSBA"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");

	    equal(geFulfillment[0].status, expectedW2, "fulfillment of writing 2(E) is as expected");
	    
	    equal(geFulfillment[1].status, expectedW50, "fulfillment of writing 50 is as expected");
	    
	    /*
	    function of checking area B is not working
	     */

	    equal(geFulfillment[3].status, expectedC, "fulfillment of area C is as expected");
	    
	    equal(geFulfillment[4].status, expectedD, "fulfillment of area D is as expected");
	    
	    equal(geFulfillment[5].status, expectedE, "fulfillment of area E is as expected");
	    
	    equal(geFulfillment[6].status, expectedF, "fulfillment of area F is as expected");
	    
	    equal(geFulfillment[7].status, expectedG, "fulfillment of area G is as expected");
	    
	    equal(geFulfillment[8].status, expectedWOR, "fulfillment of area WOR is as expected");
	    
	    equal(geFulfillment[9].status, expectedWRT, "fulfillment of area WRT is as expected");
	    
	    equal(geFulfillment[10].status, expectedEUR, "fulfillment of area EUR is as expected");
	    
	    equal(geFulfillment[11].status, expectedQUR, "fulfillment of area QUR is as expected");
	    
	    equal(geFulfillment[12].status, expectedETH, "fulfillment of area ETH is as expected");
	    
	}
	else if(user.majorType == "LSBS"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");


	    equal(geFulfillment[0].status, expectedW2, "fulfillment of writing 2(E) is as expected");
	    
	    equal(geFulfillment[1].status, expectedW50, "fulfillment of writing 50 is as expected");
	    
	    equal(geFulfillment[2].status, expectedB, "fulfillment of area B is as expected");

	    equal(geFulfillment[3].status, expectedC, "fulfillment of area C is as expected");
	    
	    equal(geFulfillment[4].status, expectedD, "fulfillment of area D is as expected");
	    
	    equal(geFulfillment[5].status, expectedE, "fulfillment of area E is as expected");
	    
	    equal(geFulfillment[6].status, expectedF, "fulfillment of area F is as expected");
	    
	    equal(geFulfillment[7].status, expectedG, "fulfillment of area G is as expected");
	    
	    equal(geFulfillment[8].status, expectedWOR, "fulfillment of area WOR is as expected");
	    
	    equal(geFulfillment[9].status, expectedWRT, "fulfillment of area WRT is as expected");
	    
	    equal(geFulfillment[10].status, expectedQUR, "fulfillment of area QUR is as expected");
	    
	    equal(geFulfillment[11].status, expectedETH, "fulfillment of area ETH is as expected");

	}
	else if(user.majorType == "BMFA"){
	    //only for testing the tests
	    //deepEqual(geFulfillment, [], "test to see the format");

	    equal(geFulfillment[0].status, expectedW2, "fulfillment of writing 2(E) is as expected");
	    
	    equal(geFulfillment[1].status, expectedW50, "fulfillment of writing 50 is as expected");
	    
	    equal(geFulfillment[2].status, expectedB, "fulfillment of area B is as expected");

	    equal(geFulfillment[3].status, expectedC, "fulfillment of area C is as expected");
	    
	    equal(geFulfillment[4].status, expectedD, "fulfillment of area D is as expected");
	    
	    equal(geFulfillment[5].status, expectedE, "fulfillment of area E is as expected");
	    
	    equal(geFulfillment[6].status, expectedG, "fulfillment of area G is as expected");
	    
	    equal(geFulfillment[7].status, expectedWOR, "fulfillment of area WOR is as expected");
	    
	    equal(geFulfillment[8].status, expectedWRT, "fulfillment of area WRT is as expected");
	    
	    equal(geFulfillment[9].status, expectedQUR, "fulfillment of area QUR is as expected");
	    
	    equal(geFulfillment[10].status, expectedETH, "fulfillment of area ETH is as expected");
	}
    });



/*
QUnit.module("check AP");

QUnit.test("check units", function(){
	equal(run_AP_analysis(inputAP), [], "check the result");
    });
*/





