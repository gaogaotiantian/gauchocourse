
var isValidAP ; 

var raw2apData = function(arr){
    /*
     *arr is an array of course label and the score of the user
     *return the full infos from apData and add the score of user
     *
     */
    var res = [];
    for(var i = 0; i < arr.length ; i++){
	var label = arr[i].label;
	var foo;
	for(var key in apData){
	    console.log(key);
	    if(label == key){
		foo = apData[key];
		console.log("found");
		break;
	    }
	}
	console.log(foo)
	foo.user_score = arr[i].score;
	res.push(foo);
	console.log(res);
    }
    return res;

}


var computeAP = function(arr){


    /*
     * arr is the return type of raw2apData
      
      A maximum of 8 units EACH in art studio, English, mathematics, and physics is allowed.
    */
    
    
    var total_units = 0;
    var ge_areas = [];
    var art = 0;
    var physics = 0;
    var math = 0;
    var english = 0;
    for(var i = 0 ; i < arr.length ; i++){
	if(!arr[i].multi_scores){
	    var label = arr[i].label;
            var units = arr[i].units;
            var ge_area = arr[i].ge.area;
            ge_areas.push(ge_area);
	    total_units += units;
	}
	else{
	    var foo = arr[i][arr[i]["user_score"]];
	    var units = foo.units;
	    var ge_area = foo.ge.area;
	    ge_areas.push(ge_area);
	    total_units += units;
	}
    }
    
    return { "units":total_units , "area":ge_areas};
}
var obj = {
    "label":"Psychology",
    "score":3
}
var arr = [obj];
var res = raw2apData(arr);



/*
var obj =     {
        "scores": [
            3,
            4,
            5
        ],
        "3": {
            "units": "8",
            "course_equivalent": "German 1-3",
            "score": 3,
            "ge": {
                "area": "B"
            }
        },
        "4": {
            "units": "8",
            "course_equivalent": "German 1-4",
            "score": 4,
            "ge": {
                "area": "B"
            }
        },
        "5": {
            "units": "8",
            "course_equivalent": "German 1-5",
            "score": 5,
            "ge": {
                "area": "B"
            }
        },
        "label": "German Language and Culture",
    "multi_scores": true,
    "user_score":4
    } 

var arr = [obj];
var res = computeAP(arr);


*/

//a simple test
/*
var obj = {
	label :"phy",
	units:3,
	ge:{area:"e",score:3}
	}


var arr = [obj]
computeAP(arr)
*/
